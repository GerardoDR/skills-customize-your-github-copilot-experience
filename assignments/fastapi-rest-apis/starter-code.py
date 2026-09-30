from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


class Book(BookCreate):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle"),
    Book(id=3, title="The Giver", author="Lois Lowry"),
]


@app.get("/books", response_model=list[Book])
def list_books():
    raise NotImplementedError("Complete the GET /books endpoint")


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    raise NotImplementedError("Complete the GET /books/{book_id} endpoint")


@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    raise NotImplementedError("Complete the POST /books endpoint")