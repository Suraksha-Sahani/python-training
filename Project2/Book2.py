from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    Book(1, "Advanced Programing Concepts", "Roby", "Sample Description for APC", 5),
    Book(2, "Be Fast with FastAPI", "Roby", "Sample Description for FastAPI", 4),
    Book(3, "Master Endpoints ", "Roby", "Sample Description for ME", 5),
    Book(4, "Computer Science Pro", "Roby", "Sample Description for CSPro", 5)
]

@app.get("/my-books")
async def get_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book_without_validation(request_book=Body()):
    return BOOKS.append(request_book)

@app.post("create-book-with-validation")
async def create_book_with_validation(book_request: BookRequest):
    # ** shows that key value in the dictionary
    new_book = Book(**book_request.dict())
    return BOOKS.append(new_book)


