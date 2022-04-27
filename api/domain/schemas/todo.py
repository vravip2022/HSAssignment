from api.domain.schemas.schema_base import SchemaBase


class TodoBase(SchemaBase):
    id: int
    description: str
    user_id: int

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    #user_id: int
    class Config:
        orm_mode = True

class TodoResponse(Todo): 
    pass