import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # 기본 설정
    app_name: str = "FastAPI App"
    debug: bool = False
    environment: str = "development"

    # 보안 관련 (반드시 설정 필요)
    secret_key: str = "change-this-in-production"

    # 데이터베이스
    database_url: str = "sqlite:///./app.db"

    # 서버 설정
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# 전역 설정 인스턴스
settings = Settings()