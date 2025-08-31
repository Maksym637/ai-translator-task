import os
from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()


app = FastAPI(
    title=f"ai-translator-api-{os.getenv('ENV')}",
    description="An AI-powered translator API that provides real-time text translation",
)


@app.get("/translator")
def perform_translation():
    return {"message": "Hello AI-powered translator!"}
