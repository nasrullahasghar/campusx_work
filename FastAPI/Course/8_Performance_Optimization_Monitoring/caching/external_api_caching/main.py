import json
import redis
import hashlib
import httpx
from pydantic import BaseModel
from typing import cast
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

app = FastAPI()
redis_client = redis.Redis(host='localhost',port=6379,db=0)

class PostRequest(BaseModel):
    post_id: int

def make_cache_key(post_id:int):
    raw = f"external_api:post_{post_id}"
    return hashlib.sha256(raw.encode()).hexdigest()

# Exception Handling
@app.exception_handler(Exception)
async def general_exception_handler(request:Request,exc:Exception):
    return JSONResponse(status_code=500,content={'error':str(exc)})

@app.post("/get-post")
async def get_post(data:PostRequest):
    cache_key = make_cache_key(data.post_id)
    cached_data = redis_client.get(cache_key)
    if cached_data:
        print("Served from redis Cached!")
        return json.loads(cast(str,cached_data))
    
    print("Calling external API...")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{data.post_id}")
        if response.status_code != 200:
            return {"error":"Post Not Found!"}
        post_data = response.json()
        # make it cache
        redis_client.setex(cache_key,600,json.dumps(post_data))
        print("Fetched and stored in Cache!")
        return post_data