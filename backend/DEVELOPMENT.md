# Local development

## Start the PostgreSQL container

Run this from the repository root (`ai-agent-harness`):

```bash
docker compose up -d postgres
docker compose ps
```

The database is available at `localhost:5432`.

## Open the PostgreSQL shell

```bash
docker exec -it agent-harness-db psql -U postgres -d agent_harness
```

To use the values in `backend/.env` when starting Compose instead:

```bash
docker compose --env-file backend/.env up -d postgres
```

To stop the container while keeping the database volume:

```bash
docker compose down
```

`docker compose down -v` also deletes the database volume and its data.

## Start the FastAPI backend

In a second terminal:

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload
```

First-time setup, if `backend/.venv` does not exist:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The backend runs at <http://127.0.0.1:8000>. Interactive API docs are at
<http://127.0.0.1:8000/docs>.

Stop the backend with `Ctrl+C`.

## Run the test

```bash
python -m pytest tests -q
```

## Startup order

1. Start PostgreSQL from the repository root.
2. Start the backend from `backend/`.

## Turn everything off

1. In the terminal running FastAPI, press `Ctrl+C`.
2. From the repository root, stop the PostgreSQL container:

```bash
docker compose down
```

This stops and removes the container but keeps the database volume and its
data. Do not use `docker compose down -v` unless you intentionally want to
delete the database data.

## Database connection note

The local backend connection in `backend/app/db/database.py` uses the Compose
database on `localhost:5432` with the `psycopg` driver. Make sure its password
matches the password used when the persistent PostgreSQL volume was created.

The backend does not yet load `backend/.env` automatically, so keep the
connection value in the code and the database credentials aligned.
