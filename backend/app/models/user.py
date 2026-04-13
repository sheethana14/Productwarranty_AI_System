from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Primary_key=True, index=True)
    # Username = Column(String(255), unique=True, index=True)
    Email= Column(String(255),Unique=True, index=True)
    Password = Column(String(255))
