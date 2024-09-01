from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.city.models import DBCity
from app.city.schemas import City, CityCreate


async def get_all_city(db: AsyncSession) -> [City]:
    result = await db.execute(select(DBCity))
    db_cities = result.scalars().all()
    return db_cities


async def create_city(db: AsyncSession, city: CityCreate):
    new_city = DBCity(**city.dict())
    db.add(new_city)
    await db.commit()
    await db.refresh(new_city)
    return new_city
