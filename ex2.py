from collections import deque

def solve_water_jug(capacity1, capacity2, target):
    """
    Solves the water jug problem using Breadth-First Search (BFS).

    Args:
        capacity1 (int): The capacity of the first jug.
        capacity2 (int): The capacity of the second jug.
        target (int): The target amount of water to reach.

    Returns:
        tuple: A tuple (goal_state, path_info) where:
               - goal_state is the state (j1, j2) that contains the target.
               - path_info is a dictionary mapping each state to its
                 (parent_state, action_taken) tuple.
               Returns (None, None) if no solution is found.
    """
    
    # Queue for BFS, storing states (jug1_amount, jug2_amount)
    queue = deque([(0, 0)])
    
    # Set to keep track of visited states to avoid cycles
    visited = {(0, 0)}
    
    # Dictionary to reconstruct the path
    # Key: (j1, j2) state
    # Value: (parent_state, action_description)
    path_info = {(0, 0): (None, "Start")}

    while queue:
        # Get the current state
        current_j1, current_j2 = queue.popleft()

        # Check if we've reached the target
        if current_j1 == target or current_j2 == target:
            return (current_j1, current_j2), path_info

        # --- Generate all possible next states ---
        
        states_and_actions = []

        # 1. Fill Jug1
        states_and_actions.append(
            ((capacity1, current_j2), f"Fill Jug1 to {capacity1}L")
        )
        
        # 2. Fill Jug2
        states_and_actions.append(
            ((current_j1, capacity2), f"Fill Jug2 to {capacity2}L")
        )
        
        # 3. Empty Jug1
        states_and_actions.append(
            ((0, current_j2), "Empty Jug1")
        )
        
        # 4. Empty Jug2
        states_and_actions.append(
            ((current_j1, 0), "Empty Jug2")
        )
        
        # 5. Pour Jug1 to Jug2
        pour_amount_j1_to_j2 = min(current_j1, capacity2 - current_j2)
        states_and_actions.append(
            (
                (current_j1 - pour_amount_j1_to_j2, current_j2 + pour_amount_j1_to_j2),
                f"Pour {pour_amount_j1_to_j2}L from Jug1 to Jug2"
            )
        )
        
        # 6. Pour Jug2 to Jug1
        pour_amount_j2_to_j1 = min(current_j2, capacity1 - current_j1)
        states_and_actions.append(
            (
                (current_j1 + pour_amount_j2_to_j1, current_j2 - pour_amount_j2_to_j1),
                f"Pour {pour_amount_j2_to_j1}L from Jug2 to Jug1"
            )
        )

        # --- Process new states ---
        for new_state, action in states_and_actions:
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)
                path_info[new_state] = ((current_j1, current_j2), action)
                
    # If the queue becomes empty and no solution was found
    return None, None

def print_solution(capacity1, capacity2, target):
    """
    Finds and prints the solution steps.
    """
    print("####################################")
    print(f"Capacities: Jug1={capacity1}L, Jug2={capacity2}L | Target: {target}L")
    print()

    goal_state, path_info = solve_water_jug(capacity1, capacity2, target)
    
    if not goal_state:
        print("No solution found.")
        print("####################################")
        return

    # Reconstruct the path from the goal state
    path = []
    current_state = goal_state
    
    while current_state is not None:
        parent, action = path_info[current_state]
        path.append((current_state, action))
        current_state = parent
        
    # Reverse the path to go from start to end
    path.reverse()

    # Print the steps
    start_state, _ = path[0]
    print(f"Start: Jug1={start_state[0]}L, Jug2={start_state[1]}L")
    
    for i, (state, action) in enumerate(path[1:], 1):
        j1, j2 = state
        # Use formatting to align the output as in the example
        print(f"{i:02d}. {action:<28} -> State: (Jug1={j1}L, Jug2={j2}L)")

    print()
    print(f"Reached target: Jug1={goal_state[0]}L, Jug2={goal_state[1]}L")
    print("####################################")


# --- Example Run ---
if __name__ == "__main__":
    # Classic problem: 4L jug, 3L jug, target 2L
    print_solution(4, 3, 2)
    
    print("\n")
    
    # Another example: 5L jug, 3L jug, target 4L
    print_solution(5, 3, 4)
