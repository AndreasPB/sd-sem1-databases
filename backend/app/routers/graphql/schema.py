from typing import List

import strawberry
from strawberry.extensions import Extension
from strawberry.fastapi.router import GraphQLRouter
from app.db.models import get_users

from app.db.database import SessionLocal

from app.routers.graphql.definitions.user import User


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context["db"] = SessionLocal()

    def on_request_end(self):
        self.execution_context.context["db"].close()


@strawberry.type
class Query:
    @strawberry.field
    def some_users(self, info, limit: int = 250) -> List[User]:
        db = info.context["db"]
        users = get_users(db, limit=limit)
        return [User.from_instance(user) for user in users]


schema = strawberry.Schema(Query, extensions=[SQLAlchemySession])
graphql_schema = GraphQLRouter(schema)
