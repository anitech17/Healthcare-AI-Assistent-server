from fastapi import FastAPI
from app.api.routes import health
from app.db.session import engine
from app.db.models import Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Healthcare AI Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(health.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Healthcare AI Backend Running"}