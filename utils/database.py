from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ.get('DATABASE_CREATE'), pool_size=60, max_overflow=-1,pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def cleanup(db):
    """
    Esto es para limpiar el objeto session (base de datos) de sqlalchemy.
    """
    db.close()
    engine.dispose()

def init_db():
    
    Base.metadata.create_all(bind=engine)


