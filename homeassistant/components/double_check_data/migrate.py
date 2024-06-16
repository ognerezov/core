from .db_tables import Base


def init_schema(engine):
    Base.metadata.create_all(engine)
