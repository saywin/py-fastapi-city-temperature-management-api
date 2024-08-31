from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.city.schemas import City


async def get_all_city(db: AsyncSession) -> list[City]:
    db_city = await db.execute(select(City))
    return db_city.scalar().all()


def create_city(db: AsyncSession, city: str, additional_info: str):
    new_city = City(city=city, additional_info=additional_info)
    db.add(new_city)
    return new_city
