import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/wait")
async def wait():
    await asyncio.sleep(3)
    return {"message":"Finished Waiting!"}