from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str

lista = [
        Usuario(id=1, nome='nome1', senha='senha1'),
        Usuario(id=2, nome='nome2', senha='senha2'),
        Usuario(id=3, nome='nome3', senha='senha3'),
        Usuario(id=4, nome='nome4', senha='senha4')
]

@app.post('/usuario')
def main(usuario: Usuario):
    lista.append(usuario)       
    return (f'O Usuario {usuario} foi cadsatrado com sucesso.')

@app.get('/usuarioListar')
def main():       
    return lista