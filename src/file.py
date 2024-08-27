import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = 'C:\\Projects\\Python\\Desktop\\ComNet Project\\data\\dados.csv'

try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

df['Estacao'] = df['Estacao'].str.strip().str.title()

print(df.head())

G = nx.Graph()
# Adicionar nós ao grafo
for index, row in df.iterrows():
    estacao = row['Estacao']
    demanda_media = row['Demanda']
    
    # Adicionar o nó com o atributo de demanda média
    G.add_node(estacao, demanda=demanda_media)

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

# Salvar métricas de centralidade em um arquivo CSV
df_centralities = pd.DataFrame({
    'Estacao': list(G.nodes),
    'Degree_Centrality': [degree_centrality[node] for node in G.nodes],
    'Betweenness_Centrality': [betweenness_centrality[node] for node in G.nodes],
    'Eigenvector_Centrality': [eigenvector_centrality[node] for node in G.nodes]
})
df_centralities.to_csv('centralities.csv', index=False)

# Identificar componentes conexos
componentes_conexos = list(nx.connected_components(G))

# Salvar componentes conexos em um arquivo CSV
df_componentes = pd.DataFrame({
    'Componente': [f'Componente {i+1}' for i in range(len(componentes_conexos))],
    'Estacoes': [', '.join(componente) for componente in componentes_conexos]
})
df_componentes.to_csv('componentes_conexos.csv', index=False)

# Identificar pontos de articulação
pontos_articulacao = list(nx.articulation_points(G))
df_articulacao = pd.DataFrame({
    'Pontos_de_Articulacao': pontos_articulacao
})
df_articulacao.to_csv('pontos_articulacao.csv', index=False)

# Análise de fluxo - Exemplo de cálculo de fluxo máximo entre duas estações
origem = 'Brás'
destino = 'República'
fluxo_maximo, fluxo_dict = nx.maximum_flow(G, origem, destino, capacity='weight')

df_fluxo_maximo = pd.DataFrame({
    'Origem': [origem],
    'Destino': [destino],
    'Fluxo_Maximo': [fluxo_maximo]
})
df_fluxo_maximo.to_csv('fluxo_maximo.csv', index=False)

# Análise de caminho mínimo
caminho_minimo = nx.shortest_path(G, source=origem, target=destino, weight='weight')
distancia_minima = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')

df_caminho_minimo = pd.DataFrame({
    'Origem': [origem],
    'Destino': [destino],
    'Caminho_Minimo': [', '.join(caminho_minimo)],
    'Distancia_Minima': [distancia_minima]
})
df_caminho_minimo.to_csv('caminho_minimo.csv', index=False)

plt.figure(figsize=(12, 8))
pos = nx.random_layout(G)
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
