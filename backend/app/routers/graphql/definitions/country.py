import strawberry

from typing import TYPE_CHECKING
from strawberry.lazy_type import LazyType

from app.db.models import Country as CountryModel

if TYPE_CHECKING:
    from .user import User
    # from .person import Person


@strawberry.type
class Country:
    id: int
    name: str
    country_code: str

    instance = strawberry.Private[CountryModel]

    # @strawberry.field
    # def people(self) -> LazyType["Person", ".person"]:
    #     from .person import Person
    #     return Person.from_instance(self.instance.person)

    @strawberry.field
    def users(self) -> LazyType["User", ".user"]:
        from .user import User
        return User.from_instance(self.instance.users)

    @classmethod
    def from_instance(cls, instance: CountryModel):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
            country_code=instance.country_code,
        )
