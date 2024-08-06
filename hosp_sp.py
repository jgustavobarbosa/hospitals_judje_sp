!pip install basedosdados
!pip install unidecode
!pip install folium
!pip install googlemaps
!pip install nltk
!pip install seaborn
!pip install dash
!pip install dash_leaflet
!pip install ast
!pip install dash==2.3.1 dash-leaflet==0.1.17 pandas pyngrok
!pip install pyngrok
!pip install ngrok
!pip install docx
!pip install Document
!pip install python-docx
!pip install geopandas
!pip install descartes
!pip install streamlit
!pip install PyPDF2
!pip install dash
!pip install streamlit-folium


import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium
import googlemaps
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
import pandas as pd
from unidecode import unidecode
from folium import LayerControl, FeatureGroup
from folium.plugins import MarkerCluster
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_leaflet as dl
import ast
import streamlit as st
from collections import defaultdict
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import re
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import plotly.express as px
import time
from collections import defaultdict
from streamlit_folium import st_folium



tjsp = pd.read_csv('/content/drive/MyDrive/pos_doc_usp/analise/tabelas_tjsp_medicamento_cancer_corrected.csv', sep=',', quotechar='"')
print(tjsp.shape)
print(tjsp.info())
#print(tjsp.describe())
tjsp.drop(['hora_coleta'], axis=1, inplace=True)
tjsp.drop(['cd_doc'], axis=1, inplace=True)
tjsp.drop(['pagina'], axis=1, inplace=True)

tjsp.columns

#conversão de um campo para data
tjsp['disponibilizacao'] = pd.to_datetime(tjsp['disponibilizacao'], errors='coerce')

# Exemplo de conversão de um campo para numérico
# df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')
tjsp_amostra = tjsp.head().to_csv('tjsp_amostra.csv', index=False)
tjsp_data = tjsp
tjsp_data.to_csv('/content/drive/MyDrive/pos_doc_usp/analise/tjsp_data.csv', index=False)


