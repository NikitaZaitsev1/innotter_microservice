from fastapi import FastAPI

from app.core.settings import get_settings

settings = get_settings()

app = FastAPI(title="microservice", debug=settings.DEBUG)
