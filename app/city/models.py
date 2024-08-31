from sqlalchemy import Column, Integer, String

from app.db import Base


class DBCity(Base):
    __tablename__ = "city"

    id = Column(Integer, index=True, primary_key=True)
    city = Column(String(255), unique=True, index=True)
    additional_info = Column(String(510))
