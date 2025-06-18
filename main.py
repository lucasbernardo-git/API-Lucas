import uvicorn
from fastapi import FastAPI
from database import engine, Base
#from app.routers import empresa
from app.routers.empresa import router as empresa_router
from app.models import cargo, cliente, copias_livro, empresa, emprestimo, enderecos, funcionario, livro, pessoas

app = FastAPI()

# Include the empresa router
app.include_router(empresa.router)

#Limpa o banco e gera um novo

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@app.get("/")
def check_api():
    return "Api Online!"

app.include_router(empresa_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)