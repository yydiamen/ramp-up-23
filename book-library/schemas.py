from pydantic import BaseModel
class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
