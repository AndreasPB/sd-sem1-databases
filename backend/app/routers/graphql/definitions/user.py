from typing import TYPE_CHECKING
import strawberry
from strawberry.lazy_type import LazyType

from app.db.models import User as UserModel

if TYPE_CHECKING:
    from .country import Country
    # from .media import Media


@strawberry.type
class User:
    id: int
    username: str
    email: str
    country_id: int

    instance: strawberry.Private[UserModel]

    @strawberry.field
    def country(self) -> LazyType["Country", ".country"]:
        from .country import Country
        return Country.from_instance(self.instance.country)

    # def media(self) -> Media:
    #     return Media.from_instance(self.instance.media)

    @classmethod
    def from_instance(cls, instance: UserModel):
        return cls(
            instance=instance,
            id=instance.id,
            username=instance.username,
            email=instance.email,
            country_id=instance.country_id,
        )
