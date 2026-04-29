from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

API_KEY = "my-secret-key"

def get_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403,detail="Unauthroized")
    return api_key

@app.get("/get-data")
def get_data(api_key: str = Depends(get_key)):
    return {"Output":"Access Granted!"}