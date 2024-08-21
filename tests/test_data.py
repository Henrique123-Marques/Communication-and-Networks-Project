import igraph as ig
import pandas as pd
import matplotlib.pyplot as plt

# Carregue o arquivo CSV (substitua pelo caminho correto)
df = pd.read_csv('C:/Projects/Python/Desktop/ComNet Project/data/Nodes.csv')

# Crie um grafo vazio
g = ig.Graph(directed=False)

# Adicione vértices ao grafo
for index, row in df.iterrows():
    g.add_vertex(name=row['Label'], id=row['ID'])

# Adicionando algumas conexões fictícias
g.add_edges([(1, 2), (2, 3), (3, 4), (4, 5)])

# Exemplo de análise: número de estações (vértices) e conexões (arestas)
print(f"Número de estações: {g.vcount()}")
print(f"Número de conexões: {g.ecount()}")

# Plotar o grafo
layout = g.layout("fruchterman_reingold")

# Usar Matplotlib para plotar
fig, ax = plt.subplots(figsize=(10, 10))

ig.plot(
    g,
    target=ax,
    layout=layout,
    vertex_size=20,       # Tamanho do círculo
    vertex_color="skyblue", # Cor do vértice
    vertex_label=None,     # Sem rótulo
    edge_width=1,
    bbox=(0, 0, 800, 800),
    margin=20
)

# Exibir o grafo
plt.show()