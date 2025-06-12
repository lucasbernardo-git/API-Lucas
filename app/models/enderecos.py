from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Endereco(Base):
    __tablename__ = "enderecos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rua = Column(String(100), nullable=True)
    numero = Column(String(100), nullable=True)
    cep = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=True)
    estado = Column(String(100), nullable=True)
    pessoa_id = Column(Integer, ForeignKey("pessoas.id"))

    pessoa = relationship("Pessoa", back_populates="endereco")