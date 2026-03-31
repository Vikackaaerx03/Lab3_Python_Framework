# Laboratory Work No. 3

## Project Title
Order Management Web Application

## Individual Assignment
Variant 11

Entity: `Order`

Fields:
- `id` - unique identifier
- `order_number` - order number
- `customer_name` - customer name
- `total_price` - total amount
- `order_date` - order date

## Laboratory Task
The task for Laboratory Work No. 3 was:

1. Create a web application according to the individual assignment.
2. Connect an SQLite database.
3. Create a model with 2-3 or more fields.
4. Implement CRUD operations.
5. Display data on a web page.

## Implemented Solution
This project implements the assignment as an order management web application.

The current version is built with:
- `FastAPI`
- `SQLite`
- `SQLAlchemy`
- `Jinja2`
- `Uvicorn`

Note: the assignment text mentions Django, but this repository contains a working FastAPI implementation.

## Features
- Create a new order
- View the list of orders
- Edit existing orders
- Delete orders
- Store data in SQLite
- Validate form input
- Display orders on HTML pages

## Order Validation
The application validates:
- `order_number` must contain exactly 3 digits in the format `001`
- `order_number` must follow the next available sequence number
- `customer_name` cannot be empty and must have a valid length
- `total_price` must be greater than `0`
- `order_date` cannot be in the future

Example:
- If the existing order numbers are `001`, `002`, `003`, the next valid number is `004`

## Project Structure
```text
app/
  main.py
  database.py
  models.py
  schemas.py
  crud.py
  router/
    order.py
  templates/
    index.html
    create.html
    edit.html
  static/
    style.css
orders.db
```

## Database
The application uses SQLite database file:

```text
orders.db
```

The `Order` table stores all order records.

## CRUD Operations
The following CRUD operations are implemented:

- Create: add a new order
- Read: display all orders on the main page
- Update: edit order information
- Delete: remove an order from the database

## How to Run
Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000
```

## Result
The developed web application allows the user to manage orders through a simple web interface, supports SQLite database storage, performs CRUD operations, and displays data on web pages according to the requirements of Laboratory Work No. 3.
