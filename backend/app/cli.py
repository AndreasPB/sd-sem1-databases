# from typer import Typer, echo
import typer

from db.models import Base
from db.database import engine


app = typer.Typer()


@app.command()
def drop_tables():
    Base.metadata.drop_all(bind=engine)
    typer.echo("Dropped all tables")


@app.command()
def create_tables():
    Base.metadata.create_all(bind=engine)
    typer.echo("Created all tables")


if __name__ == "__main__":
    app()
