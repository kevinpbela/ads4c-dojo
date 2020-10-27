from domain.logic import calculo_salario_base

def calculo_valor_a_pagar(salario, qtd_dependentes):
    primeira_faixa = 1903,98
    a = 4664.68
    b = 3751.06
    c = 2826.66
    d = 1903.99
    base = calculo_salario_base(salario, qtd_dependentes)
    if base > a:
        valor_a_pagar = (base - primeira_faixa) * 0.275
    elif base > b: 
        valor_a_pagar = (base - primeira_faixa) * 0.225
    elif base > c:
        valor_a_pagar = (base - primeira_faixa) * 0.15
    elif base > d:
        valor_a_pagar = (base - primeira_faixa) * 0.075
    else:
        valor_a_pagar = 0
    return round(valor_a_pagar, 2)
