from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

# FastAPI application instance
app = FastAPI()

# Automatically redirects HTTP requests to HTTPS
app.add_middleware(HTTPSRedirectMiddleware)