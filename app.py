import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo os dados
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho
st.header('Análise de anúncios de veículos')

# Caixa de seleção para o histograma
build_histogram = st.checkbox('Criar histograma')

if build_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de veículos')

    fig = px.histogram(
        car_data,
        x='odometer'
    )

    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de veículos')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price'
    )

    st.plotly_chart(fig, use_container_width=True)