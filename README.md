# Formal Concept Analysis (FCA) - C2466-CM0246

Este proyecto implementa el Análisis Formal de Conceptos (FCA) para la clase **C2466-CM0246-1939**, mostrando el proceso de construcción de un conjunto de conceptos formales y la representación gráfica de sus relaciones jerárquicas en un lattice de conceptos.

## Paso 1: Selección de Objetos y Atributos

Definimos un conjunto de **objetos** y sus correspondientes **atributos**. Estos objetos y atributos representan un contexto formal para el análisis.

- **Objetos**:

  - O1: "Libro de Ciencia"
  - O2: "Cuaderno"
  - O3: "Bolígrafo"
  - O4: "Regla"
  - O5: "Lápiz"
  - O6: "Libro de Matemáticas"
  - O7: "Calculadora"
  - O8: "Compás"

- **Atributos**:
  - A1: "Escribible"
  - A2: "Leíble"
  - A3: "De medición"
  - A4: "Digital"
  - A5: "De dibujo"

## Paso 2: Descripción del Contexto Formal

La descripción de cada objeto con sus atributos se detalla a continuación:

- **O1** ("Libro de Ciencia") - Atributos: Leíble
- **O2** ("Cuaderno") - Atributos: Escribible, Leíble
- **O3** ("Bolígrafo") - Atributos: Escribible
- **O4** ("Regla") - Atributos: De medición
- **O5** ("Lápiz") - Atributos: Escribible
- **O6** ("Libro de Matemáticas") - Atributos: Leíble
- **O7** ("Calculadora") - Atributos: Digital
- **O8** ("Compás") - Atributos: De medición, De dibujo

Esta información se presenta en formato de tabla, donde cada celda indica la presencia (1) o ausencia (0) de un atributo en cada objeto.

| Vista Tabular                         |
| ------------------------------------- |
| ![Tabular View](img/tabular_view.png) |

## Paso 3: Conjunto de Conceptos Formales \( C \)

Cada concepto formal \( C \) consiste en un **conjunto de objetos** (extensión) y un **conjunto de atributos** compartidos (intensión). A continuación, algunos conceptos formales extraídos del contexto:

1. **C1**: Extensión: {O1, O2, O6}, Intensión: {Leíble}
2. **C2**: Extensión: {O2}, Intensión: {Escribible, Leíble}
3. **C3**: Extensión: {O3, O5}, Intensión: {Escribible}
4. **C4**: Extensión: {O4}, Intensión: {De medición}
5. **C5**: Extensión: {O7}, Intensión: {Digital}
6. **C6**: Extensión: {O8}, Intensión: {De medición, De dibujo}
7. **C7**: Extensión: {O4, O8}, Intensión: {De medición}

## Paso 4: Relación de Orden Parcial

La relación de orden parcial establece una jerarquía de subconjuntos entre las extensiones e intensiones de los conceptos formales. Los conceptos específicos, que comparten más atributos, se colocan en niveles inferiores de la jerarquía, mientras que los conceptos generales, con menos atributos, están en niveles superiores.

1. **C1 ≤ C2**: {O2} es un subconjunto de {O1, O2, O6} y {Escribible, Leíble} ⊆ {Leíble}.
2. **C4 ≤ C7**: {O4} ⊆ {O4, O8} y {De medición} ⊆ {De medición}.

## Paso 5: Representación Gráfica del Lattice de Conceptos

La estructura jerárquica de los conceptos se visualiza en un **lattice de conceptos** donde cada nodo representa un concepto formal, y las conexiones muestran las relaciones de inclusión.

En el lattice:

- **C0** representa el concepto vacío en la parte superior.
- Los nodos están etiquetados con el conjunto de atributos o el conjunto de objetos que representan, destacando las relaciones de subconjunto.

## Visualización Completa

La tabla de contexto formal y el lattice de conceptos permiten una mejor comprensión del análisis de los datos. A continuación, se muestran ambas representaciones generadas mediante el código en Python.

| Vista del Látice                      |
| ------------------------------------- |
| ![Lattice View](img/lattice_view.png) |

| Vista Tabular                         |
| ------------------------------------- |
| ![Tabular View](img/tabular_view.png) |
