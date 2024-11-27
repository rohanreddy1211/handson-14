import heapq


def dijkstra_algorithm(graph, source):
    """
    Dijkstra's algorithm to compute the shortest paths from a single source
    in a non-negative weighted graph.

    Args:
        graph (dict): A dictionary representing the graph as adjacency lists.
                      Each key is a vertex, and the value is a list of tuples (neighbor, weight).
        source (str): The starting vertex.

    Returns:
        tuple:
            - A dictionary of shortest distances from the source to each vertex.
            - A dictionary mapping each vertex to its predecessor in the shortest path.
    """
    # Priority queue to manage (distance, vertex)
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))

    # Initialize distances and predecessors
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if the current distance is greater than the recorded shortest distance
        if current_distance > distances[current_vertex]:
            continue

        # Process each neighboring vertex
        for neighbor, weight in graph[current_vertex]:
            new_distance = current_distance + weight

            # Update if a shorter path to the neighbor is found
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, predecessors


def reconstruct_path(predecessors, target):
    """
    Reconstructs the shortest path to the target using the predecessors dictionary.

    Args:
        predecessors (dict): A dictionary mapping each vertex to its predecessor.
        target (str): The target vertex.

    Returns:
        list: The reconstructed path as a list of vertices.
    """
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    return path


def display_results(distances, predecessors, source):
    """
    Displays the shortest distances and paths from the source vertex.

    Args:
        distances (dict): Dictionary of shortest distances from the source.
        predecessors (dict): Dictionary of predecessors for reconstructing paths.
        source (str): The source vertex.
    """
    print(f"Shortest distances from source '{source}':")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance if distance < float('inf') else '∞'}")

    print(f"\nShortest paths from source '{source}':")
    for vertex in distances:
        if distances[vertex] < float('inf'):
            path = reconstruct_path(predecessors, vertex)
            print(f"Path to {vertex}: {' -> '.join(path)}")
        else:
            print(f"Path to {vertex}: No path")


# Example graph definition
graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('C', 2), ('D', 6)],
    'C': [('B', 1), ('D', 4), ('E', 6)],
    'D': [('E', 2)],
    'E': [('A', 3), ('D', 7)],
}

# Run Dijkstra's algorithm
source = 'A'
distances, predecessors = dijkstra_algorithm(graph, source)

# Display results
display_results(distances, predecessors, source)
