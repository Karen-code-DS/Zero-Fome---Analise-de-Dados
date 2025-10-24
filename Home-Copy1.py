## LENDO DOCUMENTO
import pandas as pd
import numpy as np

df = pd.read_csv('zomato.csv')
df_limpo = df.copy()

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

df_limpo['Country'] = df_limpo['Country Code'].map(mapeamento_paises)

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


# ________________________________________________GERAL________________________________________________

#1. Quantos restaurantes únicos estão registrados?
n_restaurante = df_limpo['Restaurant Name'].unique()
rest_unico = len(n_restaurante)
print(f'Número de restaurantes únicos: {rest_unico}')

# 2. Quantos países únicos estão registrados?
n_pais = df_limpo['Country'].unique()
pais_unico = len(n_pais)
print(f'Número de países únicos: {pais_unico}')

# 3. Quantas cidades únicas estão registradas?
n_cidade = df_limpo['City'].unique()
cidade_unico = len(n_cidade)
print(f'Número de cidades únicas: {cidade_unico}')

# 4. Qual o total de avaliações feitas?
n_aval = df_limpo['Aggregate rating'].count()
print(f'Total de avaliações: {n_aval}')


# 5. Qual o total de tipos de culinária registrados?
t_culinaria = df_limpo['Cuisines'].count()
print(f'Total de tipos de culinária: {t_culinaria}')



# ________________________________________________PAÍS________________________________________________

# 1. Qual o nome do país que possui mais cidades registradas?
cidade_pais = df_limpo.groupby('Country')['City'].nunique().sort_values(ascending=False).head(1)
cidade_pais


# 2. Qual o nome do país que possui mais restaurantes registrados?
restaurante_pais = df_limpo.groupby('Country')['Restaurant ID'].nunique().sort_values(ascending=False).head(1)
restaurante_pais


# 3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a registrados?
preco = df_limpo.groupby('Country')['Price range'].nunique().sort_values(ascending=False).head(1)
preco


# 4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
pais_cozinha = df_limpo.groupby('Country')['Cuisines'].count().sort_values(ascending=False).head(1)
pais_cozinha


# 5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
avaliacao_pais = df_limpo.groupby('Country')['Aggregate rating'].count().sort_values(ascending=False).head(1)
avaliacao_pais


# 6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
restaurante_entrega = df_limpo[df_limpo['Has Online delivery'] == 1]
pais_entrega = restaurante_entrega.groupby("Country").size().sort_values(ascending=False).head(1)
pais_entrega


# 7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
restaurante_reserva = df_limpo[df_limpo['Has Table booking'] == 1]
pais_reserva = restaurante_reserva.groupby("Country").size().sort_values(ascending=False).head(1)
pais_reserva


# 8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
pais_maior_avaliacao = df_limpo.groupby("Country")['Votes'].mean().sort_values(ascending=False).head(1).round(2)
pais_maior_avaliacao


# 9. Qual o nome do país que possui, na média, a maior nota média registrada?
pais_nota_maior = df_limpo.groupby("Country")['Aggregate rating'].mean().sort_values(ascending=False).head(1).round(2)
pais_nota_maior


# 10. Qual o nome do país que possui, na média, a menor nota média registrada?
pais_nota_menor = df_limpo.groupby("Country")['Aggregate rating'].mean().sort_values(ascending=True).head(1).round(2)
pais_nota_menor


# 11. Qual a média de preço de um prato para dois por país?
pais_preco2 = df_limpo.groupby("Country")['Average Cost for two'].mean().sort_values(ascending=False).head(1).round(2)
pais_preco2



# ________________________________________________CIDADE________________________________________________

# 1. Qual o nome da cidade que possui mais restaurantes registrados?
cidade_restaurante = df_limpo.groupby('City')['Restaurant ID'].nunique().sort_values(ascending=False).head(1)
cidade_restaurante


# 2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
cdd_avaliacao = df_limpo.groupby('City')['Aggregate rating'].mean().round(2).head(1)
melhor_avaliacao = cdd_avaliacao[cdd_avaliacao > 4]
melhor_avaliacao


# 3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
cdd_avaliacao_pior = df_limpo.groupby('City')['Aggregate rating'].mean().round(2)
pior_avaliacao = cdd_avaliacao_pior[cdd_avaliacao_pior < 2.5]
pior_avaliacao


# 4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
cdd_avaliacao_p2 = df_limpo.groupby('City')['Average Cost for two'].mean().sort_values(ascending=False).round(2).head(1)
cdd_avaliacao_p2


# 5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
tipos_culinaria_cdd = df_limpo.groupby('City')['Cuisines'].nunique().sort_values(ascending=False).head(1)
tipos_culinaria_cdd


# 6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
rest_c_reserva = df_limpo[df_limpo['Has Table booking'] == 1]
cdd_reserva = rest_c_reserva.groupby('City')['Has Table booking'].count().sort_values(ascending=False).head(1)
cdd_reserva


# 7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
rest_entrega = df_limpo[df_limpo['Is delivering now'] == 1]
cidade_entrega = rest_entrega['City'].value_counts().head(1)
cidade_entrega


# 8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
rest_online = df_limpo[df_limpo['Has Online delivery'] == 1]
rest_online_cdd = rest_online['City'].value_counts().head(1)
rest_online_cdd


# ________________________________________________RESTAURANTES________________________________________________

#1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
rest_qnt_avaliacao = df_limpo.groupby('Restaurant Name')['Aggregate rating'].count().sort_values(ascending=False).head(1)
rest_qnt_avaliacao


