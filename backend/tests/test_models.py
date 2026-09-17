from app import models  # noqa: F401
from app.db.base import Base


EXPECTED_TABLES = {
    "conversations",
    "messages",
    "agent_runs",
    "run_steps",
    "run_summaries",
}


def test_all_models_are_registered_on_base_metadata():
    assert set(Base.metadata.tables) == EXPECTED_TABLES
