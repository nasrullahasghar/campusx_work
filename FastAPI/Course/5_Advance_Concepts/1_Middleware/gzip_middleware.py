from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

# FastAPI application instance
app = FastAPI()

# Built-in GZip middleware to compress responses and reduce payload size
app.add_middleware(
    GZipMiddleware,            # Enables gzip compression for eligible responses
    minimum_size=1000,        # Only compress responses larger than 1000 bytes
)