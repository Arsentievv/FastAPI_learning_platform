from sqlalchemy import Table, Column, String, Integer, TIMESTAMP, ForeignKey
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

students_products = Table(
    "students_products",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
)


class Product(Base):
    __tablename__ =  "product",
    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(length=50), nullable=False)
    description = Column("description", String(length=2000), nullable=True)
    creation_date = Column("creation_date", TIMESTAMP, default=datetime.utcnow())
    owner_id = Column("owner_id", Integer, ForeignKey("user.id"))
    students = relationship("Student", secondary="students_products", back_populates="products")

