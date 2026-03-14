from fastapi import FastAPI
from dotenv import load_dotenv

from database import engine
from models import book_model
from routes import book_route
from middleware.logger_middleware import LoggerMiddleware

# Load environment variables
load_dotenv()

# Create database tables directly using SQLAlchemy
book_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book CRUD API", 
    description="A simple Laravel-like FastAPI application",
    version="1.0.0"
)

# Add Middleware into FastAPI app pipeline
app.add_middleware(LoggerMiddleware)

# Include Routes
app.include_router(book_route.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book CRUD API! Visit /docs for the Swagger UI."}

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get the port from .env, default to 8000 if not found
    port = int(os.getenv("APP_PORT", 8000))
    
    # Run the uvicorn server programmatically
    # uvicorn.run("main:app", host="0.0.0.1", port=port, reload=True)
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)
