from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Lesson(Base):
    __tablename__ = "lesson",
    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(length=250), nullable=False)
    video_link = Column("video_link", String(length=500), nullable=False)
    description = Column("description", String(length=2000), nullable=False)
    product_id = Column("product_id", Integer, ForeignKey("product.id"))
    creation_date = Column("creation_date", TIMESTAMP, default=datetime.utcnow())


class LessonStatus(Base):
    __tablename__ = "lesson_result",
    id = Column("id", Integer, primary_key=True)
    student = Column("student", Integer, ForeignKey("user.id"))
    lesson = Column("lesson", Integer, ForeignKey("lesson.id"))
    start_watching_date = Column("start_watching_date", TIMESTAMP, nullable=False)
    end_watching_date = Column("end_watching_date", TIMESTAMP, nullable=True)
    watched_seconds = Column("watched_seconds", Integer, default=0, nullable=True)
    updated_at = Column("updated_at", TIMESTAMP, nullable=True)
    status = Column("status", String, default="not_viewed", nullable=False)