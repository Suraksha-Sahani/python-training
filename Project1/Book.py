from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    category: str

MY_BOOKS = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction"},
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help"},
    {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "History"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Classic"},
    {"title": "The Art of War", "author": "Sun Tzu", "category": "Strategy"},
    {"title": "1984", "author": "George Orwell", "category": "Dystopian"},
]

@app.get("/books")
def read_all_books():
    return MY_BOOKS

@app.get("/books/{book_title}")
def _book(book_title: str):
    for book in MY_BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_book_category(category: str):
    books_to_return = [book for book in MY_BOOKS if book.get('category').casefold() == category.casefold()]
    return books_to_return

@app.get("/books/{title}/")
async def filter_by_title_category(title: str, category: str):
    filtered_books = [
        book for book in MY_BOOKS
        if book.get('title').casefold() == title.casefold() and book.get('category').casefold() == category.casefold()
    ]
    return filtered_books

@app.post("/books/create_book")
async def create_book(new_book: Book = Body(...)):
    MY_BOOKS.append(new_book.dict())
    return {"message": "New Book has been created!", "book": new_book}


@app.put("/books/update_book")
async def update_book(updated_book: Book = Body(...)):
    for i in range(len(MY_BOOKS)):
        if MY_BOOKS[i].get('title').casefold() == updated_book.title.casefold():
            MY_BOOKS[i] = updated_book.dict()
    return {"message": "Book has been updated!", "book": updated_book}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(MY_BOOKS)):
        if MY_BOOKS[i].get('title').casefold() == book_title.casefold():
            MY_BOOKS.pop(i)
            return {"book has been successfully deleted!"}

    return {"Not Found!"}