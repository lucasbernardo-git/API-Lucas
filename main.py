import uvicorn
from fastapi import FastAPI
from database import engine, Base
import app.models
from app.routers.empresa import router as empresa_router
from app.routers.book import router as book_router
from app.routers.user import router as user_router
from app.routers.borrow import router as borrow_router
app = FastAPI()

#Limpa o banco e gera um novo

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

@app.get("/")
def check_api():
    return "Api Online!"

app.include_router(empresa_router)
app.include_router(book_router)
app.include_router(user_router)
app.include_router(borrow_router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)