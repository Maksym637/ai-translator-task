import os
from dotenv import load_dotenv


load_dotenv("../env/.api.env")


class Settings:
    ENV: str = os.getenv("ENV")

    API_HOST: str = os.getenv("API_HOST")
    API_PORT: str = os.getenv("API_PORT")

    AZURE_AI_KEY: str = os.getenv("AZURE_AI_KEY")
    AZURE_AI_REGION: str = os.getenv("AZURE_AI_REGION")


settings = Settings()
