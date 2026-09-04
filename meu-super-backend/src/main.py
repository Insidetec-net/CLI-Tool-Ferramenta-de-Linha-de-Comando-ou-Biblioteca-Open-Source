from fastapi import FastAPI

app = FastAPI(title="meu-super-backend", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to meu-super-backend API!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}