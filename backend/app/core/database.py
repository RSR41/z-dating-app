# backend/app/core/database.py

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Pydantic에서 환경 변수는 대소문자를 구분하지 않지만
# 코드 가독성을 위해 대문자 속성을 그대로 사용한다.
engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# 의존성 주입용
async def get_db():
    async with async_session() as session:
        yield session
