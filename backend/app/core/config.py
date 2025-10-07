from pydantic import EmailStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_username: str
    smtp_password: str
    email_from: EmailStr

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",  # ignore extra env vars outside model fields
        env_prefix="",   # Optional, if your env vars don't have common prefix
    )

settings = Settings()
