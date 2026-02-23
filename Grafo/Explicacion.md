# Acertijo de los Misioneros y Caníbales

## Representación de Estados
Para modelar este problema matemáticamente, definimos cada estado como un trio de  valores: **`(M, C, B)`**.

Este trio representa la cantidad de elementos presentes en la **orilla de origen** (el lado inicial del río):
* **M:** Número de misioneros en el origen (0 ≤ M ≤ 3).
* **C:** Número de caníbales en el origen (0 ≤ C ≤ 3).
* **B:** Posición de la barca (1 = en el origen, 0 = en el destino).

> **Estado Inicial:** `(3, 3, 1)` (Tres misioneros, tres caníbales y la barca están en la orilla de origen).

##  Definición de Acciones y Restricciones
Las acciones son los viajes en la barca de una orilla a la otra. Las mostramos como la cantidad de personas que se suben a la barca `(m, c)`:
* `(1, 0)`:  1 misionero.
* `(2, 0)`:  2 misioneros.
* `(0, 1)`:  1 caníbal.
* `(0, 2)`:  2 caníbales.
* `(1, 1)`:  1 misionero y 1 caníbal.

**Restricción de Seguridad (Estado Válido):** Una acción solo es válida si el estado resultante cumple que, en **ambas orillas**, si hay al menos un misionero, el número de misioneros debe ser mayor o igual al número de caníbales. Hay que aclarar que la barca siempre debe llevar al menos 1 persona y máximo 2, no se mueve sola.

## Grafo de Espacio de Soluciones
El espacio de soluciones se construye modelando los estados como **nodos** y las acciones válidas como **aristas** (transiciones) entre ellos. 
Dado que cualquier viaje de ida puede deshacerse con un viaje de vuelta idéntico, el grafo es **no direccionado**. Al expandir todos los estados válidos desde el estado inicial sin repetir estados previamente visitados en la misma rama, se genera elgrafo de búsqueda. Ver y correr codigo de python

> **Estado Objetivo (Meta):** `(0, 0, 0)`

## Búsqueda y Solución (Ruta Óptima)
Para encontrar la solución se implementó el algoritmo de **Búsqueda en Anchura (BFS - Breadth-First Search)** porque el problema es muy chiquito, o bueno, la cantidad de estados posibles es muy pequena.

Se eligió BFS porque explora el grafo nivel por nivel, lo que permite encontrar la mejor solucion (el camino con el menor número de viajes en barca) en grafos no ponderados.

**Camino Encontrado (11 viajes):**
A continuación, se detalla la secuencia de estados desde el inicio hasta la meta:

1.  **`(3, 3, 1)`** - *Estado Inicial*
2.  **`(3, 1, 0)`** - (Viajan 2 caníbales al destino)
3.  **`(3, 2, 1)`** - (Regresa 1 caníbal al origen)
4.  **`(3, 0, 0)`** - (Viajan 2 caníbales al destino)
5.  **`(3, 1, 1)`** - (Regresa 1 caníbal al origen)
6.  **`(1, 1, 0)`** - (Viajan 2 misioneros al destino)
7.  **`(2, 2, 1)`** - (Regresan 1 misionero y 1 caníbal al origen)
8.  **`(0, 2, 0)`** - (Viajan 2 misioneros al destino)
9.  **`(0, 3, 1)`** - (Regresa 1 caníbal al origen)
10. **`(0, 1, 0)`** - (Viajan 2 caníbales al destino)
11. **`(0, 2, 1)`** - (Regresa 1 caníbal al origen)
12. **`(0, 0, 0)`** - (Viajan 2 caníbales al destino) -> *Nadie Murioooo!*




## Cómo correr el código
Python instalado. Abrir  terminal e instalar las dos librerías requeridas:

```bash
pip install networkx matplotlib

py Grafo.py



