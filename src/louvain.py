import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain

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

# Inicializar o grafo
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
    ('Trianon-Masp', 'Consolação'),
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

# Aplicar o algoritmo de Louvain para detectar comunidades
particao = community_louvain.best_partition(G, weight='weight')

# Exibir as comunidades detectadas
print("Comunidades detectadas:")
for estacao, comunidade in particao.items():
    print(f"Estação: {estacao} - Comunidade: {comunidade}")

# Calcular a modularidade da partição
modularidade = community_louvain.modularity(particao, G, weight='weight')
print(f"Modularidade da rede: {modularidade:.4f}")

# Visualizar o grafo com as comunidades
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)

# Desenhar nós com cores baseadas nas comunidades
cores = [particao[estacao] for estacao in G.nodes]
nx.draw_networkx_nodes(G, pos, node_size=500, cmap=plt.cm.Set3, node_color=cores)

# Desenhar arestas
nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=1, alpha=0.5)

# Desenhar rótulos dos nós
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title('Comunidades nas Estações de Metrô e Trem de São Paulo (Algoritmo de Louvain)')
plt.show()
