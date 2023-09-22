from pydantic import BaseModel
import datetime


class ProductCreate(BaseModel):
    id: int
    title: str
    description: str
    creation_date: datetime
    owner_id: int
