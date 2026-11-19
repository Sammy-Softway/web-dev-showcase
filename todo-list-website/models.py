from datetime import datetime, timezone, date
from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Text, DateTime, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Todo(db.Model):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 nullable=False,
                                                 default=lambda:
                                                 datetime.now(timezone.utc))
    due_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    def __repr__(self):
        return f"<Todo {self.id}: {self.title}>"
