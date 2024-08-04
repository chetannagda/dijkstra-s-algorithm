import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    pq = [(0, source)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

if __name__ == '__main__':
    try:
        num_nodes = int(input("Enter the number of nodes: "))
        graph = {node: {} for node in range(num_nodes)}

        for node in range(num_nodes):
            num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))
            for _ in range(num_neighbors):
                neighbor, weight = map(int, input(f"Enter neighbor and weight (space-separated) for node {node}: ").split())
                graph[node][neighbor] = weight

        source = int(input("Enter the source node: "))

        if source not in graph:
            raise ValueError("Source node does not exist in the graph.")

        distances = dijkstra(graph, source)

        print("Shortest distances from the source node:")
        for node, distance in distances.items():
            print(f"Node {node}: {distance}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")