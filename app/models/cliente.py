from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"), unique=True)
    data_cadastro = Column(Date, nullable=True)

    pessoa = relationship("Pessoa", back_populates="cliente")
    emprestimos = relationship("Emprestimo", back_populates="cliente")
