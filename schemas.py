from pydantic import BaseModel, ConfigDict


class STaskCreate(BaseModel):
    name: str
    description: str | None


class STaskGet(STaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
