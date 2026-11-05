
import streamlit as st

from calculos import (
    calcular_area,
    calcular_preco,
    aplicar_desconto,
    aplicar_valor_minimo
)


# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Calculadora de Orçamentos",
    page_icon="🧾",
    layout="centered"
)


# FUNÇÃO PARA FORMATAR MOEDA
def moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return f"R$ {texto}"


# CABEÇALHO
st.title("🧾 Calculadora de Orçamentos")
st.caption("Sistema de precificação desenvolvido em Python")
st.divider()


# BARRA LATERAL
with st.sidebar:
    st.header("⚙️ Regras de preço")
    st.write("Desconto: 5% para pedidos acima de R$ 200,00.")
    st.write("Pedido mínimo: R$ 30,00.")
    st.info("Projeto educacional — Semana 1 de GenAI")


# FORMULÁRIO
with st.container(border=True):
    st.subheader("Dados do orçamento")

    with st.form("formulario_orcamento"):

        col1, col2 = st.columns(2)

        with col1:
            largura = st.number_input(
                "Largura (cm)",
                min_value=0.01,
                value=263.0
            )

        with col2:
            altura = st.number_input(
                "Altura (cm)",
                min_value=0.01,
                value=23.0
            )

        col3, col4 = st.columns(2)

        with col3:
            preco_m2 = st.number_input(
                "Preço por m² (R$)",
                min_value=0.01,
                value=56.0
            )

        with col4:
            quantidade = st.number_input(
                "Quantidade",
                min_value=1,
                value=3,
                step=1
            )

        calcular = st.form_submit_button(
            "Calcular orçamento",
            type="primary"
        )


# RESULTADOS
if calcular:

    area = calcular_area(largura, altura)

    valor_unitario = calcular_preco(
        area, preco_m2, 1
    )

    subtotal = calcular_preco(
        area, preco_m2, quantidade
    )

    valor_com_desconto = aplicar_desconto(subtotal)
    desconto = subtotal - valor_com_desconto

    valor_final = aplicar_valor_minimo(
        valor_com_desconto
    )

    st.divider()
    st.subheader("📊 Resultado do orçamento")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Área por unidade",
            f"{area:.4f} m²"
        )

    with col2:
        st.metric(
            "Preço unitário",
            moeda(valor_unitario)
        )

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "Subtotal",
            moeda(subtotal)
        )

    with col4:
        st.metric(
            "Desconto",
            moeda(desconto)
        )

    with st.container(border=True):
        st.subheader("Valor final")
        st.metric(
            "Total do pedido",
            moeda(valor_final)
        )

    if valor_final > valor_com_desconto:
        st.info("Valor mínimo de R$ 30,00 aplicado.")

    st.success("Orçamento calculado com sucesso!")
