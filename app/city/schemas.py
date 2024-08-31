from pydantic import BaseModel


class CityBase(BaseModel):
    city: str
    additional_info: str


class City(CityBase):
    id: int


class CityCreate(CityBase):
    pass
