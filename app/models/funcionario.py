from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"), unique=True)
    salario = Column(Float, nullable=False)
    carga_horaria = Column(String, nullable=True)
    cargo_id = Column(Integer, ForeignKey("cargos.id"))
    data_contratacao = Column(Date, nullable=False)

    pessoa = relationship("Pessoa", back_populates="funcionario")
    cargo = relationship("Cargo", back_populates="funcionarios")

