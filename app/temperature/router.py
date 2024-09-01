from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.city.models import DBCity
from app.city.schemas import City
from app.dependencies import get_session
from app.temperature import schemas
from app.temperature.crud import update_temperature
from app.temperature.weather import fetch_temperature_data

router = APIRouter(tags=["Temperature"])


@router.post("/update/", response_model=list[schemas.TemperatureUpdate])
async def temp_update(db: AsyncSession = Depends(get_session)):
    cities_result = await db.execute(select(DBCity))
    cities = cities_result.scalars().all()
    updated_cities = []

    for city in cities:
        temp = await fetch_temperature_data(city.city)
        await update_temperature(city_id=city.id, new_temperature=temp, db=db)

        updated_cities.append({
            "city_id": city.id,
            "temperature": temp,
            "date_time": "2024-09-01T12:00:00Z"
        })
    return updated_cities

