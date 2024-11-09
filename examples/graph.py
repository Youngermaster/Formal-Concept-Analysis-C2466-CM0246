import seaborn as sns
import matplotlib.pyplot as plt
from fcapy.context import FormalContext
from fcapy.lattice import ConceptLattice
from fcapy.visualizer import LineVizNx

# Definir los objetos y atributos de manera directa en una lista de listas con valores booleanos
data = [
    [True, True, False, False, False],
    [True, True, False, False, False],
    [True, False, False, False, False],
    [False, False, True, False, False],
    [True, False, False, False, False],
    [False, True, False, False, False],
    [False, False, False, True, False],
    [False, False, True, False, True]
]
objects = ["Libro de Ciencia", "Cuaderno", "Bolígrafo", "Regla", "Lápiz", "Libro de Matemáticas", "Calculadora", "Compás"]
attributes = ["Escribible", "Leíble", "De medición", "Digital", "De dibujo"]

# Crear el contexto formal
K = FormalContext(data, objects, attributes)

# Convertir a DataFrame para visualización
import pandas as pd
df = pd.DataFrame(data, index=objects, columns=attributes)

# Visualizar el contexto formal como heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap="YlGnBu", cbar_kws={'label': 'Presencia de relación'})
plt.title("Contexto Formal")
plt.xlabel("Atributos")
plt.ylabel("Objetos")
plt.savefig('img/tabular_view.png')
# plt.show()

# Generar el lattice de conceptos desde el contexto formal
L = ConceptLattice.from_context(K)

# Visualización del lattice con etiquetas y colores personalizados
fig, ax = plt.subplots(figsize=(10, 6))
visualizer = LineVizNx()

# Dibujar el lattice y activar etiquetas de nodos
visualizer.draw_concept_lattice(L, ax=ax, flg_node_indices=True)

# Añadir título y leyenda
ax.set_title("Lattice de Conceptos con Etiquetas", fontsize=18)
plt.tight_layout()
plt.savefig('img/lattice_view.png')
plt.show()
