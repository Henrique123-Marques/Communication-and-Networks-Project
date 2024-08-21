import igraph as ig
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Criação do grafo
g = ig.Graph(directed=False)

# Dados das estações e conexões (arestas)
stations = [
    {'id': 0, 'name': 'Tucuruvi', 'line': 'Linha 1 Azul'},
    {'id': 1, 'name': 'Santana', 'line': 'Linha 1 Azul'},
    {'id': 2, 'name': 'Sé', 'line': 'Linha 1 Azul'},
    {'id': 3, 'name': 'Ana Rosa', 'line': 'Linha 1 Azul'},
    {'id': 4, 'name': 'Jabaquara', 'line': 'Linha 1 Azul'},
    {'id': 5, 'name': 'Vila Prudente', 'line': 'Linha 2 Verde'},
    {'id': 6, 'name': 'Tamanduateí', 'line': 'Linha 2 Verde'},
    {'id': 7, 'name': 'Sacomã', 'line': 'Linha 2 Verde'},
    {'id': 8, 'name': 'Chácara Klabin', 'line': 'Linha 2 Verde'},
    {'id': 9, 'name': 'Vila Madalena', 'line': 'Linha 2 Verde'},
    {'id': 10, 'name': 'Barra Funda', 'line': 'Linha 3 Vermelha'},
    {'id': 11, 'name': 'Marechal Deodoro', 'line': 'Linha 3 Vermelha'},
    {'id': 12, 'name': 'Anhangabaú', 'line': 'Linha 3 Vermelha'},
    {'id': 13, 'name': 'Tatuapé', 'line': 'Linha 3 Vermelha'},
    {'id': 14, 'name': 'Corinthians-Itaquera', 'line': 'Linha 3 Vermelha'},
    {'id': 15, 'name': 'Luz', 'line': 'Linha 4 Amarela'},
    {'id': 16, 'name': 'República', 'line': 'Linha 4 Amarela'},
    {'id': 17, 'name': 'Higienópolis-Mackenzie', 'line': 'Linha 4 Amarela'},
    {'id': 18, 'name': 'Paulista', 'line': 'Linha 4 Amarela'},
    {'id': 19, 'name': 'Fradique Coutinho', 'line': 'Linha 4 Amarela'},
    {'id': 20, 'name': 'Faria Lima', 'line': 'Linha 4 Amarela'},
    {'id': 21, 'name': 'Pinheiros', 'line': 'Linha 4 Amarela'},
    {'id': 22, 'name': 'Butantã', 'line': 'Linha 4 Amarela'},
    {'id': 23, 'name': 'São Paulo-Morumbi', 'line': 'Linha 4 Amarela'},
    {'id': 24, 'name': 'Vila Sônia', 'line': 'Linha 4 Amarela'},
    {'id': 25, 'name': 'Capão Redondo', 'line': 'Linha 5 Lilás'},
    {'id': 26, 'name': 'Campo Limpo', 'line': 'Linha 5 Lilás'},
    {'id': 27, 'name': 'Vila das Belezas', 'line': 'Linha 5 Lilás'},
    {'id': 28, 'name': 'Giovanni Gronchi', 'line': 'Linha 5 Lilás'},
    {'id': 29, 'name': 'Santo Amaro', 'line': 'Linha 5 Lilás'},
    {'id': 30, 'name': 'Largo Treze', 'line': 'Linha 5 Lilás'},
    {'id': 31, 'name': 'Adolfo Pinheiro', 'line': 'Linha 5 Lilás'},
    {'id': 32, 'name': 'Alto da Boa Vista', 'line': 'Linha 5 Lilás'},
    {'id': 33, 'name': 'Borba Gato', 'line': 'Linha 5 Lilás'},
    {'id': 34, 'name': 'Brooklin', 'line': 'Linha 5 Lilás'},
    {'id': 35, 'name': 'Campo Belo', 'line': 'Linha 5 Lilás'},
    {'id': 36, 'name': 'Eucaliptos', 'line': 'Linha 5 Lilás'},
    {'id': 37, 'name': 'Moema', 'line': 'Linha 5 Lilás'},
    {'id': 38, 'name': 'AACD-Servidor', 'line': 'Linha 5 Lilás'},
    {'id': 39, 'name': 'Hospital São Paulo', 'line': 'Linha 5 Lilás'},
    {'id': 40, 'name': 'Santa Cruz', 'line': 'Linha 5 Lilás'},
    {'id': 41, 'name': 'Chácara Klabin', 'line': 'Linha 5 Lilás'},
    {'id': 42, 'name': 'Oratório', 'line': 'Linha 15 Prata'},
    {'id': 43, 'name': 'São Lucas', 'line': 'Linha 15 Prata'},
    {'id': 44, 'name': 'Camilo Haddad', 'line': 'Linha 15 Prata'},
    {'id': 45, 'name': 'Vila Tolstói', 'line': 'Linha 15 Prata'},
    {'id': 46, 'name': 'Vila União', 'line': 'Linha 15 Prata'},
    {'id': 47, 'name': 'Jardim Planalto', 'line': 'Linha 15 Prata'},
    {'id': 48, 'name': 'Sapopemba', 'line': 'Linha 15 Prata'},
    {'id': 49, 'name': 'Fazenda da Juta', 'line': 'Linha 15 Prata'},
    {'id': 50, 'name': 'São Mateus', 'line': 'Linha 15 Prata'},
    {'id': 51, 'name': 'Jardim Colonial', 'line': 'Linha 15 Prata'}
]

edges = [
    # Linha 1 Azul
    (0, 1), (1, 2), (2, 3), (3, 4),
    # Linha 2 Verde
    (5, 6), (6, 7), (7, 8), (8, 9),
    # Linha 3 Vermelha
    (10, 11), (11, 12), (12, 13), (13, 14),
    # Linha 4 Amarela
    (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24),
    # Linha 5 Lilás
    (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41),
    # Linha 15 Prata
    (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 48), (48, 49), (49, 50), (50, 51)
]

# Adicionar vértices ao grafo
for station in stations:
    g.add_vertex(name=station['name'], line=station['line'])

# Adicionar arestas ao grafo
g.add_edges(edges)

# Dicionário mapeando as linhas às suas cores
line_colors = {
    'Linha 1 Azul': 'blue',
    'Linha 2 Verde': 'green',
    'Linha 3 Vermelha': 'red',
    'Linha 4 Amarela': 'yellow',
    'Linha 5 Lilás': 'purple',
    'Linha 15 Prata': 'silver'
}

# Atribuir as cores aos vértices
g.vs['color'] = [line_colors[station['line']] for station in stations]
g.vs['label'] = [station['name'] for station in stations]

# Detectar comunidades
communities = g.community_multilevel()

# Plotar o grafo com comunidades
fig, ax = plt.subplots()
ig.plot(
    communities,
    target=ax,
    layout="fruchterman_reingold",
    vertex_label=g.vs['label'],
    vertex_color=g.vs['color'],
    edge_color="gray"
)

# Adicionar título
plt.title("Linhas de trem e metrô da cidade de São Paulo separados por comunidades simples")

# Criar legendas
handles = [mpatches.Patch(color=color, label=line) for line, color in line_colors.items()]
plt.legend(handles=handles, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()