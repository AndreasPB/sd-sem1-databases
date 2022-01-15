from datetime import datetime
from re import L
from py2neo import Graph
from py2neo.ogm import (
    Model,
    Property,
    Related,
    RelatedTo,
    RelatedFrom,
    Repository,
    Label,
)


graph = Graph("bolt://graph_db:7687")
repo = Repository("bolt://graph_db:7687")


class Media(Model):
    name = Property()
    movie = Label("Movie")
    tv = Label("TV")
    provider = RelatedTo("Provider", "PROVIDED_BY")
    genre = RelatedTo("Genre", "HAS_GENRE")


class User(Model):
    username = Property()
    email = Property()
    country = RelatedTo("Country", "IS_FROM")
    media = RelatedTo("Media", "LIKES")


class Person(Model):
    name = Property()
    actor = Label("Actor")
    director = Label("Director")
    producer = Label("Producer")

    country = RelatedTo("Country", "IS_FROM")
    actor_of = Related("Media", "ACTOR_OF")
    director_of = Related("Media", "DIRECTOR_OF")
    producer_of = Related("Media", "PRODUCER_OF")


class Genre(Model):
    name = Property()
    media = RelatedTo("Media")


class Provider(Model):
    name = Property()
    poster_path = Property()
    media = RelatedTo("Media")


class Country(Model):
    name = Property()
    country_code = Property()
    people = RelatedFrom("Person")
    users = RelatedFrom("User")


lotr_fellowship = Media(
    name="The Lord of the Rings: The Fellowship of the Ring",
    movie=True,
)

lotr_two_towers = Media(
    name="The Lord of the Rings: The Two Towers",
    movie=True,
)

lotr_return_of_the_king = Media(
    name="The Lord of the Rings: The Return of the King",
    movie=True,
)

green_street_hooligans = Media(
    name="Green Street Hooligans",
    movie=True,
)


genres = {
    "Action": Genre(name="Action"),
    "Adventure": Genre(name="Adventure"),
    "Comedy": Genre(name="Comedy"),
    "Crime": Genre(name="Crime"),
    "Drama": Genre(name="Drama"),
    "Fantasy": Genre(name="Fantasy"),
    "History": Genre(name="History"),
    "Horror": Genre(name="Horror"),
    "Mystery": Genre(name="Mystery"),
    "Romance": Genre(name="Romance"),
    "Science Fiction": Genre(name="Science Fiction"),
    "Thriller": Genre(name="Thriller"),
}


countries = {
    "US": Country(name="United States", country_code="US"),
    "GB": Country(name="United Kingdom", country_code="GB"),
    "FR": Country(name="France", country_code="FR"),
    "DE": Country(name="Germany", country_code="DE"),
    "IT": Country(name="Italy", country_code="IT"),
    "ES": Country(name="Spain", country_code="ES"),
    "NL": Country(name="Netherlands", country_code="NL"),
    "BE": Country(name="Belgium", country_code="BE"),
    "DK": Country(name="Denmark", country_code="DK"),
    "NO": Country(name="Norway", country_code="NO"),
    "NZ": Country(name="New Zealand", country_code="NZ"),
    "AU": Country(name="Australia", country_code="AU"),
    "CA": Country(name="Canada", country_code="CA"),
    "JP": Country(name="Japan", country_code="JP"),
    "CN": Country(name="China", country_code="CN"),
    "IN": Country(name="India", country_code="IN"),
}

providers = {
    "Netflix": Provider(name="Netflix", poster_path="/poster/netflix.jpg"),
    "HBO Max": Provider(name="HBO Max", poster_path="/poster/hbo-max.jpg"),
    "Amazon Prime Video": Provider(
        name="Amazon Prime Video", poster_path="/poster/amazon-prime-video.jpg"
    ),
}

user1 = User(
    username="user1",
    email="user1@mail.com",
)

user2 = User(
    username="user2",
    email="user2@mail.com",
)

user3 = User(
    username="user3",
    email="user3@mail.com",
)

