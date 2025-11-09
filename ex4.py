def dfs_path(graph, start, goal):
    """
    Finds a path from start to goal using iterative Depth-First Search (DFS).

    Args:
        graph (dict): An adjacency list representation of the graph.
        start (str): The starting node.
        goal (str): The target/goal node.

    Returns:
        list: A list representing the path from start to goal if found.
        None: If no path is found.
    """
    
    # Step 1: Initialize
    # The stack will store tuples of (node, path_to_this_node)
    stack = [(start, [start])]
    
    # Keep a visited set to avoid cycles and redundant work
    visited = set()

    print(f"Starting DFS from '{start}' to find '{goal}'...")
    print("-" * 30)
    
    # Step 2: Loop until stack is empty
    while stack:
        # Pop the top node and its path
        (current_node, current_path) = stack.pop()
        
        print(f"Popped: {current_node} | Path: {' -> '.join(current_path)}")

        # If this node is the goal, we are done
        if current_node == goal:
            print(f"\nGoal '{goal}' reached!")
            return current_path

        # If not visited yet:
        if current_node not in visited:
            # Mark it as visited
            visited.add(current_node)
            print(f"  -> Marking {current_node} as visited.")

            # Get all neighbors
            neighbors = graph[current_node]
            
            # Push all its unvisited neighbors onto the stack
            # We iterate in reverse to maintain the "left-to-right"
            # exploration order (e.g., 'B' will be on top of 'C' for 'A')
            print(f"  -> Neighbors of {current_node}: {neighbors}")
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    # Create the new path for this neighbor
                    new_path = current_path + [neighbor]
                    stack.append((neighbor, new_path))
                    print(f"  -> Pushing {neighbor} to stack.")
        else:
            print(f"  -> {current_node} already visited, skipping.")

    # Step 3: Return result (failure)
    # If the loop finishes, the stack is empty and goal was not found
    print(f"\nStack is empty. Goal '{goal}' not found.")
    return None

# --- Main execution ---
if __name__ == "__main__":
    # Graph from the prompt
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    start_node = 'A'
    goal_node = 'F'
    
    # Run the DFS
    path = dfs_path(graph, start_node, goal_node)
    
    print("-" * 30)
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}.")
        
    print("\n--- Example 2: No Path ---")
    # Example where no path exists
    start_node_2 = 'D'
    goal_node_2 = 'A'
    path_2 = dfs_path(graph, start_node_2, goal_node_2)
    print("-" * 30)
    if path_2:
        print(f"Path found: {' -> '.join(path_2)}")
    else:
        print(f"No path found from {start_node_2} to {goal_node_2}.")
