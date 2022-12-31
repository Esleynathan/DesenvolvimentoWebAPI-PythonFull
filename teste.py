from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

usuarios = [(1, 'esley','minhasenha'),(2, 'camila', 'senhacamila'),(3, 'sarah', 'senhasarah')]

@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i
    
    return "Não exisgte esse usuario"