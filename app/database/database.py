# from contextlib import asynccontextmanager
#
# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
#
# from app.core.config import config
#
#
# DATABASE_URL = config.db.database_url
#
# engine = create_async_engine(DATABASE_URL, echo=False)
# AsincSessionLocal = async_sessionmaker(
#     engine, expire_on_commit=False, class_=AsyncSession
# )
#
#
# @asynccontextmanager
# async def get_db():
#     async with AsincSessionLocal() as session:
#         try:
#             yield session
#             await session.commit()
#         except Exception:
#             await session.rollback()
#             raise
#         finally:
#             await session.close()
