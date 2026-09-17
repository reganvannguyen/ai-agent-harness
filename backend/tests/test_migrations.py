import os
import subprocess
import sys
import uuid
from pathlib import Path

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import make_url


BACKEND_DIR = Path(__file__).resolve().parents[1]
ALEMBIC_CONFIG = BACKEND_DIR / "alembic.ini"
EXPECTED_TABLES = {
    "conversations",
    "messages",
    "agent_runs",
    "run_steps",
    "run_summaries",
}


def _quote_identifier(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def test_migrations_create_expected_tables():
    load_dotenv(BACKEND_DIR / ".env")
    database_url_value = os.getenv("DATABASE_URL")
    if not database_url_value:
        pytest.fail("DATABASE_URL must be set to run the migration smoke test")

    database_url = make_url(database_url_value)
    test_database_name = f"agent_harness_test_{uuid.uuid4().hex}"
    admin_engine = create_engine(database_url.set(database="postgres"), isolation_level="AUTOCOMMIT")
    test_engine = None

    try:
        with admin_engine.connect() as connection:
            connection.exec_driver_sql(
                f"CREATE DATABASE {_quote_identifier(test_database_name)}"
            )

        test_url = database_url.set(database=test_database_name)
        migration_environment = os.environ.copy()
        migration_environment["DATABASE_URL"] = test_url.render_as_string(
            hide_password=False
        )

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "alembic",
                "-c",
                str(ALEMBIC_CONFIG),
                "upgrade",
                "head",
            ],
            cwd=BACKEND_DIR,
            env=migration_environment,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"Alembic migration failed.\nstdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )

        test_engine = create_engine(test_url)
        tables = set(inspect(test_engine).get_table_names())

        assert EXPECTED_TABLES <= tables
        assert "alembic_version" in tables
    finally:
        if test_engine is not None:
            test_engine.dispose()
        with admin_engine.connect() as connection:
            connection.exec_driver_sql(
                f"DROP DATABASE IF EXISTS {_quote_identifier(test_database_name)}"
            )
        admin_engine.dispose()
