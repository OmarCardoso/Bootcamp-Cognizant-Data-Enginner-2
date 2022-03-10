from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


# Comando necessário para criar o db e fazer manipulação
engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Criar tabela Devs
class Devs(Base):
    __tablename__='devs'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(40))


# Criar tabela Atividades relacionada com Pessoas
class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    devs_id = Column(Integer, ForeignKey('devs.id'))
    devs = relationship("Devs")

class Devs_Skills(Base):
    devs_id = Column(Integer, ForeignKey('devs.id'))
    skills_id = Column(Integer, ForeignKey('skills.id'))