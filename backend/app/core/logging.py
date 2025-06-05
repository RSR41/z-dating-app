"""
Loguru-based 통합 로거 모듈
"""
from pathlib import Path
from loguru import logger

LOG_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger.remove()  # default stdout 제거 후 원하는 핸들러 재등록

# 콘솔(개발)
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="DEBUG",
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}:{line}</cyan> - {message}",
)

# 파일(운영/공통)
logger.add(
    LOG_DIR / "app.log",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)
