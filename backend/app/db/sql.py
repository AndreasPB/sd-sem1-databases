from sqlalchemy.orm import Session
from sqlalchemy import text


def create_stored_procedure(db: Session, table: str):
    #query = f"CREATE PROCEDURE selectall{table}() LANGUAGE SQL AS $$ SELECT * FROM MEDIA $$; CALL selectall{table}()"

    query = text('SELECT * FROM media')
    return db.execute(query)


def exec_stored_procedure(db: Session, table: str):
    return db.execute(f"CALL selectall{table}();")


def create_stored_function(db: Session):
    query = "CREATE FUNCTION getmovies() \
            RETURN VARCHAR(20) \
            DECLARE \
            GO;"

    return db.execute(query)


def exec_stored_function(db: Session):
    return db.execute("EXEC SelectAll")


def populate_database():
    pass
