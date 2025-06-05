#faz a ligação do banco de dados com o projeto

from sqlalchemy import create_engine

#Traz o ORM

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

#link para ligar com o banco de dados, passa o usuário e senha, localização e qual é o schema

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/projeto_lucas_api"

engine = create_engine(DATABASE_URL)

#É o responsavel pelas sessões do ORM

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

der get_db():  #Representa a chamada do banco de dados
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()