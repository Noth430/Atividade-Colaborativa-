import os 
from dataclasses import dataclass

@dataclass
class Funcionario:
    maticula: str
    senha: int
    salario_b: float

def desconto_inss(resposta):
    lista_salario = []

    if resposta <= 1.100:
        
        lista_salario.append(resposta)
        

