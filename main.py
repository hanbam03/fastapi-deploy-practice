from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 운영환경에서는 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "배포성공!",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    """서버 상태 확인용 엔드포인트"""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.get("/info")
def app_info():
    return {
        "app_name": "FastAPI 배포 실습",
        "python_version": "3.11",
        "framework": "FastAPI",
        "debug_mode": os.getenv("DEBUG", "false").lower() == "true"
    }