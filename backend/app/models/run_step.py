from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB

class RunStep(Base):
    __tablename__ = "run_steps"
    id: Mapped[int] = mapped_column(primary_key= True)
    agen_run_id: Mapped[int] = mapped_column(ForeignKey("agent_runs.id"))
    step_order: Mapped[int]
    step_type: Mapped[str]
    pay_load: Mapped[dict] = mapped_column(JSONB)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), server_default= func.now())
    
