from app.db.base import Base

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, DateTime, func
from datetime import datetime




class Message (Base):
    __tablename__ = "messages"
    
    id: Mapped[int] = mapped_column(primary_key= True)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"))
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone= True), server_default= func.now())
