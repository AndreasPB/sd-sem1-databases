from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.models import Base

from app.db.database import engine
from app.routers import root, person, user, country, genre, provider, media
from app.routers.graphql import index
from app.routers.graphql.schema import graphql_schema


Base.metadata.create_all(bind=engine)


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

app.include_router(index.graphql_app, prefix="/v1/graphql", tags=["graphql"])
app.include_router(graphql_schema, prefix="/v2/graphql", tags=["graphql"])
app.include_router(root.router)
app.include_router(person.router)
app.include_router(user.router)
app.include_router(country.router)
app.include_router(genre.router)
app.include_router(provider.router)
app.include_router(media.router)
