from typing import Annotated
from fastapi import Depends, APIRouter

from repository import TaskRepository
from schemas import STaskCreate, STaskGet, STaskId

router = APIRouter(
    prefix="/tasks"
)


@router.post("")
async def create_task(
        task: Annotated[STaskCreate, Depends()],
) -> STaskId:
    task_id = await TaskRepository.create_one(task)
    return {'ok': True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STaskCreate]:
    tasks = await TaskRepository.get_all()
    return tasks
