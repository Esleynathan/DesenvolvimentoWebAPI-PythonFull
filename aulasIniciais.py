from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    x = 10
    for i in range(10):
        x += 1
        
    return {'mensagem': 'Home', 'valor': x}

@app.get("/cadastro")
def cadastro():
    return {'mensagem': 'Cadastro'}

@app.get("/login")
def login():
    return {'mensagem': 'Login'}    