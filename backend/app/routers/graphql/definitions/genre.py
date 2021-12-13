import strawberry

from app.db.models import Genre as GenreModel

from .media import Media


@strawberry.type
class Genre:
    id: int
    name: str

    instance: strawberry.Private[GenreModel]

    @strawberry.field
    def media(self) -> Media:
        return Media.from_instance(self.instance.media)

    @classmethod
    def from_instance(cls, instance: GenreModel):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
        )
