from fastapi import FastAPI
from config import settings

# FastAPI 앱 설정
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None
)


@app.get("/")
async def root():
    """기본 엔드포인트"""
    return {"message": "FastAPI Application"}


@app.get("/config")
async def get_config():
    """현재 환경설정 값 확인"""
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "environment": settings.environment,
        "host": settings.host,
        "port": settings.port,
        "database_url": settings.database_url,
        "secret_key": settings.secret_key[:4] + "..." if settings.secret_key else None
    }