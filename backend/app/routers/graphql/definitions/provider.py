import strawberry

from app.db.models import Provider as ProviderModel

# from .person import Person
# from .media import Media


@strawberry.type
class Provider:
    id: int
    name: str
    media_type: str
    
    instance = strawberry.Private[ProviderModel]
    
    # @strawberry.field
    # def person(self):
    #     return Person.from_instance(self.instance.person)

    # @strawberry.field
    # def media(self):
    #     return Media.from_instance(self.instance.media)
    
    @classmethod
    def from_instance(cls, instance: ProviderModel):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
            media_type=instance.media_type,
        )
