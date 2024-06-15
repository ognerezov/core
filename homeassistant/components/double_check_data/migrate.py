from .db_tables import Base


def init_schema():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_schema()