users = [
    user1,
    user2,
    user3,
]

peter_jackson = Person(name="Peter Jackson", director=True)
elijah_wood = Person(name="Elijah Wood", actor=True, producer=True)
ian_mckellen = Person(name="Ian McKellen", actor=True)
viggo_mortensen = Person(name="Viggo Mortensen", actor=True)
orlando_bloom = Person(name="Orlando Bloom", actor=True)

lotr_cast = [
    peter_jackson,
    elijah_wood,
    ian_mckellen,
    viggo_mortensen,
    orlando_bloom,
]


def populate_graph():
    graph.delete_all()

    # Countries
    for country in countries.values():
        repo.save(country)

    # Genres
    for genre in genres.values():
        repo.save(genre)

    # Fellowship of the Ring
    repo.save(lotr_fellowship)
    lotr_fellowship.genre.add(genres["Action"])
    lotr_fellowship.genre.add(genres["Adventure"])
    lotr_fellowship.genre.add(genres["Fantasy"])
    lotr_fellowship.provider.add(providers["HBO Max"])
    [person.actor_of.add(lotr_fellowship) for person in lotr_cast[1:]]
    [person.director_of.add(lotr_fellowship) for person in lotr_cast[:1]]

    [repo.save(lotr) for lotr in lotr_cast]
    repo.save(lotr_fellowship)

    # Two Towers
    repo.save(lotr_two_towers)
    lotr_two_towers.genre.add(genres["Action"])
    lotr_two_towers.genre.add(genres["Adventure"])
    lotr_two_towers.genre.add(genres["Fantasy"])
    lotr_two_towers.provider.add(providers["HBO Max"])
    [person.actor_of.add(lotr_two_towers) for person in lotr_cast[1:]]
    [person.director_of.add(lotr_two_towers) for person in lotr_cast[:1]]

    [repo.save(lotr) for lotr in lotr_cast]
    repo.save(lotr_two_towers)

    # Return of the King
    repo.save(lotr_return_of_the_king)
    lotr_return_of_the_king.genre.add(genres["Action"])
    lotr_return_of_the_king.genre.add(genres["Adventure"])
    lotr_return_of_the_king.genre.add(genres["Fantasy"])
    lotr_return_of_the_king.provider.add(providers["HBO Max"])
    [person.actor_of.add(lotr_return_of_the_king) for person in lotr_cast[1:]]
    [person.director_of.add(lotr_return_of_the_king) for person in lotr_cast[:1]]

    [repo.save(lotr) for lotr in lotr_cast]
    repo.save(lotr_return_of_the_king)

    # Green Street Hooligans
    repo.save(green_street_hooligans)
    green_street_hooligans.genre.add(genres["Crime"])
    green_street_hooligans.genre.add(genres["Drama"])
    green_street_hooligans.provider.add(providers["Netflix"])

    elijah_wood.actor_of.add(green_street_hooligans)

    repo.save(green_street_hooligans)

    # People
    peter_jackson.country.add(countries["NZ"])
    elijah_wood.country.add(countries["US"])
    ian_mckellen.country.add(countries["GB"])
    viggo_mortensen.country.add(countries["DK"])
    orlando_bloom.country.add(countries["US"])

    [repo.save(person) for person in lotr_cast]

    # Users
    [repo.save(user) for user in users]

    user1.media.add(lotr_fellowship, properties={"timestamp": datetime.now()})
    user1.media.add(lotr_two_towers, properties={"timestamp": datetime.now()})
    user1.country.add(countries["US"])

    user2.media.add(lotr_return_of_the_king, properties={"timestamp": datetime.now()})
    user2.media.add(green_street_hooligans, properties={"timestamp": datetime.now()})
    user2.country.add(countries["IN"])

    user3.media.add(lotr_fellowship, properties={"timestamp": datetime.now()})
    user3.media.add(lotr_return_of_the_king, properties={"timestamp": datetime.now()})
    user3.country.add(countries["CA"])

    [repo.save(user) for user in users]
