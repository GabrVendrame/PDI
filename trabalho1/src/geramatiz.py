import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.colors import hsv_to_rgb

# Cria um grid de valores de matiz
h = np.linspace(0, 1, 360)

# Cria a figura e o subplot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')

# Desenha um círculo para representar a matiz
circle = plt.Circle((0.5, 0.5), 0.4, color='white', ec='none')
ax.add_artist(circle)

# Adiciona os setores de cunha coloridos para representar as matizes
for i in range(len(h)):
    theta1 = (90 - i) % 360
    theta2 = (91 - i) % 360
    wedge = Wedge((0.5, 0.5), 0.4, theta1, theta2, edgecolor='none', facecolor=hsv_to_rgb([h[i], 1, 1]))
    ax.add_artist(wedge)

# Adiciona os valores dos ângulos na parte de fora do círculo com alinhamento horizontal
for angle in range(0, 360, 30):  # Ângulos a serem rotulados
    x = 0.5 + 0.45 * np.cos(np.radians(90 - angle))
    y = 0.5 + 0.45 * np.sin(np.radians(90 - angle))
    ax.text(x, y, f'{angle}°', ha='center', va='center', fontsize=10, rotation=0)

# Remove os eixos
ax.set_xticks([])
ax.set_yticks([])

# Espelha horizontalmente a imagem
ax.invert_xaxis()

# Salva a imagem em um arquivo .png
plt.savefig('matiz_hsv.png', dpi=300, bbox_inches='tight', pad_inches=0)

# Fecha a figura
plt.close()