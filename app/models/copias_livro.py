from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class CopiaLivro(Base):
    __tablename__ = "copias_livro"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    livro_id = Column(Integer, ForeignKey("livros.id"))
    numero_copia = Column(String(100), nullable=True)
    disponivel = Column(Boolean, default=True)
    estado_conservacao = Column(String(100), nullable=False)

    livro = relationship("Livro", back_populates="copias")
    emprestimos = relationship("Emprestimo", secondary="emprestimo_copia", back_populates="copias")

