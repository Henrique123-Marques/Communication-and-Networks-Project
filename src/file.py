import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = 'C:\\Projects\\Python\\Desktop\\ComNet Project\\data\\dados.csv'

try:
    # Tenta ler o arquivo CSV com a codificação utf-8
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    # Se falhar, tenta com a codificação 'ISO-8859-1'
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Remover espaços em branco e padronizar capitalização nos nomes das estações
df['Estacao'] = df['Estacao'].str.strip().str.title()

print(df.head())

# Inicializar o grafo
G = nx.Graph()

# Adicionar nós ao grafo
for index, row in df.iterrows():
    estacao = row['Estacao']
    demanda_media = row['Demanda']
    
    # Adicionar o nó com o atributo de demanda média
    G.add_node(estacao, demanda=demanda_media)

# Imprimir todos os nós do grafo para depuração
#print("Nós do grafo (estações):")
#	print(G.nodes)

# Definir conexões (corrigir para refletir o padrão de capitalização e remoção de espaços)
conexoes = [
    ('Ana Rosa', 'Paraíso'),
    ('Sé', 'Luz'),
    ('Vila Prudente', 'Tamanduateí'),
    ('Paulista', 'Consolação'),
    ('Brás', 'República'),
    ('Santa Cecília', 'Barra Funda'),
    ('Pinheiros', 'Pinheiros')
    # Adicione todas as conexões reais
]

# Remover espaços e padronizar nomes nas conexões
conexoes = [(estacao1.strip().title(), estacao2.strip().title()) for estacao1, estacao2 in conexoes]

# Adicionar arestas ao grafo com base nas conexões
for estacao1, estacao2 in conexoes:
    if estacao1 in G.nodes and estacao2 in G.nodes:
        demanda1 = G.nodes[estacao1]['demanda']
        demanda2 = G.nodes[estacao2]['demanda']
        
        # Defina o peso da aresta como a média das demandas das duas estações conectadas
        peso = (demanda1 + demanda2) / 2
        G.add_edge(estacao1, estacao2, weight=peso)
    else:
        print(f"Erro: Uma ou ambas as estações '{estacao1}' ou '{estacao2}' não existem no grafo.")


# Cálculo das métricas de centralidade
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G, weight='weight')
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
print(f"Grau de Centralidade (Degree Centrality): {degree_centrality}")
print(f"\nCentralidade de Intermediação (Betweenness Centrality): {betweenness_centrality}")
print(f"\nCentralidade de Conectividade (Eigenvector Centrality): {eigenvector_centrality}")

#ANALISE DE CONECTIVIDADE - Identificar componentes conexos
componentes_conexos = list(nx.connected_components(G))
print(f"Componentes Conexos (Sub-redes):")
for i, componente in enumerate(componentes_conexos):
    print(f"Componente {i+1}: {componente}")

# RESILIENCIA DE REDE - Identificar pontos de articulação
pontos_articulacao = list(nx.articulation_points(G))
# Exibir pontos de articulação
print("Pontos Críticos (Pontos de Articulação):")
print(pontos_articulacao)


# ANALISE DE FLUXO - Exemplo de cálculo de fluxo máximo entre duas estações
origem = 'Brás'
destino = 'República'
fluxo_maximo, fluxo_dict = nx.maximum_flow(G, origem, destino, capacity='weight')
print(f"Fluxo Máximo entre {origem} e {destino}: {fluxo_maximo}")

#CAMINHO MINIMO 
origem = 'Brás'
destino = 'República'
# Encontrar o caminho mais curto considerando o peso das arestas
caminho_minimo = nx.shortest_path(G, source=origem, target=destino, weight='weight')
print(f"Caminho Mínimo entre {origem} e {destino}: {caminho_minimo}")
distancia_minima = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')
print(f"Distância do Caminho Mínimo entre {origem} e {destino}: {distancia_minima}")


# Desenhar o grafo
plt.figure(figsize=(12, 8))
#pos = nx.spring_layout(G, seed=42)  # Layout do grafo
pos = nx.random_layout(G)

# Desenhar nós
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
# Desenhar arestas com espessura proporcional ao peso
edges = nx.draw_networkx_edges(
    G, pos, 
    edgelist=G.edges(data=True), 
    width=[d['weight']/1000 for (u, v, d) in G.edges(data=True)],
    alpha=0.6
)
nx.draw_networkx_labels(G, pos, font_size=8)
plt.title('Grafo das Estações de Metrô e Trem de São Paulo')
plt.show()
