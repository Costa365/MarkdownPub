from pydantic import BaseModel


class MarkDown(BaseModel):
    doc: str


class MarkDownUpdate(BaseModel):
    doc: str
    editId: str
