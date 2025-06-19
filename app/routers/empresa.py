from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from app.models.empresa import Empresa as EmpresaModel

router = APIRouter(prefix="/empresa", tags=["empresas"])

# Pydantic Models
class CompanyBase(BaseModel):
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None
    numero_contato: Optional[str] = None
    email_contato: Optional[str] = None
    website: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    cnpj: Optional[str] = None # All fields optional for update
    razao_social: Optional[str] = None
    # Other fields are already optional in CompanyBase

class CompanyResponse(CompanyBase):
    id: int

    class Config:
        orm_mode = True

# CRUD Endpoints
@router.post("/", response_model=CompanyResponse, status_code=status.HTTP_201_CREATED)
def criar_empresa(empresa: CompanyCreate, db: Session = Depends(get_db)):
    db_empresa = EmpresaModel(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@router.get("/", response_model=List[CompanyResponse])
def listar_empresas(db: Session = Depends(get_db)):
    empresas = db.query(EmpresaModel).all()
    return empresas

@router.get("/{cnpj}", response_model=CompanyResponse)
def obter_empresa(cnpj: str, db: Session = Depends(get_db)):
    empresa = db.query(EmpresaModel).filter(EmpresaModel.cnpj == cnpj).first()
    if empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Empresa não encontrada")
    return empresa

@router.put("/{id}", response_model=CompanyResponse)
def atualizar_empresa(id: int, empresa_update: CompanyUpdate, db: Session = Depends(get_db)):
    db_empresa = db.query(EmpresaModel).filter(EmpresaModel.id == id).first()
    if db_empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Empresa não encontrada")

    update_data = empresa_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_empresa, key, value)
    
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_empresa(id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(EmpresaModel).filter(EmpresaModel.id == id).first()
    if db_empresa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Empresa não encontrada")

    db.delete(db_empresa)
    db.commit()
    return None
