from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from app.db.base import Base
from datetime import datetime

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    