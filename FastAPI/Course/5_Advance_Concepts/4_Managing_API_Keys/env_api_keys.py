from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str = ""  # satisfy type checker

    class Config:
        env_file = ".env"

app = FastAPI()
settings = Settings()

def require_api_key(api_key: str = Header(...)) -> str:
    if not settings.api_key:
        raise RuntimeError("API Key Not Configured(missing api_key in .env / env vars).")
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key

@app.get("/get-data")
def get_data(api_key: str = Depends(require_api_key)):
    return {"Output": "Access Granted!"}