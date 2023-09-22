from pydantic import BaseModel
import datetime
import email


class UserCreate(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: email
    password: str
    creation_date: datetime
