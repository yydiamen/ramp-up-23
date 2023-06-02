from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from uuid import UUID,uuid4


class BookInfo(BaseModel):
    title: str
    author: str
    year: int

class Book(BookInfo):
    uid: UUID


db: dict[UUID, Book] = dict()

app = FastAPI()

@app.post("/books", status_code=status.HTTP_201_CREATED)
def post_book(book_info: BookInfo):
    book: Book = Book(
        author=book_info.author,
        title = book_info.title,
        year = book_info.year,
        uid = uuid4()
    )
    db[book.uid] = book
    return book

@app.get("/books")
def get_all_books():
    return [book for book in db.values()]

@app.get("/books/{uid}")
def get_book_by_id(uid: UUID, response: Response):
    book: Book = db.get(uid)
    if book is None:
        response.status_code = status.HTTP_404_NOT_FOUND
    return book

@app.put("/books/{uid}")
def update_book_by_id(uid: UUID, book_info: BookInfo, response: Response):
    book: Book = db.get(uid)
    if not book is None:
        book.author = book_info.author
        book.year = book_info.year
        book.title = book_info.title
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
    return book

@app.delete("/books/{uid}")
def delete_book_by_id(uid: UUID, response: Response):
    book = db.get(uid)
    if not book is None:
        del db[uid]
        return book
    else:
        response.status_code = status.HTTP_404_NOT_FOUND