# 2. Qual o nome do restaurante com a maior nota média?
rest_melhor = df_limpo.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
rest_melhor


# 3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
prato_caro = df_limpo.groupby('Restaurant Name')['Average Cost for two'].max().sort_values(ascending=False).head(1)
prato_caro


# 4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
comida_br = df_limpo[df_limpo['Cuisines'] == "Brazilian"]
comida_br_ruim = comida_br.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=True).head(1)
comida_br_ruim


# 5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
comida_br_doBR = df_limpo[(df_limpo['Cuisines'] == "Brazilian") & (df_limpo['Country'] == "Brazil")]
comida_br_melhor = comida_br_doBR.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
comida_br_melhor


# 6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
# Pedidos online
pedido_online = df_limpo[df_limpo['Has Online delivery'] == 1]
restaurante_online = pedido_online['Aggregate rating'].mean()

# Pedidos não online
pedido_n_online = df_limpo[df_limpo['Has Online delivery'] == 0]
restaurante_n_online = pedido_n_online['Aggregate rating'].mean()

# Comparaçao
print(f"A média de restaurantes que aceitam pedidos online: {restaurante_online:.2f}")
print(f'A média de restaurantes que não aceitam pedidos online: {restaurante_n_online:.2f}')

if restaurante_online > restaurante_n_online:
    print('SIM, restaurantes com entrega online têm melhores avaliações em média')
else:
    print('NÃO, restaurantes com entrega online NÃO têm melhores avaliações em média')


# 7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
rest_reserva = df_limpo[df_limpo['Has Table booking'] == 1]
rest_reserva_mean = rest_reserva['Average Cost for two'].mean()
print(f'A média de preço de pratos para dois COM reserva é: {rest_reserva_mean:.2f}')

rest_s_reserva = df_limpo[df_limpo['Has Table booking'] == 0]
rest_s_reserva_mean = rest_s_reserva['Average Cost for two'].mean()
print(f'A média de preço de pratos para dois SEM reserva é: {rest_reserva_mean:.2f}')

print("Restaurantes COM reserva:", len(rest_reserva))
print("Restaurantes SEM reserva:", len(rest_s_reserva))

if rest_reserva_mean > rest_s_reserva_mean:
    print('SIM, os restaurantes que tem reserva tem pratos para dois mais caros')
elif rest_reserva_mean < rest_s_reserva_mean: 
    print('NÃO, os restaurantes que tem reserva não tem pratos para dois mais caros')
else:
    print('EMPATE, os preços médios são IGUAIS')


# 8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
comida_japan_eua = df_limpo[(df_limpo['Cuisines'] == "Japanese") & (df_limpo['Country'] == "United States")]
comida_japan_eua_mean = comida_japan_eua['Average Cost for two'].mean()
print(f'Média de preços de restaurantes de comida japonesa nos EUA: {comida_japan_eua_mean:.2f}')

churras_eua = df_limpo[(df_limpo['Cuisines'] == "BBQ") & (df_limpo['Country'] == "United States")]
churras_eua_mean = churras_eua['Average Cost for two'].mean()
print(f'Média de preços de churrascaria nos EUA: {churras_eua_mean:.2f}')

if comida_japan_eua_mean == churras_eua_mean:
    print('Não há diiferença de valor para pratos que servem duas pessoas')
elif comida_japan_eua_mean > churras_eua_mean:
    print('Comida japonesa tem preço maior que churrascaria em pratos que servem duas pessoas')
else:
    print('A churrascaria tem preço maior que a comida japonesa para pratos que servem duas pessoas')



# ________________________________________________TIPOS_DE_cULINÁRIA________________________________________________

# 1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
comida_italian = df_limpo[df_limpo['Cuisines'] == 'Italian']
comida_italian_melhor = comida_italian.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
comida_italian_melhor


# 2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
comida_italian_pior = comida_italian.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=True).head(1)
comida_italian_pior


# 3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
comida_eua = df_limpo[df_limpo['Cuisines'] == 'American']
comida_eua_melhor = comida_eua.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
comida_eua_melhor


# 4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
comida_eua_pior = comida_eua.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=True).head(1)
comida_eua_pior


# 5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
comida_arabic = df_limpo[df_limpo['Cuisines'] == 'Asian']
comida_arabic_melhor = comida_arabic.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
comida_arabic_melhor


# 6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
comida_arabic_pior = comida_arabic.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=True).head(1)
comida_arabic_pior


# 7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
melhor_japan = comida_japan.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
melhor_japan


# 8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
pior_japan = comida_japan.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=True).head(1)
pior_japan


# 9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
comida_caseira = df_limpo[df_limpo['Cuisines'] == 'Home-made']
melhor_caseira = comida_caseira.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
melhor_caseira


# 10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
comida_caseira = df_limpo[df_limpo['Cuisines'] == 'Home-made']
pior_caseira = comida_caseira.groupby('Restaurant Name')['Aggregate rating'].mean().sort_values(ascending=True).head(1)
pior_caseira


# 11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
melhor_culinaria_p2 = df_limpo.groupby('Cuisines')['Average Cost for two'].mean().sort_values(ascending=False).head(1)
melhor_culinaria_p2


# 12. Qual o tipo de culinária que possui a maior nota média?
melhor_culinaria = df_limpo.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False).head(1)
melhor_culinaria


# 13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?
rest_online_entrega = df_limpo[(df_limpo['Has Online delivery'] == 1) & (df_limpo['Has Table booking'] == 1)]
culinaria_online_rest = rest_online_entrega['Cuisines'].value_counts().head(1)
culinaria_online_rest

