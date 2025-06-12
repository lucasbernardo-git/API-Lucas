from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Pessoa(Base):
    __tablename__ = "pessoas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome_completo = Column(String(100), nullable=False)
    cpf = Column(String(100), unique=True, index=True, nullable=False)
    telefone = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    data_nascimento = Column(Date, nullable=False)

    endereco = relationship("Endereco", uselist=False, back_populates="pessoa")
    cliente = relationship("Cliente", uselist=False, back_populates="pessoa")
    funcionario = relationship("Funcionario", uselist=False, back_populates="pessoa")