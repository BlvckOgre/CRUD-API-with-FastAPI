from fastapi import FastAPI
from .database import Base, engine
from .routes import router

app = FastAPI()

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router)
