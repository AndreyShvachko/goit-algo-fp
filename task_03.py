import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)] 

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        #якщо існує кращий шлях до вершини, пропускаємо
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            #якщо є коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances [neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
        
        return distance
    
graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
}
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print("Найкоротші шляхи від вершини", start_vertex, ":", shortest_paths)