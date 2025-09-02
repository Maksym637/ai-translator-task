from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.translator import translator_router
from config import settings


app = FastAPI(
    title=f"ai-translator-api-{settings.ENV}",
    description="An AI-powered translator API that provides real-time text translation",
)

app.include_router(translator_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
