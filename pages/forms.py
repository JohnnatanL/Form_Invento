import streamlit as st
import datetime

st.set_page_config(page_title="Invento Logo Existo🐑", page_icon="🐑")#, layout="wide")
st.header("Queremos te conhecer!")

# Formulário
with st.form(key='my_form'):
    #Elementos do formulário
    cola, colb = st.columns(2)
    with cola: nome = st.text_input("Qual o seu nome")
    with colb: data_nasc = st.date_input("Qual a Data do seu nascimento?", value=datetime.date.today(), min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
    colc, cold = st.columns(2)
    with colc: produto_fav = st.selectbox("Qual seu produto favorito aqui na Invento?", ['Azulejo', 'Camisa', 'Quadro', 'Chaveiro'])

    #Botão Enviar
    submit_button = st.form_submit_button(label='Enviar')

# Ao clicar em enviar
if submit_button:
    st.write(f'Nome: {nome}')
    st.write(f'Data de Nascimento: {data_nasc}')
    st.write(f'Produto Favorito: {produto_fav}')