# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI, using HTTP methods, path parameters, request validation, and appropriate status codes to manage a collection of books.

## 📝 Tasks

### 🛠️ Create a Books Collection Endpoint

#### Description
Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`. Complete the starter code so the API returns the books in its in-memory collection. Run it with `uvicorn starter-code:app --reload` and inspect the interactive API documentation at `/docs`.

#### Requirements
Completed program should:

- Define a `GET /books` endpoint that returns every book as JSON
- Return each book's `id`, `title`, and `author`
- Return an empty JSON list if the collection has no books


### 🛠️ Retrieve a Book by ID

#### Description
Add an endpoint that looks up one book using its ID from the URL. Return a clear `404 Not Found` response when no book has that ID.

#### Requirements
Completed program should:

- Define a `GET /books/{book_id}` endpoint
- Return the matching book when its ID exists
- Raise an `HTTPException` with status code `404` when the ID is unknown


### 🛠️ Add a Book with Request Validation

#### Description
Use the provided Pydantic request model to accept a new book. Add it to the in-memory collection and return the created book with a newly assigned ID.

#### Requirements
Completed program should:

- Define a `POST /books` endpoint that accepts a book title and author
- Return the created book with a unique integer ID and status code `201 Created`
- Let FastAPI reject requests that omit required fields or provide values of the wrong type