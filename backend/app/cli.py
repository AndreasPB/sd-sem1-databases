# from typer import Typer, echo
import typer

from db.models import Base

from db.database import engine, SessionLocal
from db.sql import (
    create_stored_procedure,
    exec_stored_procedure,
    create_stored_function,
    exec_stored_function,
)


app = typer.Typer()


@app.command()
def drop_tables():
    Base.metadata.drop_all(bind=engine)
    typer.echo("Dropped all tables")


@app.command()
def create_tables():
    Base.metadata.create_all(bind=engine)
    typer.echo("Created all tables")


@app.command()
def make_stored_procedure(table: str):
    db = SessionLocal()
    typer.echo(f"Creating stored procedure for table: {table}")
    typer.echo(create_stored_procedure(db=db, table=table))


@app.command()
def run_stored_procedure(table: str):
    db = SessionLocal()
    typer.echo(f"Excecuting stored procedure for table: {table}")
    exec_stored_procedure(db=db, table=table)


@app.command()
def make_stored_function(table: str):
    db = SessionLocal()
    typer.echo("Creating stored function for table:", table)
    create_stored_function(db=db, table=table)


@app.command()
def run_stored_function(table: str):
    db = SessionLocal()
    typer.echo("Excecuting stored function for table:", table)
    exec_stored_function(db=db, table=table)


if __name__ == "__main__":
    app()