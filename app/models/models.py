from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(BigInteger, unique=True, index=True)
    full_name = Column(String)
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime)
