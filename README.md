# Python-Projects
# Optimizador de Rutas en Python 🚚

Armé este pequeño script para resolver un problema clásico de logística: encontrar la ruta más eficiente dentro de una red de distribución (depósitos, sucursales y clientes) usando teoría de grafos y el algoritmo de Dijkstra. 

Lo copado de este proyecto es que no solo calcula el camino óptimo, sino que le agregué un factor de costo y tráfico variable para ver cómo se reconfigura la red ante imprevistos. Además, te genera un gráfico visual con `Matplotlib` donde se resalta claramente la ruta elegida en rojo.

## 🛠️ ¿Qué tecnologías usé?
* **Python** como base principal.
* **NetworkX** para armar y procesar la red de nodos.
* **Matplotlib** para armar la visualización gráfica.

## 🚀 Cómo correrlo en tu compu
Si quieres probarlo, es súper sencillo:

1. Asegúrate de tener Python instalado.
2. Instala las librerías necesarias ejecutando esto en tu terminal:
   ```bash
   pip install networkx matplotlib
