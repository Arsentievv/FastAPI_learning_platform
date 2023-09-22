from enum import Enum

from pydantic import BaseModel, Field
import datetime


class LessonCreate(BaseModel):
    id: int
    title: str
    video_link: str
    description: str
    product_id: int
    creation_date: datetime


class StatusType(Enum):
    viewed = "viewed"
    not_viewed = "not_viewed"


class LessonStatusCreate(BaseModel):
    id: int
    student: int
    lesson: int
    start_watching_date: datetime
    end_watching_date: datetime
    watched_seconds: int = Field(ge=0)
    updated_at: datetime
    status: StatusType
