# import asyncio
#
# from sqlalchemy.ext.asyncio import create_async_engine
#
# from app.core.config import config
# from app.models.models import Base
#
#
# async def tables():
#     engine = create_async_engine(config.db.database_url)
#
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#         print("✅ Таблицы созданы!")
#
#
# if __name__ == "__main__":
#     asyncio.run(tables())
