from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import as_declarative


@as_declarative
class Base(object):
    updated_at = Column(Integer)


class Foo(Base):
    __tablename__ = "foo"
    id: int = Column(Integer(), primary_key=True)
    name: str = Column(String)


f1 = Foo()

val: int = f1.id

p: str = f1.name

Foo.id.property

f2 = Foo(name="some name", updated_at=5)
