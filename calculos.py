
# CÁLCULO DA ÁREA
def calcular_area(largura, altura):
    return (largura * altura) / 10000


# CÁLCULO DO PREÇO
def calcular_preco(area, preco_m2, quantidade):
    return area * preco_m2 * quantidade


# DESCONTO DE 5% ACIMA DE R$ 200
def aplicar_desconto(valor_total):
    if valor_total > 200:
        desconto = valor_total * 0.05
        return valor_total - desconto
    else:
        return valor_total


# VALOR MÍNIMO DE R$ 30
def aplicar_valor_minimo(valor_total):
    if valor_total < 30:
        return 30.00
    else:
        return valor_total
