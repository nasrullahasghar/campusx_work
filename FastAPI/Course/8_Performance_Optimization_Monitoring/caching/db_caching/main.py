import sqlite3
import redis
import hashlib
import json
from typing import cast
from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
app = FastAPI()

redis_client = redis.Redis(host='localhost',port=6379,db=0)

# establish db connection
def get_db_connection():
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn

# setup database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")  # or DROP TABLE + recreate

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)

    cursor.execute("INSERT INTO users (id, name, age) VALUES (1, 'Michael', 45)")
    cursor.execute("INSERT INTO users (id, name, age) VALUES (2, 'Jim', 35)")
    cursor.execute("INSERT INTO users (id, name, age) VALUES (3, 'Pam', 27)")

    conn.commit()
    conn.close()

# Invoke the methond of db
init_db()

class UserQuery(BaseModel):
    user_id: int

def make_cache_key(user_id: int):
    raw = f"user:{user_id}"
    return hashlib.sha256(raw.encode()).hexdigest()

# Exception Handling
@app.exception_handler(Exception)
async def general_exception_handler(request: Request,exc: Exception):
    return JSONResponse(
        status_code=500,
        content = {"error": str(exc)}
    )

@app.post("/get-user")
def get_user(query: UserQuery):
    cache_key = make_cache_key(query.user_id)
    # get the data
    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("Serving from Redis Cache!")
        return json.loads(cast(str,cached_data))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id =?",(query.user_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return {"message":"User Not Found!"}
    
    result = {'id':row['id'],'name':row['name'],'age':row['age']}
    redis_client.setex(cache_key,3600,json.dumps(result))
    print("Fetched From DB and Cached!")
    return result