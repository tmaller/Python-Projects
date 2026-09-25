import matplotlib.pyplot as plt
import networkx as nx


def calcular_ruta_optima(red_conexiones, origen, destino, factor_costo=1.0):
  """Calcula la ruta más corta en un grafo ponderado aplicando un factor de costo variable."""
  G = nx.Graph()


  for u, v, peso_base in red_conexiones:
    peso_ajustado = (
        peso_base * factor_costo
    ) 
    G.add_edge(u, v, weight=peso_ajustado)

  
  if origen not in G or destino not in G:
    return None, None, f"Error: El origen o destino no existen en la red."


  ruta = nx.shortest_path(G, source=origen, target=destino, weight="weight")
  costo_total = nx.shortest_path_length(
      G, source=origen, target=destino, weight="weight"
  )

  return G, ruta, costo_total


#DEFINICIÓN DE VARIABLES DEL SISTEMA


conexiones_base = [
    ("Depósito Central", "Sucursal Norte", 12),
    ("Depósito Central", "Sucursal Oeste", 15),
    ("Sucursal Norte", "Cliente A", 8),
    ("Sucursal Norte", "Cliente B", 20),
    ("Sucursal Oeste", "Cliente B", 10),
    ("Sucursal Oeste", "Sucursal Sur", 7),
    ("Cliente B", "Cliente Final", 5),
    ("Sucursal Sur", "Cliente Final", 14),
]


punto_origen = "Depósito Central"
punto_destino = "Cliente Final"


factor_congestion = 1.0


#EJECUCIÓN DEL MODELO
G, ruta_optima, costo_total = calcular_ruta_optima(
    conexiones_base, punto_origen, punto_destino, factor_congestion
)

if isinstance(ruta_optima, list):
  print(f"--- SIMULACIÓN DE LOGÍSTICA (Factor: {factor_congestion}) ---")
  print(f"Ruta óptima: {' -> '.join(ruta_optima)}")
  print(f"Costo operativo total: {costo_total:.2f} unidades")

  #VISUALIZACIÓN GRÁFICA
  plt.figure(figsize=(10, 6))
  pos = nx.spring_layout(G, seed=42)


  nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=2500)
  nx.draw_networkx_edges(G, pos, edge_color="gray", width=2)
  nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")


  labels_peso = {
      (u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)
  }
  nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_peso)

  
  edges_en_ruta = list(zip(ruta_optima[:-1], ruta_optima[1:]))
  nx.draw_networkx_edges(
      G, pos, edgelist=edges_en_ruta, edge_color="crimson", width=4
  )

  plt.title(
      f"Optimizador Logístico Dinámico\nDe {punto_origen} a {punto_destino}"
      f" (Factor de Costo: {factor_congestion})",
      fontsize=11,
  )
  plt.axis("off")
  plt.tight_layout()
  plt.show()
else:
  print(costo_total)
