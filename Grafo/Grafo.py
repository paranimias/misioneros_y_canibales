import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from collections import deque

def es_valido(estado):
    m, c, b = estado
    if m < 0 or m > 3 or c < 0 or c > 3: return False
    if m > 0 and m < c: return False
    if (3 - m) > 0 and (3 - m) < (3 - c): return False
    return True

def obtener_sucesores(estado):
    m, c, b = estado
    sucesores = []
    movimientos = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for dm, dc in movimientos:
        if b == 1: nuevo_estado = (m - dm, c - dc, 0)
        else:      nuevo_estado = (m + dm, c + dc, 1)
        if es_valido(nuevo_estado):
            sucesores.append(nuevo_estado)
    return sucesores

def busqueda_bfs(inicio, meta):
    grafo = nx.Graph()
    cola = deque([inicio])
    niveles = {inicio: 0}
    visitados = set([inicio])
    padres = {inicio: None} 

    while cola:
        actual = cola.popleft()
        nivel_actual = niveles[actual]
        
        for sucesor in obtener_sucesores(actual):
            grafo.add_edge(actual, sucesor)
            if sucesor not in visitados:
                visitados.add(sucesor)
                niveles[sucesor] = nivel_actual + 1
                padres[sucesor] = actual
                cola.append(sucesor)
                
    camino = []
    aristas = []
    
    if meta in visitados:
        paso_actual = meta
        while paso_actual is not None:
            camino.append(paso_actual)
            paso_actual = padres[paso_actual]
        
        camino.reverse()
        aristas = list(zip(camino, camino[1:]))
        
    return grafo, niveles, camino, aristas

estado_inicial = (3, 3, 1)
estado_objetivo = (0, 0, 0)

G, niveles, camino_solucion, aristas_solucion = busqueda_bfs(estado_inicial, estado_objetivo)

fig, ax = plt.subplots(figsize=(16, 12), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

pos = {}
nodos_por_nivel = {}
for estado, nivel in niveles.items():
    if nivel not in nodos_por_nivel: nodos_por_nivel[nivel] = []
    nodos_por_nivel[nivel].append(estado)

for nivel, nodos in nodos_por_nivel.items():
    cantidad = len(nodos)
    desplazamiento_zigzag = 0.3 if nivel % 2 == 0 else -0.3
    
    for i, nodo in enumerate(nodos):
        x_pos = (i - (cantidad - 1) / 2) * 1.5 + desplazamiento_zigzag
        y_pos = -nivel * 1.0 
        pos[nodo] = (x_pos, y_pos)

etiquetas = {}
for nodo in G.nodes():
    etiquetas[nodo] = f"{nodo[0]}, {nodo[1]}, {nodo[2]}"

aristas_normales = []
for u, v in G.edges():
    if (u, v) in aristas_solucion or (v, u) in aristas_solucion:
        continue
    aristas_normales.append((u, v))

nx.draw_networkx_edges(G, pos, edgelist=aristas_normales, edge_color='#94a3b8', width=1.5, alpha=0.6)
nx.draw_networkx_edges(G, pos, edgelist=aristas_solucion, edge_color='#e53e3e', width=4.0)

nodos_normales = [n for n in G.nodes() if n not in [estado_inicial, estado_objetivo] and n not in camino_solucion]
nodos_camino = [n for n in camino_solucion if n not in [estado_inicial, estado_objetivo]]

nx.draw_networkx_nodes(G, pos, nodelist=nodos_normales, node_color='#e2e8f0', node_size=4800, edgecolors='#cbd5e1', linewidths=2)
nx.draw_networkx_nodes(G, pos, nodelist=nodos_camino, node_color='#fed7aa', node_size=4800, edgecolors='#ea580c', linewidths=2.5) 
nx.draw_networkx_nodes(G, pos, nodelist=[estado_inicial], node_color='#86efac', node_size=5500, edgecolors='#166534', linewidths=3) 
nx.draw_networkx_nodes(G, pos, nodelist=[estado_objetivo], node_color='#fde047', node_size=5500, edgecolors='#854d0e', linewidths=3) 

nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=14, font_family='sans-serif', font_weight='bold', font_color='#334155')

leyenda_elementos = [
    mpatches.Patch(color='#86efac', label='Estado Inicial'),
    mpatches.Patch(color='#fde047', label='Estado Objetivo (Meta)'),
    mpatches.Patch(color='#fed7aa', label='Nodos en Ruta Óptima'),
    mpatches.Patch(color='#e2e8f0', label='Otros Estados Válidos'),
    Line2D([0], [0], color='#e53e3e', lw=4, label='Camino de Solución'),
    Line2D([0], [0], color='#94a3b8', lw=1.5, label='Transición Válida')
]
plt.legend(handles=leyenda_elementos, loc='lower left', fontsize=11, frameon=True, shadow=True, facecolor='white')

plt.title("Espacio de Estados: Misioneros y Caníbales\n", fontsize=22, fontweight='bold', color='#1e293b')
plt.suptitle("Análisis de Búsqueda y Ruta Óptima", fontsize=16, color='#64748b', y=0.92)

plt.box(False)
plt.axis('off')

texto_explicativo = (
    "📝 FORMATO DEL NODO:  M, C, B\n"
    "------------------------------------------\n"
    "M = Misioneros en origen\n"
    "C = Caníbales en origen\n"
    "B = Barca (1=Origen | 0=Destino)"
)
plt.figtext(0.02, 0.96, texto_explicativo, wrap=True, horizontalalignment='left', verticalalignment='top', fontsize=12, 
            bbox={'facecolor': 'white', 'alpha': 0.9, 'pad': 10, 'edgecolor': '#cbd5e1', 'boxstyle': 'round,pad=0.5'})

plt.subplots_adjust(top=0.85, bottom=0.05)

plt.show()
