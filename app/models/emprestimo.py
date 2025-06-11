from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Emprestimo(Base):
    __tablename__ = "emprestimos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    data_retirada = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=False)
    valor_multa = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente", back_populates="emprestimos")
    copias = relationship("CopiaLivro", secondary="emprestimo_copia", back_populates="emprestimos")

