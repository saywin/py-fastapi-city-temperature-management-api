from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.city import schemas, crud
from app.dependencies import get_session

router = APIRouter()


@router.get("/", response_model=list[schemas.City])
async def read_cities(db: AsyncSession = Depends(get_session)):
    return await crud.get_all_city(db=db)


@router.post("/", response_model=schemas.CityCreate)
async def add_city(
        city: schemas.CityCreate,
        db: AsyncSession = Depends(get_session)
):
    city = await crud.create_city(
        db=db,
        city=city
    )
    await db.commit()
    return city
