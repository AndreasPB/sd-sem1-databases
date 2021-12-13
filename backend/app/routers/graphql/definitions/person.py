from typing import TYPE_CHECKING
import strawberry
from strawberry.lazy_type import LazyType

from app.db.models import Person as PersonModel

if TYPE_CHECKING:
    from .country import Country
    from .media import Media


@strawberry.type
class Person:
    id: int
    name: str
    job: str
    country_id: int
    
    instance = strawberry.Private[PersonModel]
    
    @strawberry.field
    def country(self) -> LazyType["Country", ".country"]:
        from .country import Country
        return Country.from_instance(self.instance.country)

    @strawberry.field
    def media(self) -> LazyType["Media", ".media"]:
        from .media import Media
        return Media.from_instance(self.instance.media)

    @classmethod
    def from_instance(cls, instance: PersonModel):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
            job=instance.job,
            country_id=instance.country_id
        )
