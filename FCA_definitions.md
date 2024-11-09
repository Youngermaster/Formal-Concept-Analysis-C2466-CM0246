# Ejemplo de Análisis Formal de Conceptos (FCA)

## Paso 1: Seleccionar un conjunto de objetos con sus atributos

Supongamos que tenemos un conjunto de objetos (productos) y un conjunto de atributos que describen algunas de sus características. Aquí hay un ejemplo:

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

## Paso 2: Descripción por extensión del conjunto de objetos con sus atributos

Aquí detallamos cada objeto con los atributos que posee:

- **O1** ("Libro de Ciencia") - Atributos: A2
- **O2** ("Cuaderno") - Atributos: A1, A2
- **O3** ("Bolígrafo") - Atributos: A1
- **O4** ("Regla") - Atributos: A3
- **O5** ("Lápiz") - Atributos: A1
- **O6** ("Libro de Matemáticas") - Atributos: A2
- **O7** ("Calculadora") - Atributos: A4
- **O8** ("Compás") - Atributos: A5, A3

## Paso 3: Crear el conjunto de conceptos formales \( C \)

Cada concepto formal está compuesto por un conjunto de objetos (extensión) y un conjunto de atributos compartidos (intensión). A continuación, construimos algunos conceptos formales \( C \) para este conjunto:

1. **C1**: Extensión: {O1, O2, O6}, Intensión: {A2}
2. **C2**: Extensión: {O2}, Intensión: {A1, A2}
3. **C3**: Extensión: {O3, O5}, Intensión: {A1}
4. **C4**: Extensión: {O4}, Intensión: {A3}
5. **C5**: Extensión: {O7}, Intensión: {A4}
6. **C6**: Extensión: {O8}, Intensión: {A5, A3}
7. **C7**: Extensión: {O4, O8}, Intensión: {A3} (Concepto con atributos de medición)

## Paso 4: Definir la relación de orden parcial

La relación de orden parcial se establece mediante la inclusión de subconjuntos entre extensiones e intensiones. Aquí, se representará una jerarquía donde los conceptos más específicos (con más atributos) estarán en niveles inferiores, mientras que los más generales estarán en niveles superiores.

1. **C1 ≤ C2**: {O2} es un subconjunto de {O1, O2, O6} y {A1, A2} ⊆ {A2}.
2. **C4 ≤ C7**: {O4} ⊆ {O4, O8} y {A3} ⊆ {A3}.

## Paso 5: Representación gráfica de los nodos del Lattice

La representación gráfica del lattice organiza los conceptos formales en un diagrama en el que se puede observar la relación jerárquica entre los conceptos. Este lattice tendría una estructura similar a la siguiente:

```
       C0
      / | \
    C3 C4 C1
     |   |   \
     C2   C7   C6
```

Aquí:

- **C0** representa el concepto vacío (sin atributos ni objetos) en la parte superior.
- **C2** representa un concepto que solo tiene {O2} y atributos {A1, A2}.
- **C7** representa un concepto intermedio con objetos de medición.

## Paso 6: Asignar las etiquetas a cada nodo

Finalmente, asignamos etiquetas a cada nodo con base en los objetos o atributos. Usualmente, los nodos se etiquetan con el atributo distintivo o conjunto de atributos. Ejemplo de etiquetado:

- **Nodo C1**: "Leíble" (ya que agrupa los objetos que tienen el atributo "Leíble" - A2).
- **Nodo C3**: "Escribible" (agrupa objetos con el atributo "Escribible" - A1).
- **Nodo C4**: "De medición" (agrupa objetos con el atributo "De medición" - A3).
- **Nodo C7**: "De dibujo y medición" (agrupa el objeto "Compás", que es tanto de medición como de dibujo).
