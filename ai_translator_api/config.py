import os
from dotenv import load_dotenv


load_dotenv("../env/.api.env")


class Settings:
    ENV: str = os.getenv("ENV")

    API_HOST: str = os.getenv("API_HOST")
    API_PORT: str = os.getenv("API_PORT")
    ORIGIN_PORT: str = os.getenv("ORIGIN_PORT")

    AZURE_AI_KEY: str = os.getenv("AZURE_AI_KEY")
    AZURE_AI_REGION: str = os.getenv("AZURE_AI_REGION")

    ORIGINS: str = f"http://{API_HOST}:{ORIGIN_PORT}"


settings = Settings()
