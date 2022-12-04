from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ.get('DATABASE_CREATE'), pool_size=60, max_overflow=-1)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    print('llegue hasta la inicializacion de la bdd')
    Base.metadata.create_all(bind=engine)


