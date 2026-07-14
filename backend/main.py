from fastapi import FastAPI
from backend.api.routes import router
from backend.config.settings import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)
app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": settings.VERSION}
