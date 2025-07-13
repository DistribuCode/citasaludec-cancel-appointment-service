from fastapi import FastAPI
from prometheus_client import start_http_server
from src.routes import appointment_routes
from src.config.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

start_http_server(8001)

app.include_router(appointment_routes.router)
