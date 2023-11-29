import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import cairosvg  # Asegúrate de que esta biblioteca esté instalada
import random


def generate_random_color(min_brightness=0.7):
    while True:
        r, g, b = [random.random() for _ in range(3)]
        brightness = (r * 299 + g * 587 + b * 114) / 1000  # Calculate brightness (Luma)
        if brightness >= min_brightness:
            return f'#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}'


# Define el gráfico de Rumania
romania_graph = nx.Graph()

# Agrega nodos con sus posiciones
romania_locations = {
    'Arad': (91, 492), 'Bucharest': (400, 327), 'Cracovia': (253, 288), 'Dobreta': (165, 299),
    'Efoire': (562, 293), 'Fagaras': (305, 449), 'Giurgiu': (375, 270), 'Hirsova': (534, 350),
    'Iasi': (473, 506), 'Lugoj': (165, 379), 'Medahia': (168, 339), 'Neamt': (406, 537),
    'Oradea': (131, 571), 'Pitesti': (320, 368), 'Rimicu': (233, 410), 'Sibiu': (207, 457),
    'Timisoara': (94, 410), 'Urziceni': (456, 350), 'Vaslui': (509, 444), 'Zerind': (108, 531)
}

romania_graph.add_nodes_from(romania_locations.keys())
nx.set_node_attributes(romania_graph, romania_locations, 'pos')

romania_edges = [
    ('Arad', 'Zerind', {'weight': 75}), ('Arad', 'Sibiu', {'weight': 140}), ('Arad', 'Timisoara', {'weight': 118}),
    ('Bucharest', 'Urziceni', {'weight': 85}), ('Bucharest', 'Pitesti', {'weight': 101}), ('Bucharest', 'Giurgiu', {'weight': 90}),
    ('Bucharest', 'Fagaras', {'weight': 211}), ('Cracovia', 'Dobreta', {'weight': 120}), ('Cracovia', 'Rimicu', {'weight': 146}),
    ('Cracovia', 'Pitesti', {'weight': 138}), ('Dobreta', 'Medahia', {'weight': 75}), ('Efoire', 'Hirsova', {'weight': 86}),
    ('Fagaras', 'Sibiu', {'weight': 99}), ('Hirsova', 'Urziceni', {'weight': 98}), ('Iasi', 'Vaslui', {'weight': 92}),
    ('Iasi', 'Neamt', {'weight': 87}), ('Lugoj', 'Timisoara', {'weight': 111}), ('Lugoj', 'Medahia', {'weight': 70}),
    ('Oradea', 'Zerind', {'weight': 71}), ('Oradea', 'Sibiu', {'weight': 151}), ('Pitesti', 'Rimicu', {'weight': 97}),
    ('Rimicu', 'Sibiu', {'weight': 80}), ('Urziceni', 'Vaslui', {'weight': 142})
]

romania_graph.add_edges_from(romania_edges)

# Dibuja el gráfico de Rumania
plt.figure(figsize=(10, 10))
pos = nx.get_node_attributes(romania_graph, 'pos')
labels = {node: node for node in romania_graph.nodes()}

random_node_colors = [generate_random_color() for _ in romania_graph.nodes()]
#label_positions = {k: (x, y - 10) for k, (x, y) in pos.items()}  # Adjust the '-10' for the desired displacement

nx.draw(romania_graph, pos, with_labels=False, labels=None, node_size=800, node_color=random_node_colors, font_size=12, font_weight='bold')
edge_labels = nx.get_edge_attributes(romania_graph, 'weight')
nx.draw_networkx_edge_labels(romania_graph, pos, edge_labels=edge_labels)

# Draw node labels with adjusted positions
nx.draw_networkx_labels(romania_graph, pos=pos, labels=labels, font_size=12, font_weight='bold')




#nx.draw(romania_graph, label_positions, with_labels=True, labels=labels, node_size=800, node_color=random_node_colors, font_size=12, font_weight='bold')
#edge_labels = nx.get_edge_attributes(romania_graph, 'weight')
#nx.draw_networkx_edge_labels(romania_graph, pos, edge_labels=edge_labels)

# Convierte la imagen SVG en PNG y agrega la bandera de Rumania como fondo
cairosvg.svg2png(url="https://upload.wikimedia.org/wikipedia/commons/7/73/Flag_of_Romania.svg", write_to="romania_flag.png")
flag_image = plt.imread("romania_flag.png")
imagebox = OffsetImage(flag_image, zoom=0.1)
ab = AnnotationBbox(imagebox, (0.5, 0.70), frameon=False, xycoords='axes fraction')
plt.gca().add_artist(ab)
plt.title("Mapa de Romania", fontsize=16, y=0.73)
# Add the second title with bold font
plt.text(330.5, 250.00, "ULPGC - 2023", fontsize=16, fontweight='bold', ha='center', va='center')
plt.text(330.5, 240.00, "Fundamentos de los Sistemas Inteligentes", fontsize=16, fontweight='bold', ha='center', va='center')
plt.text(330.5, 230.00, " ", fontsize=16, fontweight='bold', ha='center', va='center')


plt.show()
