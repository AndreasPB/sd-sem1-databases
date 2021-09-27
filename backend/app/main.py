from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models

from db.database import engine
from routers import root, person


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:5000",
    "http://localhost:3000",
    "http://localhost",
    "https://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(root.router)
app.include_router(person.router)
