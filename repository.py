from sqlalchemy import select
from db import session, TaskTable
from schemas import STaskCreate


class TaskRepository:
    @staticmethod
    async def create_one(data: STaskCreate) -> int:
        async with session() as db:
            task_dict = data.model_dump()
            task = TaskTable(**task_dict)
            db.add(task)
            await db.flush()
            await db.commit()
            return task.id

    @staticmethod
    async def get_all() -> list[STaskCreate]:
        async with session() as db:
            query = select(TaskTable)
            result = await db.execute(query)
            tasks = result.scalars().all()
            task_schemas = [STaskCreate.model_validate(task_model) for task_model in tasks]
            return task_schemas
