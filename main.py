import uvicorn
from fastapi import fastapi

app = FastAPI()

@app.get("/")
def check_api():
    return "Api Online!"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)