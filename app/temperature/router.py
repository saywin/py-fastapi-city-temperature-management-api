from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.city.models import DBCity
from app.city.schemas import City
from app.dependencies import get_session
from app.temperature import schemas
from app.temperature.crud import create_temp_record
from app.temperature.weather import fetch_temperature_data

router = APIRouter(tags=["Temperature"])


@router.post("/update/", response_model=list[schemas.TemperatureUpdate])
async def temp_update(db: AsyncSession = Depends(get_session)):
    cities_result = await db.execute(select(DBCity))
    cities = cities_result.scalars().all()
    updated_cities = []

    for city in cities:
        temp = await fetch_temperature_data(city.city)
        created_entry = await create_temp_record(
            city_id=city.id, temp=temp, db=db)
        updated_cities.append({
            "city_id": created_entry.city_id,
            "temperature": created_entry.temperature,
            "date_time": created_entry.date_time
        })

    return updated_cities
