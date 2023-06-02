from fastapi import FastAPI, Body
import schemas
import uuid

app = FastAPI()

BookLibrary = {
    
}

@app.get("/books/")
def getBooks():
    return BookLibrary
    

@app.get("/books/{id}")
def getBooksByID(id:str):
    return BookLibrary[id]
    
@app.post("/books/")
def addBook(book:schemas.Book):
    newBook = len(BookLibrary.keys()) + 1
    newid = uuid.uuid1()
    BookLibrary[newBook] = {newid:book}
    return newid
    
    
@app.put("/books/{id}")
def bookUpdate(id:int, book:schemas.Book):
    BookLibrary[id]["title"] = book.title
    BookLibrary[id]["author"] = book.author
    BookLibrary[id]["year"] = book.year

@app.delete()