from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware, # <--------- Built-in CORS middleware to control cross-origin requests.
    allow_origins=[
        "https://my-frontend.com",  # Allowed production frontend origin
        "http://localhost:3000",    # Allowed local dev frontend origin
    ],
    allow_credentials=True,          # Allow cookies/authorization info to be sent
    allow_methods=["GET","POST","PUT","DELETE"],  # Allowed HTTP methods
    allow_headers=["*"],            # Allow all request headers
)

# Define End-Points
# ------------------------>
# ------------------------>
# ------------------------>
# ------------------------>
# ------------------------>
# ------------------------>

