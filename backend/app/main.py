from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter

from app.db.models import Base

from app.db.database import engine
from app.routers import root, person, user, country, genre, provider, media
from app.routers.graphql import index


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

# @strawberry.type
# class Flemming:
#     id: int
#     name: str
#     age: int
# 
# cool_list_of_flemmings = [
#     Flemming(id=1, name="Flemming", age=11),
#     Flemming(id=2, name="Flemming", age=22),
#     Flemming(id=3, name="Flemming", age=33),
#     Flemming(id=4, name="Flemming", age=44),
#     Flemming(id=5, name="Flemming", age=55),
# ]
# 
# @strawberry.type
# class Query:
#     @strawberry.field
#     def get(self, id: int) -> Flemming:
#         return next(filter(lambda x: x.id == id, cool_list_of_flemmings))
# 
# schema = strawberry.Schema(Query)
# graphql_app = GraphQLRouter(schema)

app.include_router(index.graphql_app, prefix="/graphql", tags=["graphql"])
app.include_router(root.router)
app.include_router(person.router)
app.include_router(user.router)
app.include_router(country.router)
app.include_router(genre.router)
app.include_router(provider.router)
app.include_router(media.router)
