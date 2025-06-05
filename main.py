import uvicorn
from fastapi import fastapi
from database import engine, Base
from app.routers import empresa
#Limpa o banco e gera um novo

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def check_api():
    return "Api Online!"

app.include_router(empresa.router)