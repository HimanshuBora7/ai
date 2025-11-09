import heapq

def best_first_search(graph, heuristic, start, goal):
    """
    Finds a path from start to goal using Greedy Best-First Search.

    Args:
        graph (dict): An adjacency list of the graph.
        heuristic (dict): A dictionary mapping nodes to their heuristic value (e.g., h(n)).
        start (str): The starting node.
        goal (str): The target/goal node.

    Returns:
        list: A list representing the path from start to goal if found.
        None: If no path is found.
    """
    
    # Step 1: Initialize an empty Priority Queue (pq).
    # We will store tuples: (heuristic_value, node, path_to_node)
    pq = []
    
    # Set to keep track of visited nodes to avoid cycles and re-adding
    visited = set()

    # Step 2: Insert the starting node into pq.
    # The evaluation function for Greedy BFS is just the heuristic h(n).
    start_heuristic = heuristic[start]
    heapq.heappush(pq, (start_heuristic, start, [start]))
    
    # Mark the start node as visited (per step 3.3, on insertion)
    visited.add(start)
    
    print(f"Starting Best-First Search from '{start}' to find '{goal}'...")
    print("-" * 40)

    # Step 3: While pq is not empty:
    while pq:
        # 1. Remove the node u with the lowest evaluation value from pq.
        (h_value, current_node, current_path) = heapq.heappop(pq)
        
        print(f"Popped: {current_node} (h={h_value}) | Path: {' -> '.join(current_path)}")

        # 2. If u is the goal node, terminate the search.
        if current_node == goal:
            print(f"\nGoal '{goal}' reached!")
            return current_path
        
        # 3. Otherwise, for each neighbor v of u:
        # (Step 4, "Mark u as examined", is implicitly done by popping it
        # and not adding it back.)
        
        for neighbor in graph[current_node]:
            # If v has not been visited:
            if neighbor not in visited:
                # Mark v as visited
                visited.add(neighbor)
                
                # Insert v into pq.
                neighbor_heuristic = heuristic[neighbor]
                new_path = current_path + [neighbor]
                heapq.heappush(pq, (neighbor_heuristic, neighbor, new_path))
                print(f"  -> Adding {neighbor} (h={neighbor_heuristic}) to priority queue.")

    # Step 4: End the procedure (pq became empty).
    print(f"\nPriority queue is empty. Goal '{goal}' not found.")
    return None

# --- Main execution ---
if __name__ == "__main__":
    
    # Example: A simplified graph of Romanian cities
    romania_graph = {
        'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
        'Zerind': ['Arad', 'Oradea'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
        'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']
    }
    
    # Heuristic: Straight-line distance to Bucharest
    heuristic_to_bucharest = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
        'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
        'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
        'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }
    
    start_node = 'Arad'
    goal_node = 'Bucharest'
    
    # Run the Best-First Search
    path = best_first_search(romania_graph, heuristic_to_bucharest, start_node, goal_node)
    
    print("-" * 40)
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")
