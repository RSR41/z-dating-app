from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- 내부 모듈 ---
from app.core.config import settings
from app.core.logging import logger          # ← 추가
from app.api.api_v1.api import api_router
from app.api.api_v1.endpoints.health import router as health_router  # ← 추가

app = FastAPI(
    title="z-dating-app API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS ── 프런트 dev 도메인만 우선 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# 라우터
# ─────────────────────────────────────────────
app.include_router(health_router)            # /healthcheck
app.include_router(api_router, prefix="/api/v1")

# ─────────────────────────────────────────────
# 이벤트 훅 (선택)
# ─────────────────────────────────────────────
@app.on_event("startup")
async def on_startup() -> None:
    logger.info("🚀  FastAPI started")

@app.on_event("shutdown")
async def on_shutdown() -> None:
    logger.info("🛑  FastAPI stopped")
