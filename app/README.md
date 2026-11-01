# Site Intelligence API

A FastAPI application for retrieving and creating monitoring sites.
Built to demonstrate REST endpoints, Pydantic validation, error
handling, and modular Python project structure.

## Features

- List sites and filter by status.
- Retrieve a site by ID.
- Create a site with a user-supplied ID.
- Validate site names, statuses, and depths.
- Return 404 for missing sites and 409 for duplicate IDs.
- Explore endpoints through Swagger UI.

## Project structure

```text
app/
├── __init__.py
├── main.py
├── schemas.py
├── sample_data.py
└── routers/
    ├── __init__.py
    └── sites.py
requirements.txt
README.md
.gitignore
```

## Run locally

Requires Python 3.10 or newer.

From the project root, run these commands in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --reload-dir app
```

Open http://127.0.0.1:8000/docs for interactive API documentation.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/sites` | List sites |
| GET | `/sites?status=Active` | Filter sites by status |
| GET | `/sites/{site_id}` | Retrieve one site |
| POST | `/sites/{site_id}` | Create a site |

Example POST request body:

```json
{
  "site_name": "Monitoring Site C",
  "status": "Active",
  "depth": 95.5
}
```

Use an ID that does not already exist in the POST URL.

## Current limitations

Data is stored in an in-memory dictionary. Changes are lost when
the application restarts. There is no database or authentication.