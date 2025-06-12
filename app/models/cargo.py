from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Cargo(Base):
    __tablename__ = "cargos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(18), nullable=False)
    descricao = Column(String(100), nullable=True)

    funcionarios = relationship("Funcionario", back_populates="cargo")
