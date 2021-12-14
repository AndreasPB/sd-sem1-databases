from app.mongo_schemas import Genre, Media, Provider, Person, Country, User


list_of_countries = [
    Country(name="Denmark", country_code="DK"),
    Country(name="Sweden", country_code="SE"),
    Country(name="Norway", country_code="NO"),
    Country(name="Finland", country_code="FI"),
    Country(name="Netherlands", country_code="NL"),
    Country(name="United States of America", country_code="US"),
    Country(name="United Kingdom", country_code="UK"),
    Country(name="Canada", country_code="CA"),
    Country(name="Australia", country_code="AU"),
]


list_of_people = [
    Person(name="Ian McKellen", job="actor", country=list_of_countries[6]),
    Person(name="Daniel Radcliffe", job="actor", country=list_of_countries[6]),
    Person(name="Emma Watson", job="actor", country=list_of_countries[6]),
    Person(name="Matt LeBlanc", job="actor", country=list_of_countries[5]),
    Person(name="Michael Caine", job="actor", country=list_of_countries[5]),
    Person(name="Morgan Freeman", job="actor", country=list_of_countries[5]),
    Person(name="Nikolaj Coster-Waldau", job="actor", country=list_of_countries[0]),
    Person(name="Lars von Trier", job="actor", country=list_of_countries[0]),
    Person(name="Mads Mikkelsen", job="actor", country=list_of_countries[0]),
]

list_of_genres = [
    Genre(name="Action"),
    Genre(name="Adventure"),
    Genre(name="Comedy"),
    Genre(name="Drama"),
    Genre(name="Fantasy"),
    Genre(name="Horror"),
    Genre(name="Mystery"),
    Genre(name="Romance"),
    Genre(name="Sci-Fi"),
    Genre(name="Thriller"),
]

list_of_providers = [
    Provider(
        name="Netflix",
        url="https://www.netflix.com/",
        poster_path="/static/images/logo_net.png",
    ),
    Provider(
        name="Amazon Prime Video",
        url="https://www.amazon.com/",
        poster_path="/static/images/logo_prime.png",
    ),
    Provider(
        name="HBO",
        url="https://www.hbo.com/",
        poster_path="/static/images/logo_hbo.png",
    ),
    Provider(
        name="Hulu",
        url="https://www.hulu.com/",
        poster_path="/static/images/logo_hulu.png",
    ),
    Provider(
        name="Disney+",
        url="https://www.disneyplus.com/",
        poster_path="/static/images/logo_disney.png",
    ),
    Provider(
        name="Vudu",
        url="https://www.vudu.com/",
        poster_path="/static/images/logo_vudu.png",
    ),
    Provider(
        name="HBO Go",
        url="https://www.hbogo.com/",
        poster_path="/static/images/logo_hbogo.png",
    ),
    Provider(
        name="Amazon Video",
        url="https://www.amazon.com/",
        poster_path="/static/images/logo_amazon.png",
    ),
    Provider(
        name="Google Play Movies",
        url="https://www.google.com/",
        poster_path="/static/images/logo_google.png",
    ),
    Provider(
        name="YouTube Premium",
        url="https://www.youtube.com/",
        poster_path="/static/images/logo_youtube.png",
    ),
]


list_of_media = [
    Media(
        name="Lord of the Rings",
        media_type="movie",
        people=[list_of_people[0], list_of_people[1]],
        genres=[list_of_genres[0], list_of_genres[1], list_of_genres[2]],
        providers=[
            list_of_providers[0],
            list_of_providers[1],
        ],
    ),
    Media(
        name="The Hobbit",
        media_type="movie",
        people=[list_of_people[0], list_of_people[1]],
        genres=[list_of_genres[0], list_of_genres[3]],
        providers=[list_of_providers[2], list_of_providers[3]],
    ),
    Media(
        name="The Matrix",
        media_type="movie",
        people=[list_of_people[2], list_of_people[3]],
        genres=[list_of_genres[4], list_of_genres[5]],
        providers=[list_of_providers[3], list_of_providers[4]],
    ),
    Media(
        name="The Godfather",
        media_type="movie",
        people=[list_of_people[4], list_of_people[5]],
        genres=[list_of_genres[6], list_of_genres[7]],
        providers=[list_of_providers[5], list_of_providers[6]],
    ),
    Media(
        name="The Shawshank Redemption",
        media_type="movie",
        people=[list_of_people[0], list_of_people[3]],
        genres=[list_of_genres[4]],
        providers=[list_of_providers[0]],
    ),
    Media(
        name="Friends",
        media_type="tv",
        people=[list_of_people[4], list_of_people[6]],
        genres=[list_of_genres[1], list_of_genres[2]],
        providers=[list_of_providers[6], list_of_providers[7]],
    ),
    Media(
        name="The Simpsons",
        media_type="tv",
        people=[list_of_people[2], list_of_people[4]],
        genress=[list_of_genres[3]],
        providers=[list_of_providers[7]],
    ),
    Media(
        name="The Big Bang Theory",
        media_type="tv",
        people=[list_of_people[2], list_of_people[3]],
        genres=[list_of_genres[1], list_of_genres[2]],
        providers=[list_of_providers[7], list_of_providers[1]],
    ),
    Media(
        name="The Office",
        media_type="tv",
        people=[list_of_people[2], list_of_people[5]],
        genres=[list_of_genres[1], list_of_genres[2]],
        providers=[list_of_providers[2], list_of_providers[3]],
    ),
]

list_of_users = [
    User(
        username="andreaspb",
        email="andreaspb@example.com",
        country=list_of_countries[0],
        favorites=[list_of_media[0], list_of_media[1]],
    ),
    User(
        username="frederikv",
        email="frederikv@example.com",
        country=list_of_countries[0],
        favorites=[list_of_media[2], list_of_media[3]],
    ),
    User(
        username="jensv",
        email="jensv@example.com",
        country=list_of_countries[0],
        favorites=[list_of_media[4], list_of_media[5]],
    ),
    User(
        username="johnh",
        email="johnh@example.com",
        country=list_of_countries[5],
    ),
    User(
        username="janej",
        email="janej@example.com",
        country=list_of_countries[5],
        favorites=[list_of_media[6], list_of_media[7]],
    ),
]
