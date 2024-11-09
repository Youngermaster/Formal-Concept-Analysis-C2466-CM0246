from fcapy.context import FormalContext
from fcapy.lattice import ConceptLattice
import matplotlib.pyplot as plt
from fcapy.visualizer import LineVizNx

# Paso 1: Crear el contexto formal directamente sin pandas
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

# Imprimir el contexto para verificar
print("Contexto Formal:")
print(K)

# Paso 2: Crear el lattice de conceptos

# Generar el lattice de conceptos desde el contexto formal
L = ConceptLattice.from_context(K)

# Imprimir el número de conceptos y sus extremos (más general y más específico)
print("\nNúmero de conceptos:", len(L))
print("Índices del concepto más general y más específico:", L.top, L.bottom)

# Paso 3: Visualización gráfica del lattice de conceptos

# Crear la visualización del lattice usando el visualizador integrado en FCApy
fig, ax = plt.subplots(figsize=(10, 6))
visualizer = LineVizNx()
visualizer.draw_concept_lattice(L, ax=ax, flg_node_indices=True)

# Ajustes y título para la gráfica
ax.set_title("Lattice de Conceptos", fontsize=18)
plt.tight_layout()
plt.show()
