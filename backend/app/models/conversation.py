from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, DateTime

from datetime import datetime

from app.db.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    