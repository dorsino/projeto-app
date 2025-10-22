import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Análise de Anúncios de Vendas de Carros Usados')
car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.checkbox('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

explot_chart = st.checkbox('Criar gráfico de dispersão') # criar um botão
if explot_chart: # se o botão for clicado
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)