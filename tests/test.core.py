import igraph as ig
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

g = ig.Graph(15, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), 
	(0, 11), (0, 12), (0, 13), (0, 14), (0, 15)], directed=True)

g['title'] = "Linhas de trem e metrô da cidade de São Paulo"
g.vs['name'] = ['Linha 1 Azul', 'Linha 2 Verde', 'Linha 2 Verde', 'Linha 3 Vermelha', 'Linha 4 Amarela', 
'Linha 5 Lilás', 'Linha 6 Laranja' ,'Linha 7 Rubí', 'Linha 8 Diamante', 'Linha 9 Esmeralda', 'Linha 10 Turquesa',
'Linha 11 Coral', 'Linha 12 Safira', 'Linha 13 Jade', 'Linha 14 Onix', 'Linha 15 Prata']
g.es["capacity"] = [7, 8, 1, 2, 3, 4, 5]

#Cores correspondentes de cada linha:
line_colors = {
	'Linha 1 Azul': 'blue', 'Linha 2 Verde': 'green', 'Linha 3 Vermelha': 'red', 'Linha 4 Amarela': 'yellow', 
	'Linha 5 Lilás': 'pink', 'Linha 6 Laranja': 'orange', 'Linha 7 Rubí': 'red', 'Linha 8 Diamante': 'blue', 'Linha 9 Esmeralda': 'green',
	'Linha 10 Turquesa': 'gray', 'Linha 11 Coral': 'gray', 'Linha 12 Safira': 'red', 'Linha 13 Jade': 'blue',
	'Linha 14 Onix': '#dddd', 'Linha 15 Prata': 'gray',
}
g.vs['color'] = [line_colors[name] for name in g.vs['name']]

flow = g.maxflow(3, 0, capacity=g.es["capacity"])

print("Max flow:", flow.value)
print("Edge assignments:", flow.flow)

# Output:
# Max flow: 6.0
# Edge assignments [1.0, 5.0, 1.0, 2.0, 3.0, 3.0, 3.0]

fig, ax = plt.subplots()
ig.plot(
    g,
    target=ax,
    layout="circle",
    vertex_label = g.vs['name'],
    vertex_color = g.vs['color']
)
plt.title(g['title'])

#Legendas de cada linha de trem
legends = [mpatches.Patch(color=color, label=line) for  line, color in line_colors.items()]
#plt.legend(handles=legends, bbox_to_anchor=(1.05, 1), loc = 'upper left')

plt.show()