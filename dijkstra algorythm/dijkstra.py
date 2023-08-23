import heapq


def dijkstra(graph, start):
    # Initializing distances with infinity and the distance of the start vertex with 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue for the vertices
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Check if the current distance is less than the previously recorded distance
        if current_distance > distances[current_vertex]:
            continue

        # Iterating through the connected vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If the calculated distance is less than the previously recorded distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(distances)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
