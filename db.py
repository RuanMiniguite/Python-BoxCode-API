from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

NOME_BANCO = "boxcode"

engine = create_engine(f"sqlite:///./{NOME_BANCO}.sqlite", echo=True)
Base = declarative_base()

# Declaracao das classes
class Fisica(Base):

    __tablename__ = "fisica"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(String, nullable=False)
    instEnsino = Column(String, nullable=False)
    cpf = Column(Integer, nullable=False)
    #projeto_id = Column(Integer, ForeignKey("projeto.id"))

    def __repr__(self):
        return f"Fisica {self.nome}"

class Juridica(Base):
    __tablename__ = "juridica"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    segmento = Column(String, nullable=False)
    cnpj = Column(String, nullable=False)
    #projeto_id = Column(Integer, ForeignKey("projeto.id"))

    def __repr__(self) -> str:
        return f"Juridica {self.nome}"

class Projeto(Base):
    __tablename__ = "projeto"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    segmento = Column(String, nullable=False)

# fim da declaracao

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()