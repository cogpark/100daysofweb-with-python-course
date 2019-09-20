from db import db_folder

import sqlalchemy
import sqlalchemy.orm

__engine = None
__factory = None


def global_init(db_name: str):
    global __engine, __factory

    if __factory:
        return

    conn_str = 'sqlite:///' + db_folder.get_full_path(db_name)
    __engine = sqlalchemy.create_engine(conn_str, echo=True)
    __factory = sqlalchemy.orm.sessionmaker(bind=__engine)


def create_tables() -> sqlalchemy.orm.Session:
    if not __engine:
        raise Exception("You have not called global_init()")

    # noinspection PyUnresolvedReferences
    import data.__all_models
    from data.sqlalchemybase import SqlAlchemyBase
    SqlAlchemyBase.metadata.create_all(__engine)


def create_session() -> sqlalchemy.orm:
    session = __factory()
    session.expire_on_commit = False
    return session
