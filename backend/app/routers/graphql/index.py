import strawberry
from strawberry.fastapi import GraphQLRouter
from app.schemas import PersonType, UserType, CountryType

denmark = CountryType(id=1, name="Denmark", country_code="DK")
sweden = CountryType(id=2, name="Sweden", country_code="SE")
norway = CountryType(id=3, name="Norway", country_code="NO")
spain = CountryType(id=4, name="Spain", country_code="ES")

person_list = [
    PersonType(id=1, name="John Doe", job="Actor", country=denmark),
    PersonType(id=2, name="Jane Doe", job="Actor", country=sweden),
    PersonType(id=3, name="Jack Smith", job="Director", country=norway),
    PersonType(id=4, name="Jasmine Smith", job="Director", country=spain),
]

user_list = [
    UserType(id=1, username="john", email="john@mail.com", country=denmark),
    UserType(id=2, username="jane", email="jane@mail.com", country=sweden),
    UserType(id=3, username="jack", email="jack@mail.com", country=norway),
    UserType(id=4, username="jasmine", email="jasmine@mail.com", country=spain),
]


@strawberry.type
class Query:
    @strawberry.field
    def get_country(self, id: int) -> CountryType:
        return next(filter(lambda x: x.id == id, [denmark, sweden, norway, spain]))
    
    @strawberry.field
    def get_countries(self) -> list[CountryType]:
        return [denmark, sweden, norway, spain]

    @strawberry.field
    def get_person(self, id: int) -> PersonType:
        return next(filter(lambda x: x.id == id, person_list))

    @strawberry.field
    def get_people(self) -> list[PersonType]:
        return person_list

    @strawberry.field
    def get_user(self, id: int) -> UserType:
        return next(filter(lambda x: x.id == id, user_list))

    @strawberry.field
    def get_users(self) -> list[UserType]:
        return user_list

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
