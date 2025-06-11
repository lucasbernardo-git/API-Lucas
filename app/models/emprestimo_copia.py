from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Table, Boolean
from sqlalchemy.orm import relationship
from database import Base


emprestimo_copia = Table(
    "emprestimo_copia",
    Base.metadata,
    Column("emprestimo_id", Integer, ForeignKey("emprestimos.id")),
    Column("copia_id", Integer, ForeignKey("copias_livro.id"))
)
