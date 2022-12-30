from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def root():
    return {'mensagem': 'Home'}

@app.get("/cadastro")
def cadastro():
    return {'mensagem': 'Cadastro'}

@app.get("/login")
def login():
    return {'mensagem': 'Login'}    