# Dados formatados dos hospitais
data = [
    ["HOSPITAL ESTADUAL DE DIADEMA - SERRARIA", "R. JOSÉ BONIFÁCIO, 1.641", "11-4056.9000", "DIADEMA", "HOSPITAL GERAL COM CIRURGIA ONCOLÓGICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL DAS CLÍNICAS LUZIA DE PINHO MELO", "R. MANOEL DE OLIVEIRA, S/N", "11-4699.8951", "MOGI DAS CRUZES", "HOSPITAL GERAL COM CIRURGIA ONCOLÓGICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["Centro Oncológico Mogi das Cruzes S/C. Ltda.", "R. DR. OSCAR MARINHO COUTO, 78", "11-4727.6043", "MOGI DAS CRUZES", "UNCACON COM SERVIÇOS DE RADIOTERAPIA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL ESTADUAL MÁRIO COVAS DE SANTO ANDRÉ", "R. HENRIQUE CALDERAZZO, 321", "11-6829.5000", "SANTO ANDRÉ", "UNACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["CENTRO HOSPITALAR DO MUNICÍPIO DE SANTO ANDRÉ", "AV. JOÃO RAMALHO, 326", "11-4433.0060", "SANTO ANDRÉ", "UNACON", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL ANCHIETA SÃO BERNARDO DO CAMPO / FUNDAÇÃO ABC", "R. SILVA JARDIM , 470", "11-4345.4011", "S. BERNARDO DO CAMPO", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL MUNICIPAL UNIVERSITÁRIO DE SÃO BERNARDO DO CAMPO", "AV. BISPO CESAR D'ACORSO FILHO, 161", "11-4365.1480", "S. BERNARDO DO CAMPO", "HOSPITAL GERAL COM CIRURGIA ONCOLÓGICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL MATERNO-INFANTIL MÁRCIA BRAIDO", "R. LUIZ LOUZA, 48", "11-4228.8000", "SÃO CAETANO DO SUL", "UNACON", "DRS 1 - GRANDE SÃO PAULO"],
    ["CENTRO DE REFERÊNCIA DA SAÚDE DA MULHER", "AV. BRIG. LUÍS ANTÔNIO, 683", "11-3242.3433", "SÃO PAULO", "UNACON", "DRS 1 - GRANDE SÃO PAULO"],
    ["CONJUNTO HOSPITALAR DO MANDAQUI", "R. VOLUNTÁRIOS DA PÁTRIA, 4.301", "11-6959.3611", "SÃO PAULO", "HOSPITAL GERAL COM CIRURGIA ONCOLÓGICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL DE TRANSPLANTES DO ESTADO DE SÃO PAULO E.J. ZERBINI", "AV. BRIG. LUÍS ANTÔNIO, 2651", "11-3284.9111", "SÃO PAULO", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL DE CLÍNICAS DA FACULDADE DE MEDICINA DA USP / FUNDAÇÃO FACULDADE DE MEDICINA", "AV. REBOUÇAS, 381", "11-3083.3931", "SÃO PAULO", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL DO CÂNCER A. C. CAMARGO", "R. PROF. ANTÔNIO PRUDENTE, 211", "11-2189.5000", "SÃO PAULO", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL INFANTIL DARCY VARGAS", "R. DR. SERAPHICO DE ASSIS CARVALHO, 34", "11-3723.3700", "SÃO PAULO", "UNACON EXCLUSIVA DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL HELIÓPOLIS", "R. CONEGO XAVIER, 276", "11-2274.7846", "SÃO PAULO", "UNACON", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL IPIRANGA", "AV. NAZARÉ, 28", "11-6215.6449", "SÃO PAULO", "UNACON", "DRS 1 - GRANDE SÃO PAULO"],
    ["SANTA CASA DE SÃO PAULO", "R. CESÁRIO MOTA JR, 112", "11-3226.7000", "SÃO PAULO", "UNACON COM SERVIÇOS DE HEMATOLOGIA E DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["SOC. PORTUGUESA DE BENEFICÊNCIA-SÃO PAULO", "R. MAESTRO CARDIM, 769", "11-3505.1000", "SÃO PAULO", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["CASA DE SAÚDE SANTA MARCELINA", "R.SANTA MARCELINA, 177", "11-3170.6000", "SÃO PAULO", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL SÃO PAULO / UNIFESP", "R. NAPOLEÃO DE BARROS, 715", "11-5572.1922", "SÃO PAULO", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL GERAL DE VILA NOVA CACHOEIRINHA", "AV. DEP. EMÍLIO CARLOS, 3.000", "11-3859.4822", "SÃO PAULO", "HOSPITAL GERAL COM CIRURGIA ONCOLÓGICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["INSTITUTO BRASILEIRO DE CONTROLE DO CÂNCER - IBCC", "AV. ALCÂNTARA MACHADO, 2.576", "11-3474.4222", "SÃO PAULO", "UNCACON COM SERVIÇOS DE RADIOTERAPIA", "DRS 1 - GRANDE SÃO PAULO"],
    ["INSTITUTO DE CÂNCER DR. ARNALDO VIEIRA DE CARVALHO", "R. DR. CESÁRIO MOTTA JR, 112", "11-3350.7088", "SÃO PAULO", "CACON", "DRS 1 - GRANDE SÃO PAULO"],
    ["INSTITUTO DO CÂNCER DO ESTADO DE SÃO PAULO", "AV. DR. ARNALDO, 251", "11-3893.2000", "SÃO PAULO", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 1 - GRANDE SÃO PAULO"],
    ["HOSPITAL GERAL DE PIRAJUSSARA", "R. IBIRAMA, 1.214", "11-4138.9481", "TABOÃO DA SERRA", "HOSPITAL GERAL COM CIRURGIA ONCOLÓGICA", "DRS 1 - GRANDE SÃO PAULO"],
    ["SANTA CASA DE ARAÇATUBA", "R. FLORIANO PEIXOTO, 896", "18-3607.3000", "ARAÇATUBA", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 2 - ARAÇATUBA"],
    ["SANTA CASA DE MISERICÓRDIA DE ARARAQUARA", "AV. JOSÉ BONIFÁCIO, 794", "16-3303.2999", "ARARAQUARA", "UNACON COM SERVIÇOS DE RADIOTERAPIA E HEMATOLOGIA", "DRS 3 - ARARAQUARA"],
    ["SANTA CASA DE SÃO CARLOS", "R. PAULINO BOTELHO DE ABREU SAMPAIO, 573", "16-3373.2699", "SÃO CARLOS", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 3 - ARARAQUARA"],
    ["HOSPITAL SANTO AMARO", "R. QUINTO BERTOLDI, 40", "13-3389.1515", "GUARUJÁ", "UNACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 4 - BAIXADA SANTISTA"],
    ["SANTA CASA DE SANTOS", "AV. CLAUDIO LUIZ DA COSTA, 50", "13-3202.0695", "SANTOS", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 4 - BAIXADA SANTISTA"],
    ["SOCIEDADE PORTUGUESA BENEFICÊNCIA - SANTOS", "AV. BERNARDINO DE CAMPOS, 47", "13-3229.3434", "SANTOS", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 4 - BAIXADA SANTISTA"],
    ["HOSPITAL GUILHERME ÁLVARO", "R. OSWALDO CRUZ, 197", "13-3202.1300", "SANTOS", "UNACON", "DRS 4 - BAIXADA SANTISTA"],
    ["FUNDAÇÃO PIO XII", "AV. ANTENOR DUARTE VILELA, 1.331", "17-3321.6600", "BARRETOS", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 5 - BARRETOS"],
    ["SANTA CASA DE AVARÉ", "R. PARAÍBA, 1.003", "14-3711.9100", "AVARÉ", "UNACON", "DRS 6 - BAURU"],
    ["HOSPITAL ESTADUAL DE BAURU", "AV. ENG. LUÍS CARRIJO, 1.100", "14-3103.777", "BAURU", "UNACON COM SERVIÇOS DE RADIOTERAPIA, HEMATOLOGIA E ONCOLOGIA PEDIÁTRICA", "DRS 6 - BAURU"],
    ["HOSPITAL DAS CLÍNICAS - UNESP", "R. RUBIAO JR., S/N", "14-6821.1466", "BOTUCATU", "UNACON COM SERVIÇOS DE RADIOTERAPIA, HEMATOLOGIA E ONCOLOGIA PEDIÁTRICA", "DRS 6 - BAURU"],
    ["HOSPITAL AMARAL CARVALHO", "R. DONA SILVERIA, 150", "14-3602.1200", "JAÚ", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 6 - BAURU"],
    ["HOSPITAL UNIVERSITÁRIO SÃO FRANCISCO", "AV. SÃO FRANCISCO DE ASSIS, 218", "11-4034.8000", "BRAGANCA PAULISTA", "UNACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 7 - CAMPINAS"],
    ["CENTRO INFANTIL DE INVESTIGAÇÃO HEMATOLÓGICA DR. DOMINGOS A. BOLDRINI", "R. DR.GABRIEL PORTO, 1.270", "19-3787.5000", "CAMPINAS", "UNACON EXCLUSIVA DE ONCOLOGIA PEDIÁTRICA COM SERVIÇO DE RADIOTERAPIA", "DRS 7 - CAMPINAS"],
    ["HOSPITAL E MATERNIDADE CELSO PIERRO", "AV. JOHN BOYD DUNLOP, S/N", "19-3343.8441", "CAMPINAS", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 7 - CAMPINAS"],
    ["HOSPITAL DAS CLÍNICAS - UNICAMP", "R.VITAL BRASIL, 251", "19-3788.8008", "CAMPINAS", "CACON", "DRS 7 - CAMPINAS"],
    ["HOSPITAL MUNICIPAL DR. MÁRIO GATTI", "R. PREFEITO FARIA LIMA, 340", "19-3772.5796", "CAMPINAS", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 7 - CAMPINAS"],
    ["HOSPITAL SÃO VICENTE DE PAULO", "R. S. VICENTE DE PAULO, 223", "11-4583.8155", "JUNDIAÍ", "UNACON COM SERVIÇOS DE HEMATOLOGIA E ONCOLOGIA PEDIÁTRICA", "DRS 7 - CAMPINAS"],
    ["SANTA CASA DE FRANCA", "PÇA. DOM PEDRO II, 1.826", "16-3711.4181", "FRANCA", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 8 - FRANCA"],
    ["HOSPITAL REGIONAL DE ASSIS", "PÇA. DR. SYMPHROSIO A. SANTOS, S/N", "18-0320.6000", "ASSIS", "UNACON", "DRS 9 - MARÍLIA"],
    ["HOSPITAL DAS CLÍNICAS DE MARÍLIA", "R. AZIZ ATALLAH, S/N", "14-3402.1744", "MARÍLIA", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 9 - MARÍLIA"],
    ["SANTA CASA DE MARÍLIA", "AV. VICENTE FERREIRA, 828", "14-3402.5555", "MARÍLIA", "UNACON COM SERVIÇOS DE HEMATOLOGIA E ONCOLOGIA PEDIÁTRICA", "DRS 9 - MARÍLIA"],
    ["SOCIEDADE BENEFICENTE SÃO FRANCISCO DE ASSIS DE TUPÃ", "R. COROADOS, 776", "14-3441.3622", "TUPÃ", "UNACON", "DRS 9 - MARÍLIA"],
    ["SANTA CASA DE ARARAS", "PÇA. DR. NARCISO GOMES, 49", "19-3543.5400", "ARARAS", "UNACON", "DRS 10 - PIRACICABA"],
    ["SANTA CASA DE LIMEIRA", "AV. ANTÔNIO OMETTO, 675", "19-3446.6122", "LIMEIRA", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 10 - PIRACICABA"],
    ["ASSOC. FORNECEDORES DE CANA DE PIRACICABA", "AV. BARÃO DE VALENÇA, 716", "19-3403.2800", "PIRACICABA", "UNACON COM SERVIÇOS DE RADIOTERAPIA E DE HEMATOLOGIA", "DRS 10 - PIRACICABA"],
    ["SANTA CASA DE PIRACICABA", "AV. INDEPENDÊNCIA, 953", "19-3417.5000", "PIRACICABA", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 10 - PIRACICABA"],
    ["SANTA CASA DE RIO CLARO", "R. DOIS, 297", "19-3535.7000", "RIO CLARO", "UNACON", "DRS 10 - PIRACICABA"],
    ["SANTA CASA PRESIDENTE PRUDENTE", "R. VENCESLAU BRAZ, 05", "18-2101.8000", "PRESIDENTE PRUDENTE", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 11 - PRESIDENTE PRUDENTE"],
    ["HOSPITAL REGIONAL DO VALE DO RIBEIRA", "R. DOS EXPEDICIONÁRIOS, 140", "13-3856.9600", "PARIQUERAAÇU", "UNACON", "DRS 12 - REGISTRO"],
    ["HOSPITAL DAS CLÍNICAS DE RIBEIRÃO PRETO", "CAMPUS UNIVERSITÁRIO, S/N", "16-3602.1000", "RIB. PRETO", "CACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 13 - RIBEIRÃO PRETO"],
    ["SOC. PORTUGUESA BENEFICÊNCIA RIB.PRETO", "R. TIBIRIÇA, 1.172", "16-3977.5500", "RIB. PRETO", "CACON", "DRS 13 - RIBEIRÃO PRETO"],
    ["SANTA CASA DE RIBEIRÃO PRETO", "AV. SAUDADE, 456", "16-3605.0606", "RIB. PRETO", "UNACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 13 - RIBEIRÃO PRETO"],
    ["HOSPITAL MUNICIPAL DR. TABAJARA RAMOS", "AV. PADRE JAIME, 1.500", "19-3891.9444", "MOGI GUAÇU", "UNACON", "DRS 14 - SÃO JOÃO DA BOA VISTA"],
    ["SANTA CASA DONA CAROLINA MALHEIROS", "R. CAROLINA MALHEIROS, 92", "19-3633.2222", "SÃO JOÃO DA BOA VISTA", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 14 - SÃO JOÃO DA BOA VISTA"],
    ["HOSPITAL PADRE ALBINO", "R. BELÉM, 519", "17-3531.3000", "CATANDUVA", "UNACON", "DRS 15 - SÃO JOSÉ DO RIO PRETO"],
    ["SANTA CASA S. J. RIO PRETO", "R. DR. FRITZ JACOBS, 1.236", "17-3214.9200", "S. J. RIO PRETO", "CACON", "DRS 15 - SÃO JOSÉ DO RIO PRETO"],
    ["HOSPITAL DE BASE DE SÃO JOSÉ DO RIO PRETO", "AV. BRIG. FARIA LIMA, 5.544", "17-3201.5000", "S. J. RIO PRETO", "UNACON COM SERVIÇOS DE HEMATOLOGIA E ONCOLOGIA PEDIÁTRICA", "DRS 15 - SÃO JOSÉ DO RIO PRETO"],
    ["CONJUNTO HOSPITALAR DE SOROCABA", "AV. COMENDADOR PEREIRA INÁCIO, 564", "15-3332.9121", "SOROCABA", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 16 - SOROCABA"],
    ["SANTA CASA DE SOROCABA", "AV. SÃO PAULO, 750", "15-2101.8000", "SOROCABA", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 16 - SOROCABA"],
    ["HOSPITAL E MATERNIDADE FREI GALVÃO", "R. DOMINGOS LEME, 77", "12-3128.3800", "GUARATINGUETÁ", "UNACON COM SERVIÇO DE RADIOTERAPIA", "DRS 17 - TAUBATÉ"],
    ["ASSOCIAÇÃO CASA FONTE DA VIDA", "R. ERNESTO DUARTE, 70", "12-3954.2400", "JACAREÍ", "UNACON", "DRS 17 - TAUBATÉ"],
    ["HOSPITAL E MATERNIDADE PIO XII", "R. PARAGUASSU, 51", "12-3928.3300", "SÃO JOSÉ DOS CAMPOS", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 17 - TAUBATÉ"],
    ["IPMMI / HOSPITAL MATERNO INFANTIL ANTONINHO DA ROCHA MARMO", "AV. HEITOR VILLA LOBOS, 1.961", "12-3797.0777", "SÃO JOSÉ DOS CAMPOS", "UNACON", "DRS 17 - TAUBATÉ"],
    ["GACC - GRUPO DE ASSISTÊNCIA À CRIANÇA COM CÂNCER", "AV. POSSIDONIO JOSÉ DE FREITAS, 1.200", "12-3949.3167", "SÃO JOSÉ DOS CAMPOS", "UNACON COM SERVIÇO DE ONCOLOGIA PEDIÁTRICA", "DRS 17 - TAUBATÉ"],
    ["HOSPITAL REGIONAL VALE DO PARAÍBA", "AV. TIRADENTES, 280", "12-3634.2000", "TAUBATÉ", "UNACON COM SERVIÇO DE HEMATOLOGIA", "DRS 17 - TAUBATÉ"],
    ["INSTITUTO DE RADIOTERAPIA DO ABC", "AV. PORTUGAL, 592", "11-4438.9900", "SANTO ANDRÉ", "SERVIÇO ISOLADO DE RADIOTERAPIA", "DRS 17 - TAUBATÉ"],
    ["INSTITUTO DE RADIOTERAPIA PRESIDENTE PRUDENTE S/C LTDA", "AV. MANOEL GOULART, 3.301", "18-3222.3100", "PRESIDENTE PRUDENTE", "SERVIÇO ISOLADO DE RADIOTERAPIA", "DRS 17 - TAUBATÉ"],
    ["INSTITUTO DE RADIOTERAPIA VALE DO PARAÍBA", "R. MAJOR ANTÔNIO DOMINGUES, 494", "12-3921.9055", "SÃO JOSÉ DOS CAMPOS", "SERVIÇO ISOLADO DE RADIOTERAPIA", "DRS 17 - TAUBATÉ"]
]

# Criação do DataFrame
df_hospitais = pd.DataFrame(data, columns=["Nome", "Endereço", "Telefone", "Município", "Tipo", "DRS"])

# Exibir o DataFrame
df_hospitais

# Salvar em um arquivo CSV (opcional)
df_hospitais.to_csv("hospitais.csv", index=False)


# Função para contar citações no dataset tjsp
def count_citations(hospitals, tjsp_data):
    citations = defaultdict(int)
    for hospital in hospitals['Nome']:
        pattern = re.compile(r'\b' + re.escape(hospital) + r'\b', re.IGNORECASE)
        citations[hospital] = int(tjsp_data['julgado'].str.contains(pattern, regex=True).sum())
    return citations

# Função para obter coordenadas geográficas
def get_coordinates(address):
    geolocator = Nominatim(user_agent="my_agent")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
    except (GeocoderTimedOut, GeocoderServiceError):
        pass
    return None

# Carregar os dados dos hospitais
#hospitals = df_hospitais
hospitals = pd.read_csv("/content/hospitais.csv")

# Carregar o dataset tjsp (substitua 'caminho/para/tjsp_dataset.csv' pelo caminho real do seu arquivo)
tjsp_data = pd.read_csv('/content/drive/MyDrive/pos_doc_usp/analise/tjsp_data.csv')

# Contar citações
citations = count_citations(hospitals, tjsp_data)

# Criar mapa
m = folium.Map(location=[-23.5505, -46.6333], zoom_start=7)  # Centralizado em São Paulo

plotted_hospitals = 0
for index, row in hospitals.iterrows():
    hospital = row['Nome']
    endereco = row['Endereço']
    municipio = row['Município']
    full_address = f"{endereco}, {municipio}, São Paulo, Brasil"
    coords = get_coordinates(full_address)
    if coords:
        folium.CircleMarker(
            location=coords,
            radius=max(5, min(citations[hospital], 20)),  # Limita o raio entre 5 e 20
            popup=f"{hospital}: {citations[hospital]} citações",
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(m)
        plotted_hospitals += 1

# Exibir o número de hospitais plotados
print(f"Número de hospitais plotados no mapa: {plotted_hospitals}")

# Salvar o mapa
m.save("mapa_citacoes_hospitais_municipio.html")

print("Mapa gerado e salvo como 'mapa_citacoes_hospitais_municipio.html'")

# Exibir o DataFrame com as contagens de citações
citations_df = pd.DataFrame(list(citations.items()), columns=['Hospital', 'Citações'])
print(citations_df)

# Salvar o DataFrame em um arquivo CSV para visualização
citations_df.to_csv("/content/citacoes_hospitais_novo.csv", index=False)
print("DataFrame de citações salvo como 'citacoes_hospitais.csv'")


# Carregar o dataset TJSP
tjsp_data = pd.read_csv('/content/drive/MyDrive/pos_doc_usp/analise/tjsp_data.csv')

# Lista de medicamentos
medicamentos = [
    "ABIRATERONA", "AFLIBERCEPTE", "APIXABANA", "BORTEZOMIBE", "BROMETO DE TIOTRÓPIO", "CANABIDIOL",
    "DENOSUMABE", "DULOXETINA", "ENXOPARINA", "INSULINA E INSUMOS", "LISDEXANFETAMINA", "OMALIZUMABE",
    "PREGABALINA", "RANIBIZUMABE", "RITUXIMABE", "RIVAROXABANA", "SACUBITRIL + VALSARTANA", "SORAFENIBE",
    "TEMOZOLAMIDA", "TERIPARATIDA"
]
def count_medication_citations(medications, tjsp_data):
    citations = defaultdict(lambda: defaultdict(int))
    for medication in medications:
        pattern = re.compile(r'\b' + re.escape(medication) + r'\b', re.IGNORECASE)
        matches = tjsp_data['julgado'].str.contains(pattern, regex=True)
        municipios = tjsp_data.loc[matches, 'comarca']
        for municipio in municipios:
            citations[medication][municipio] += 1
    return citations

medication_citations = count_medication_citations(medicamentos, tjsp_data)


# Função para obter coordenadas geográficas
def get_coordinates(address):
    geolocator = Nominatim(user_agent="my_agent")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
    except (GeocoderTimedOut, GeocoderServiceError):
        pass
    return None

# Criar mapa
m = folium.Map(location=[-23.5505, -46.6333], zoom_start=7)  # Centralizado em São Paulo

# Plotar medicamentos no mapa
for medication, municipios in medication_citations.items():
    for municipio, count in municipios.items():
        coords = get_coordinates(f"{municipio}, São Paulo, Brasil")
        if coords:
            folium.CircleMarker(
                location=coords,
                radius=max(5, min(count, 20)),  # Limita o raio entre 5 e 20
                popup=f"{medication}: {count} citações em {municipio}",
                color='blue',
                fill=True,
                fill_color='blue'
            ).add_to(m)

# Salvar o mapa
m.save("mapa_citacoes_medicamentos.html")



# Função para contar citações dos medicamentos no dataset TJSP
def count_medication_citations(medications, tjsp_data):
    citations = defaultdict(lambda: defaultdict(int))
    for medication in medications:
        pattern = re.compile(r'\b' + re.escape(medication) + r'\b', re.IGNORECASE)
        matches = tjsp_data['julgado'].str.contains(pattern, regex=True)
        comarcas = tjsp_data.loc[matches, 'comarca']
        for comarca in comarcas:
            citations[medication][comarca] += 1
    return citations

# Lista de medicamentos
medicamentos = [
    "ABIRATERONA", "AFLIBERCEPTE", "APIXABANA", "BORTEZOMIBE", "BROMETO DE TIOTRÓPIO", "CANABIDIOL",
    "DENOSUMABE", "DULOXETINA", "ENXOPARINA", "INSULINA E INSUMOS", "LISDEXANFETAMINA", "OMALIZUMABE",
    "PREGABALINA", "RANIBIZUMABE", "RITUXIMABE", "RIVAROXABANA", "SACUBITRIL + VALSARTANA", "SORAFENIBE",
    "TEMOZOLAMIDA", "TERIPARATIDA"
]

# Carregar o dataset TJSP (substitua 'caminho/para/tjsp_dataset.csv' pelo caminho real do seu arquivo)
tjsp_data = pd.read_csv('/content/drive/MyDrive/pos_doc_usp/analise/tjsp_data.csv')

# Contar as citações dos medicamentos
medication_citations = count_medication_citations(medicamentos, tjsp_data)

# Preparar dados para o Dash
citation_list = []
for medication, comarcas in medication_citations.items():
    for comarca, count in comarcas.items():
        citation_list.append({'medication': medication, 'comarca': comarca, 'count': count})

citation_df = pd.DataFrame(citation_list)

# Iniciar o Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Citações de Medicamentos por Comarca"),
    dcc.Dropdown(
        id='medication-dropdown',
        options=[{'label': med, 'value': med} for med in medicamentos],
        value=medicamentos[0]
    ),
    dcc.Graph(id='citation-graph'),
    dcc.Graph(id='citation-map')
])

@app.callback(
    [Output('citation-graph', 'figure'), Output('citation-map', 'figure')],
    [Input('medication-dropdown', 'value')]
)
def update_dashboard(selected_medication):
    filtered_df = citation_df[citation_df['medication'] == selected_medication]

    fig = px.bar(filtered_df, x='comarca', y='count', title=f"Citações de {selected_medication} por Comarca")

    # Adicionar coordenadas fictícias para o exemplo
    filtered_df['latitude'] = filtered_df['comarca'].apply(lambda x: -23.5505 + hash(x) % 10 * 0.01)
    filtered_df['longitude'] = filtered_df['comarca'].apply(lambda x: -46.6333 + hash(x) % 10 * 0.01)

    map_fig = px.scatter_mapbox(
        filtered_df, lat='latitude', lon='longitude', size='count',
        color='count', hover_name='comarca', zoom=6,
        mapbox_style="carto-positron"
    )
    return fig, map_fig

if __name__ == '__main__':
    app.run_server(debug=True)


# Função para contar citações dos medicamentos no dataset TJSP
def count_medication_citations(medications, tjsp_data):
    citations = defaultdict(lambda: defaultdict(int))
    for medication in medications:
        pattern = re.compile(r'\b' + re.escape(medication) + r'\b', re.IGNORECASE)
        matches = tjsp_data['julgado'].str.contains(pattern, regex=True)
        comarcas = tjsp_data.loc[matches, 'comarca']
        for comarca in comarcas:
            citations[medication][comarca] += 1
    return citations

# Cache para coordenadas
coords_cache = {}

# Função para obter coordenadas geográficas com cache e lógica de repetição
def get_coordinates(address):
    if address in coords_cache:
        return coords_cache[address]

    geolocator = Nominatim(user_agent="my_agent", timeout=10)
    retries = 3
    for i in range(retries):
        try:
            location = geolocator.geocode(address)
            if location:
                coords_cache[address] = (location.latitude, location.longitude)
                return location.latitude, location.longitude
        except (GeocoderTimedOut, GeocoderServiceError):
            time.sleep(2 ** i)  # Espera exponencial antes de tentar novamente

    return None

# Lista de medicamentos
medicamentos = [
    "ABIRATERONA", "AFLIBERCEPTE", "APIXABANA", "BORTEZOMIBE", "BROMETO DE TIOTRÓPIO", "CANABIDIOL",
    "DENOSUMABE", "DULOXETINA", "ENXOPARINA", "INSULINA E INSUMOS", "LISDEXANFETAMINA", "OMALIZUMABE",
    "PREGABALINA", "RANIBIZUMABE", "RITUXIMABE", "RIVAROXABANA", "SACUBITRIL + VALSARTANA", "SORAFENIBE",
    "TEMOZOLAMIDA", "TERIPARATIDA"
]

# Carregar o dataset TJSP (substitua 'caminho/para/tjsp_dataset.csv' pelo caminho real do seu arquivo)
tjsp_data = pd.read_csv('/content/drive/MyDrive/pos_doc_usp/analise/tjsp_data.csv')

# Contar as citações dos medicamentos
medication_citations = count_medication_citations(medicamentos, tjsp_data)

# Preparar dados para o Streamlit
citation_list = []
for medication, comarcas in medication_citations.items():
    for comarca, count in comarcas.items():
        coords = get_coordinates(f"{comarca}, São Paulo, Brasil")
        if coords:
            citation_list.append({
                'medication': medication,
                'comarca': comarca,
                'count': count,
                'latitude': coords[0],
                'longitude': coords[1]
            })

citation_df = pd.DataFrame(citation_list)

# Iniciar o Streamlit
st.title("Ações de Medicamentos por Comarca / município")

# Dropdown para selecionar o medicamento
selected_medication = st.selectbox("Selecione o Medicamento", medicamentos)

# Filtrar dados com base na seleção
filtered_df = citation_df[citation_df['medication'] == selected_medication]

# Gráfico de barras
st.subheader(f"Citações de {selected_medication} por Comarca")
bar_fig = px.bar(filtered_df, x='comarca', y='count', title=f"Citações de {selected_medication} por Comarca")
st.plotly_chart(bar_fig)

# Gráfico de pizza
st.subheader(f"Distribuição das Citações de {selected_medication}")
pie_fig = px.pie(filtered_df, names='comarca', values='count', title=f"Distribuição das Citações de {selected_medication}")
st.plotly_chart(pie_fig)

# Mapa interativo
st.subheader(f"Mapa das Citações de {selected_medication}")
m = folium.Map(location=[-23.5505, -46.6333], zoom_start=7)  # Centralizado em São Paulo
marker_cluster = MarkerCluster().add_to(m)

for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['comarca']}: {row['count']} citações"
    ).add_to(marker_cluster)

# Exibir o mapa no Streamlit
from streamlit_folium import st_folium
st_folium(m)

