from fastapi import FastAPI
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

@app.post("/books")
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
def get_book_by_id(uid: UUID):
    book: Book = db.get(uid)
    return book

@app.put("/books/{uid}")
def update_book_by_id(uid: UUID, book_info: BookInfo):
    book: Book = db.get(uid)
    if not book is None:
        book.author = book_info.author
        book.year = book_info.year
        book.title = book_info.title
    return book

@app.delete("/books/{uid}")
def delete_book_by_id(uid: UUID):
    book = db.get(uid)
    if not book is None:
        del db[uid]
        return book
    else:
        return book