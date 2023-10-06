import heapq
from collections import defaultdict


def dijkstra(graph, start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    visited = set()
    heap = [(0, start)]

    while heap:
        (distance, current_node) = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance_to_neighbor = distance + weight
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                heapq.heappush(heap, (distance_to_neighbor, neighbor))

    return distances
