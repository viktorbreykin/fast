import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=5001, log_level="info", reload=True)
