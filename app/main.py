import asyncio

from fastapi import FastAPI


from app.city.router import router

app = FastAPI()


app.include_router(router, prefix="/city")


@app.get("/")
async def root():
    return {"message": "Hello World"}
