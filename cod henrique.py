def calcular_inss(salario_base):
    if salario_base <= 1100:
        return salario_base * 0.075
    elif salario_base <= 2203.48:
        return salario_base * 0.09
    elif salario_base <= 3305.22:
        return salario_base * 0.12
    elif salario_base <= 6433.57:
        return salario_base * 0.14
    else:
        return 854.36

def calacular_irrf(salario_base):
    if salario_base <= 2259.20:
        return salario_base + print("isento: ")
    elif salario_base >= 2259.21 or salario_base <= 2826.65:
        return salario_base * 0.075
    elif salario_base >= 2826.65 or salario_base <= 3751.06:
        return salario_base * 0.15
    elif salario_base >= 3751.06 or salario_base <= 4664.68:
        return salario_base *0.22
    elif salario_base >= 4664.68:
        return salario_base * 0.00275
        