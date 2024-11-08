from pydantic import BaseModel


class STaskCreate(BaseModel):
    name: str
    description: str | None


class STaskGet(STaskCreate):
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int