from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

#Creates database engine
engine = create_engine('sqlite:///todo.db',echo=False,poolclass=StaticPool,connect_args={'check_same_thread': False})

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)