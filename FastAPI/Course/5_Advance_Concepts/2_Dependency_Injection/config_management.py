from fastapi import FastAPI,Depends

app = FastAPI()

class Settings:
    def __init__(self) -> None:
        self.api_key = 'my_secret'
        self.bug = True

def get_setting():
    return Settings()


@app.get("/config")
def get_config(settings: Settings = Depends(get_setting)):
    return {"api_key": settings.api_key}