# Finance Tracking System API

## Overview
This project is a Python-powered backend for a finance tracking system, designed to allow users to manage and analyze their financial records. Built with FastAPI, SQLAlchemy, and SQLite, the architecture emphasizes clean code, logical file organization, and maintainability. 

It provides REST API endpoints for financial records management, analytics, and role-based access control, ensuring robust data handling and proper validation.

## Features
* **Financial Records Management**: Full CRUD operations for income and expenses, including fields for amount, type, category, date, and notes.
* **Summary & Analytics**: Generates meaningful financial summaries, including total income, total expenses, current balance, and category-wise breakdowns.
* **Role-Based Access Control**: Implements basic user handling with three distinct roles: Viewer, Analyst, and Admin.
* **Validation & Error Handling:** Utilizes Pydantic for strict input validation, ensuring predictable application behavior and providing useful error responses with appropriate HTTP status codes.

## Tech Stack
* Framework: FastAPI
* ORM: SQLAlchemy
* Database: SQLite 
* Server: Uvicorn

## Detailed Project Structure
The project is logically organized to enforce a strict separation of concerns, ensuring that business rules, summaries, and access behavior are clearly implemented.
```
finance_backend/
├── app/
│   ├── main.py          # FastAPI application instance and router registration
│   ├── database.py      # SQLAlchemy engine and SQLite session management
│   ├── models.py        # Database schema definitions (SQLAlchemy)
│   ├── schemas.py       # Data validation and response models (Pydantic)
│   ├── crud.py          # Core business logic and database queries
│   ├── dependencies.py  # Auth, role-checking, and DB session injection
│   └── routers/
│       ├── records.py   # API endpoints for financial records
│       ├── summary.py   # API endpoints for analytics
│       └── users.py     # API endpoints for user management
├── requirements.txt     # Dependency handling
└── README.md            # Project documentation
```

## Future Maintenance and Scalability
To ensure this application remains maintainable and scalable as business requirements grow, the architecture follows several key engineering practices:

* **Modularity and Extensibility:** Because the routing, business logic (CRUD), and data models are separated, new features (like CSV import/export or pagination) can be added to specific modules without risking regressions in unrelated components.
* **Database Migrations:** As the data model evolves, maintaining the schema manually will become error-prone. Future iterations should integrate a migration tool like Alembic. This will allow schema changes to be tracked and applied sequentially across different environments.
* **Testing:** While the current interface is designed to be easy to test manually via the Swagger UI, long-term maintenance requires automated testing. Implementing a unit testing suite using Pytest for the CRUD functions and endpoint validation will prevent future code changes from breaking existing features.
* **Authentication Upgrades:** The current role-handling relies on a simplified access model. Because the authorization logic is isolated in dependencies.py, it can be upgraded to robust token-based authentication (e.g., OAuth2 with JWTs) without requiring rewrites of the core endpoints.

## Versioning Strategy
Proper versioning is critical for production readiness and team collaboration.

1. ***API Versioning:*** 
Future API developments should implement URL-based routing versions (e.g., `/api/v1/records/` instead of `/records/`). This allows the development of a v2 API with breaking changes while continuing to support legacy clients on v1.

2. ***Source Control and Git Flow:***
The codebase should be maintained using a standard branching strategy (such as GitFlow or GitHub Flow). Feature branches should be used for new development, ensuring that the main branch always reflects a stable, deployable state.

3. ***Dependency Versioning:***
All packages in requirements.txt must remain pinned to specific versions (e.g., fastapi==0.110.0). When upgrading dependencies, developers should test the application locally to ensure compatibility before updating the requirements file. This guarantees that deployment environments mirror the development environment exactly.

## Setup and Installation Instructions

1. Clone or Download the Repository
Ensure you are in the root directory of the project.

2. Create a Virtual Environment
Isolate your dependencies to maintain a clean environment:   
`python -m venv venv`

3. Activate the Virtual Environment:  
  Windows: `venv\Scripts\activate`  
  macOS/Linux: `source venv/bin/activate`

4. Install Dependencies  
`pip install -r requirements.txt`

5. Run the Application
Start the Uvicorn server from the root directory. The SQLite database will initialize automatically on startup.  
`uvicorn app.main:app --reload`

## How to Test the System
FastAPI automatically generates an interactive backend interface. Once the server is running, navigate to:

http://127.0.0.1:8000/docs

From the Swagger UI, you can test all endpoints, verify input validation by providing invalid data, and evaluate how the system returns meaningful summaries.

-----------

