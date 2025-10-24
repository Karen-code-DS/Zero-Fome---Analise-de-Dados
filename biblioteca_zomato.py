## IMPORTANDO BIBLIOTECAS
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go



### INSERINDO COLUNAS
# Dicionário completo de mapeamento Country Code -> Country Name
mapeamento_paises = {
    1: 'India',
    14: 'Australia', 
    30: 'Brazil',
    37: 'Canada',
    94: 'Indonesia',
    148: 'New Zealand',
    162: 'Philippines',
    166: 'Qatar',
    184: 'Singapore',
    189: 'South Africa',
    191: 'Sri Lanka',
    208: 'Turkey',
    214: 'United Arab Emirates',
    215: 'United Kingdom',
    216: 'United States',
    356: 'India'  # Código alternativo para India
}

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]

## LIMPEZA DE DADOS
def limpeza_dados(df):
    
    # Remover NaN
    df_limpo = df_limpo.dropna()
    
    # Remover os espaços 
    df_limpo = df_limpo.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    
    # Converter object para string
    coluna = ['Restaurant Name', 'City', 'Address', 'Locality', 'Locality Verbose', 'Cuisines', 'Currency', 'Rating color', 'Rating text']
    colunas_existentes = [col for col in coluna if col in df_limpo.columns]
    
    for coluna in colunas_existentes:
        if coluna in df_limpo.columns:
            df_limpo[coluna] = df_limpo[coluna].astype(str).str.strip()
         
    return df_limpo

def creat_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return 'expensive'
    else:
        return 'gourmet'

def carregar_dados (caminho_arquivo='zomato.csv'):
    df = pd.read_csv('zomato.csv')
    df['Country'] = df['Country'].map(mapeamento_paises)
    return df