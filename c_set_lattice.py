import networkx as nx
import matplotlib.pyplot as plt

# Definir el conjunto C
concepts = [
    ("O1", ["Escribible", "Leíble"]),
    ("O2", ["Escribible", "Leíble"]),
    ("O3", ["Escribible"]),
    ("O4", ["De medición"]),
    ("O5", ["Escribible"]),
    ("O6", ["Leíble"]),
    ("O7", ["Digital"]),
    ("O8", ["De medición", "De dibujo"]),
    ("O1,O2", ["Escribible", "Leíble"]),
    ("O1,O6", ["Leíble"]),
    ("O3,O5", ["Escribible"]),
    ("O4,O8", ["De medición"]),
    ("O1,O2,O6", ["Leíble"]),
    ("O1,O2,O3,O5", ["Escribible"]),
    ("O1,O2,O3,O4,O5,O6,O7,O8", []),
    ("∅", ["Escribible", "Leíble", "De medición", "Digital", "De dibujo"]),
]

# Crear un grafo dirigido para el lattice
G = nx.DiGraph()

# Añadir nodos al grafo con las etiquetas y niveles (subset_key)
levels = {
    0: 1,  # Nodo "O1"
    1: 1,  # Nodo "O2"
    2: 1,  # Nodo "O3"
    3: 1,  # Nodo "O4"
    4: 1,  # Nodo "O5"
    5: 1,  # Nodo "O6"
    6: 1,  # Nodo "O7"
    7: 1,  # Nodo "O8"
    8: 2,  # Nodo "O1,O2"
    9: 2,  # Nodo "O1,O6"
    10: 2,  # Nodo "O3,O5"
    11: 2,  # Nodo "O4,O8"
    12: 3,  # Nodo "O1,O2,O6"
    13: 3,  # Nodo "O1,O2,O3,O5"
    14: 4,  # Nodo "O1,O2,O3,O4,O5,O6,O7,O8"
    15: 5,  # Nodo "∅"
}

for i, (objects, attributes) in enumerate(concepts):
    label = f"({objects}; {', '.join(attributes) if attributes else '∅'})"
    G.add_node(i, label=label, subset_key=levels[i])

# Definir las relaciones jerárquicas (aristas) del lattice
edges = [
    (0, 8), (1, 8), (2, 10), (3, 11), (4, 10), (5, 9), (6, 14), (7, 11),
    (8, 12), (9, 12), (10, 13), (11, 12),
    (12, 14), (13, 14), (14, 15)
]
G.add_edges_from(edges)

# Dibujar el lattice usando niveles jerárquicos
pos = nx.multipartite_layout(G, subset_key="subset_key")
plt.figure(figsize=(12, 8))

# Dibujar nodos con etiquetas
labels = nx.get_node_attributes(G, "label")
nx.draw(
    G, pos, with_labels=True, labels=labels, node_size=3000, node_color="skyblue", 
    font_size=8, font_color="black", font_weight="bold", edge_color="gray", arrows=True
)

# Añadir título
plt.title("Látice de Conceptos con Elementos de C", fontsize=16)
plt.savefig('img/c_set_lattice.png')
plt.tight_layout()
plt.show()
