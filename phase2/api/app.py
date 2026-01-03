from fastapi import FastAPI
from phase2.api.routes import router

app = FastAPI(
    title="VIX Phase 2 API",
    version="2.0"
)

app.include_router(router)
