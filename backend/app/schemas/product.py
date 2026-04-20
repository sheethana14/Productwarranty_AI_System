from pydantic import BaseModel
from datetime import date

class ProductCreate(BaseModel):
    name: str
    description: str
    category: str
    warranty_months: int
    vendor_id: int

class RegisterProduct(BaseModel):
    product_id: int
    purchase_date: date