# hospitals_judje_sp

## README.md: Análise e Visualização de Citações de Medicamentos em Ações Judiciais

Este script Python realiza a análise e visualização de citações de medicamentos em ações judiciais, utilizando dados do Tribunal de Justiça de São Paulo (TJSP). Ele processa um dataset contendo informações sobre as ações e identifica a frequência com que determinados medicamentos são mencionados em diferentes comarcas. Os resultados são apresentados em gráficos interativos e um mapa, permitindo explorar a distribuição geográfica das citações.

### Funcionalidades Principais

1.  **Contagem de Citações:**
    *   Carrega um dataset CSV contendo informações sobre ações judiciais.
    *   Recebe uma lista de medicamentos de interesse.
    *   Conta o número de vezes que cada medicamento é citado em cada comarca, utilizando expressões regulares para busca no texto das ações.

2.  **Geolocalização:**
    *   Utiliza o serviço de geocodificação Nominatim para obter as coordenadas geográficas das comarcas.
    *   Implementa um cache para evitar requisições repetidas ao serviço de geocodificação, otimizando o desempenho.
    *   Lida com possíveis erros de geocodificação, como timeouts ou indisponibilidade do serviço.

3.  **Visualização:**
    *   Cria um mapa interativo com marcadores para cada comarca, com o tamanho do marcador representando a quantidade de citações de um medicamento selecionado.
    *   Gera gráficos de barras e pizza para visualizar a distribuição das citações por comarca.
    *   Permite a seleção do medicamento a ser analisado através de um dropdown.

### Requisitos

*   Python 3.x
*   Bibliotecas: `pandas`, `folium`, `geopy`, `plotly`, `streamlit`, `streamlit_folium` (instale usando `pip install -r requirements.txt`)

### Como Usar

1.  **Preparar os Dados:**
    *   Tenha um arquivo CSV contendo os dados das ações judiciais do TJSP, com colunas relevantes como "julgado" (texto da ação) e "comarca".
    *   Adapte o caminho do arquivo no código (`'/content/drive/MyDrive/pos_doc_usp/analise/tjsp_data.csv'`) para o local correto do seu arquivo.
    *   Se necessário, ajuste a lista de `medicamentos` para incluir os medicamentos de seu interesse.

2.  **Executar o Script:**
    *   Abra um terminal ou prompt de comando.
    *   Navegue até o diretório onde o script está salvo.
    *   Execute o comando: `streamlit run nome_do_seu_script.py`

3.  **Interagir com a Aplicação:**
    *   A aplicação será aberta em seu navegador padrão.
    *   Utilize o dropdown para selecionar o medicamento que deseja analisar.
    *   O mapa e os gráficos serão atualizados automaticamente para exibir as citações do medicamento selecionado.

### Adaptações Necessárias

*   **Caminhos dos Arquivos:** Certifique-se de que os caminhos para os arquivos CSV (`tjsp_data.csv` e `hospitais.csv`) estejam corretos em seu ambiente.
*   **Instalação de Dependências:** Execute `pip install -r requirements.txt` para instalar as bibliotecas necessárias.
*   **Configuração do Nominatim:** Se encontrar problemas com o serviço de geocodificação, você pode precisar configurar um servidor Nominatim local ou usar uma chave de API para um serviço de geocodificação alternativo.
*   **Dados Fictícios:** O código atualmente adiciona coordenadas fictícias para demonstração. Remova essa parte e utilize a função `get_coordinates` para obter as coordenadas reais das comarcas.

### Observações

*   Este script oferece uma visualização interativa e informativa das citações de medicamentos em ações judiciais.
*   A análise pode ser expandida para incluir outras variáveis, como tipos de ações, datas, etc.
*   Certifique-se de ter acesso aos dados do TJSP e permissão para utilizá-los.

**requirements.txt**

```
pandas
folium
geopy
plotly
streamlit
streamlit-folium
```
