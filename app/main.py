from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Stock Analyzer API")

app.include_router(router)