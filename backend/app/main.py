from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.db.database import Base, engine

app = FastAPI()
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)