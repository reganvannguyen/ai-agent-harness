from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from datetime import datetime

class RunSummary(Base):
    __tablename__ = "run_summaries"
    id: Mapped[int] = mapped_column(primary_key= True)
    agent_run_id: Mapped[int] = mapped_column(ForeignKey("agent_runs.id"))
    summary: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), server_default= func.now())
    
