# Book API

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
6. Access the API at `http://localhost:8000/api/books`

## API Endpoints

- **Create Book**: `POST /api/books/create/`
- **Get Book by ID**: `GET /api/books/{id}/`
- **Get Books with Filters**: `GET /api/books/`
- **Update Book**: `PUT /api/books/{id}/update/`
- **Delete Book**: `DELETE /api/books/{id}/delete/`




## HOW TO RUN


Create a Book: Navigate to http://127.0.0.1:8000/api/books/ and use a form or tool to POST the JSON data.

Get Book by ID: Visit http://127.0.0.1:8000/api/books/1/ to see details of the book with ID 1.

Update a Book: Use a form or tool to PUT JSON data to http://127.0.0.1:8000/api/books/1/.

Delete a Book: Navigate to http://127.0.0.1:8000/api/books/1/ and perform a DELETE request.