import strawberry

from app.db.models import Media as MediaModel

from .person import Person


@strawberry.type
class Media:
    id: int
    name: str
    media_type: str
    
    instance = strawberry.Private[MediaModel]
    
    @strawberry.field
    def person(self) -> Person:
        return Person.from_instance(self.instance.person)

    @classmethod
    def from_instance(cls, instance: MediaModel):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
            media_type=instance.media_type,
        )