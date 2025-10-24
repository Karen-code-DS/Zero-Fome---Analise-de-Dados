# ==============================================================================================================================================================
## IMPORTANDO BIBLIOTECAS
from PIL import Image
import streamlit as st
import os
# ==============================================================================================================================================================



# Configuração dapágina
st.set_page_config(
    page_title='Dashboard - Fome Zero',
    page_icon='📊',
    layout='wide'
)

    # Abrir imagem
image=Image.open('fomezero.png')
st.sidebar.image(image, width=200)

# ------------------ criar barra lateral -------------------------------



# ------------------ pagina inicial (Home) -------------------------------
st.title('📊 Dashboard')
st.markdown("""___""")

st.markdown(
    """
    A Fome Zero é o marketplace líder que conecta clientes aos melhores restaurantes. Nosso core business é simplificar a experiência gastronômica, centralizando o encontro e as negociações entre quem deseja comer bem e quem serve comida de qualidade.
    
    Aqui, os restaurantes parceiros disponibilizam seu cadastro completo na plataforma, incluindo:
    
    - Localização: Endereço e área de entrega.
    - Culinária: Tipo de comida e especialidades.
    - Serviços: Possui reservas? Faz entregas?
    - Avaliações: Notas e feedbacks verídicos dos clientes.
    
    Este dashboard é seu centro de controle para gerenciar e ampliar o sucesso do seu restaurante na nossa praça digital.
    """
)