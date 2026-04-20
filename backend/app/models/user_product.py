from sqlalchemy import Column, Integer, ForeignKey, Date
from app.db.database import Base

class UserProduct(Base):
    __tablename__ = "user_products"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    purchase_date = Column(Date)
    warranty_expiry = Column(Date)