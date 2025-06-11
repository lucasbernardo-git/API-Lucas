from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Livro(Base):
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    escritor = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    editora = Column(String, nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)

    copias = relationship("CopiaLivro", back_populates="livro")
