#!python
import sqlalchemy as sa
from sqlalchemy.ext import compiler
from sqlalchemy.schema import DDLElement
from sqlalchemy.sql import table

from db import models
from db.database import engine


class CreateView(DDLElement):
    def __init__(self, name, selectable):
        self.name = name
        self.selectable = selectable


class DropView(DDLElement):
    def __init__(self, name):
        self.name = name


@compiler.compiles(CreateView)
def compile(element, compiler, **kw):
    return "CREATE VIEW %s AS %s" % (
        element.name,
        compiler.sql_compiler.process(element.selectable, literal_binds=True),
    )


@compiler.compiles(DropView)
def compile(element, compiler, **kw):
    return "DROP VIEW %s" % (element.name)


def view(name, metadata, selectable):
    t = table(name)

    for c in selectable.c:
        c._make_proxy(t)

    sa.event.listen(metadata, "after_create", CreateView(name, selectable))
    sa.event.listen(metadata, "before_drop", DropView(name))
    return t


def initialize_views():
    metadata = sa.MetaData()

    user_view = view(
        "user_view",
        metadata,
        sa.select(
            [
                models.User.id.label("id"),
                models.User.username.label("username"),
                models.Media.name.label("media_name"),
                models.Media.genre.label("genre")
            ]
        )
        .select_from(models.User.join(models.Media))
    )

    assert user_view.primary_key == [user_view.c.id]

    # illustrate ORM usage
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import Session

    Base = declarative_base(metadata=metadata)

    class UserView(Base):
        __table__ = user_view

        def __repr__(self) -> str:
            return super().__repr__()

    s = Session(engine)
    print(s.query(UserView).all())
    s.close()
