import matplotlib.pyplot as plt
import networkx as nx
import time

# Клас для вузла дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для вставки елементів у дерево з масиву у порядку рівнів
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

# Функція для генерації кольорів від темного до світлого
def generate_gradient_colors(num_colors):
    colors = []
    for i in range(num_colors):
        # Генерація кольору від темного (#000000) до світлого (#FFFFFF)
        intensity = int(255 * (i / (num_colors - 1)))
        color = f'#{intensity:02x}{intensity:02x}{intensity:02x}'
        colors.append(color)
    return colors

# Функція для малювання дерева та його оновлення на кожному кроці обходу
def draw_tree_with_colors(tree_root, visited_nodes, pos=None, node_colors=None):
    G = nx.Graph()
    nodes = []
    
    def add_edges(node):
        if not node:
            return
        nodes.append(node)
        if node.left:
            G.add_edge(node.value, node.left.value)
            add_edges(node.left)
        if node.right:
            G.add_edge(node.value, node.right.value)
            add_edges(node.right)
    
    add_edges(tree_root)

    if pos is None:
        pos = nx.spring_layout(G)
    
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=16, font_color='white')
    plt.pause(0.5)

# Візуалізація обходу в глибину (DFS)
def dfs(root):
    if not root:
        return
    stack = [root]
    visited = set()
    visited_nodes = []
    
    # Генерація градієнтних кольорів
    num_nodes = 6  # Приклад для 6 вузлів
    node_colors = ['#999999'] * num_nodes  # Сірі кольори для початкового стану
    gradient_colors = generate_gradient_colors(num_nodes)
    
    while stack:
        current = stack.pop()
        if current.value not in visited:
            visited.add(current.value)
            visited_nodes.append(current.value)
            
            # Присвоєння градієнтного кольору
            node_colors[visited_nodes.index(current.value)] = gradient_colors[len(visited_nodes) - 1]
            draw_tree_with_colors(root, visited_nodes, node_colors=node_colors)
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
    
    return visited_nodes

# Візуалізація обходу в ширину (BFS)
def bfs(root):
    if not root:
        return
    queue = [root]
    visited = set()
    visited_nodes = []
    
    # Генерація градієнтних кольорів
    num_nodes = 6  # Приклад для 6 вузлів
    node_colors = ['#999999'] * num_nodes  # Сірі кольори для початкового стану
    gradient_colors = generate_gradient_colors(num_nodes)
    
    while queue:
        current = queue.pop(0)
        if current.value not in visited:
            visited.add(current.value)
            visited_nodes.append(current.value)
            
            # Присвоєння градієнтного кольору
            node_colors[visited_nodes.index(current.value)] = gradient_colors[len(visited_nodes) - 1]
            draw_tree_with_colors(root, visited_nodes, node_colors=node_colors)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return visited_nodes

# Основний код для запуску
arr = [9, 8, 7, 2, 1, 4]  # Масив для побудови дерева
root = insert_level_order(arr, None, 0, len(arr))

# Показуємо обходи
plt.ion()  # Увімкнення інтерактивного режиму для графіків

print("Обхід у глибину (DFS):")
dfs(root)  # Візуалізація обходу в глибину

time.sleep(2)

print("Обхід у ширину (BFS):")
bfs(root)  # Візуалізація обходу в ширину

plt.ioff()  # Вимкнення інтерактивного режиму
plt.show()
