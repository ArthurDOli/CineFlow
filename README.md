# CineFlow API

CineFlow API is the backend for a cinema management system, developed in Python with the FastAPI framework. The application allows for the registration and control of movies, rooms, screening sessions, and ticket sales.

## Features

- **Movie Management:** Endpoints to create, list, update, and delete movies from the catalog.
- **Room Management:** Endpoints for the complete control of cinema rooms, including name and capacity.
- **Session Scheduling:** A complete system for scheduling sessions, with robust logic that prevents scheduling conflicts in the same room.
- **Ticket Sales:** An endpoint to "buy" a ticket for a specific session, with validation to prevent selling already occupied seats.
- **Data Querying:** Routes to list all registered resources and to view tickets sold per session.

## Technologies Used

- **Backend:** Python, FastAPI
- **Database:** SQLite with SQLAlchemy

## Installation and Setup

Follow the steps below to set up and run the project locally:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ArthurDOli/CineFlow.git
    cd CineFlow
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the database:**
    This project uses SQLite and does not require environment variable configuration. To create the initial database, run the script:

    ```bash
    python database.py
    ```

5.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available with interactive documentation at `http://127.0.0.1:8000/docs`.

## Project Structure

```
CineFlow/
├── routers/
│ ├── movie.py
│ ├── room.py
│ ├── session.py
│ └── ticket.py
├── .gitignore
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── schemas.py
└── requirements.txt
```

- **main.py:** Entry point for the FastAPI application, where the routers are included.
- **database.py:** Script to initialize the database.
- **dependencies.py:** Defines reusable dependencies, such as the database session.
- **models.py:** Defines the SQLAlchemy data models (database tables).
- **schemas.py:** Defines the Pydantic schemas for input and output data validation.
- **routers/:** Contains the files that define the API endpoints, grouped by resource.
