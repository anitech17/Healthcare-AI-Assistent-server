from fastapi import FastAPI
from app.api.routes import health
from app.db.session import engine
from app.db.models import Base

app = FastAPI(
    title="Healthcare AI Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Healthcare AI Backend Running"}