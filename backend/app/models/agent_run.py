from sqlalchemy import DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from datetime import datetime


class AgentRun(Base):
    __tablename__ = "agent_runs"
    id: Mapped[int] = mapped_column(primary_key= True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    trigger_message_id: Mapped[int] = mapped_column(ForeignKey("messages.id"))
    status: Mapped[str]
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), server_default= func.now())
    completed_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), server_default= func.now())

