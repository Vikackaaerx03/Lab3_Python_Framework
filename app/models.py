from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, nullable=False)
    customer_name = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    order_date = Column(Date, nullable=False)