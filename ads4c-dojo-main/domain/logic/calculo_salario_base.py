from domain.logic import calculo_inss, calcula_dedutor

def calculo_salario_base(salario, qtd_dependentes):
    desconto_dep = calcula_dedutor(qtd_dependentes)
    valor_desconto = calculo_inss(salario)
    salario_base = salario - desconto_dep - valor_desconto
    return round(salario_base,2)
