"""
Solicite a matrícula e senha do funcionário para ter acesso aos seus dados.
Solicite o salário base do funcionário.
Pergunte se o funcionário deseja receber vale transporte (s/n).
Pergunte o valor do vale refeição fornecido pela empresa.
Calcule os descontos e acréscimos na folha de pagamento do funcionário.
Mostre o salário líquido do funcionário após os descontos e acréscimos.

Considere que o funcionário possui apenas um dependente.
Considere que o salário base é o salário antes de quaisquer descontos ou acréscimos.
Considere que o salário base, o vale refeição e o plano de saúde são informados em reais (R$).

Alunos: Maria luiza e Henrique Santos 
"""

import os

os.system("cls || clear")

salario_base = float(int(input("Digite o seu salário base: ")))

def desconto_inss (total):
    lista_salario = []
    if lista_salario <= 1100:
        desconto = total * 0.075
        total_final = total - desconto 
        lista_salario.append(total) 
        return total_final
    
    elif lista_salario >= 1100.01 and lista_salario <= 2203.48:
        desconto = total * 0.09
        total_final = total - desconto
        lista_salario.append(total) 
        return total_final
    
    elif lista_salario >= 2203.49 and lista_salario <= 3305.22:
        desconto = total * 0.012
        total_final = total - desconto
        lista_salario.append(total) 
        return total_final
    
    elif lista_salario >= 3305.22 and lista_salario <= 6433.57:
        desconto = total * 0.014
        total_final = total - desconto
        lista_salario.append(total) 
        return total_final
    





