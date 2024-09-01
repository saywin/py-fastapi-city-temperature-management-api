from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.temperature.models import DBTemperature


async def get_temperature_by_city_id(db: AsyncSession, city_id: int) -> DBTemperature:
    find_temperature_by_id = select(DBTemperature).where(DBTemperature.city_id == city_id)
    result = await db.execute(find_temperature_by_id)
    return result.scalars().first()


async def update_temperature(db: AsyncSession, city_id: int, new_temperature: float) -> DBTemperature:
    temp_entry = await get_temperature_by_city_id(db, city_id)
    if temp_entry:
        temp_entry.temperature = new_temperature
        temp_entry.date_time = datetime.utcnow()
        db.add(temp_entry)
        await db.commit()
        await db.refresh(temp_entry)
    return temp_entry
