from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True)
    first_name = Column("first_name", String(length=50), nullable=True)
    last_name = Column("last_name", String(length=50), nullable=True)
    username = Column("username", String(length=50), nullable=False)
    email = Column("email", String(length=20), unique=True, nullable=False)
    password = Column("password", String(length=30), nullable=False)
    creation_date = Column("creation_date", TIMESTAMP, default=datetime.utcnow())
    products = relationship("Product", secondary="students_products", back_populates="students")
