import time

def simple_reflex_agent(room_name, state):
    """
    A simple reflex agent function.
    
    Args:
        room_name (str): The name of the room the agent is in. (Not used in this simple logic)
        state (str): The perceived state of the room ("Clean" or "Dirty").
        
    Returns:
        str: The action to take ("Clean" or "Move").
    """
    # Step 3: Reflex Agent Function
    if state == "Dirty":
        return "Clean"
    else:
        # Agent decides to move if the room is already clean.
        # The simulation loop will handle *where* it moves.
        return "Move"

def draw_grid(environment, agent_location):
    """
    Prints a visual representation of the 2x2 environment.
    
    Grid layout based on prompt:
    (0,1) | (1,1)  -> Room1 | Room2
    (0,0) | (1,0)  -> Room3 | Room4
    """
    
    # Helper to get status string, e.g., "Dirty"
    r1_status = environment["Room1"]
    r2_status = environment["Room2"]
    r3_status = environment["Room3"]
    r4_status = environment["Room4"]

    # Helper to place the agent marker "(A)"
    r1_agent = " (A) " if agent_location == "Room1" else "     "
    r2_agent = " (A) " if agent_location == "Room2" else "     "
    r3_agent = " (A) " if agent_location == "Room3" else "     "
    r4_agent = " (A) " if agent_location == "Room4" else "     "

    # Print the grid
    print("+" + "-"*18 + "+" + "-"*18 + "+")
    
    # Top Row: Room1 | Room2
    print(f"| {r1_status:<7} {r1_agent} | {r2_status:<7} {r2_agent} |")
    print(f"|      Room1       |      Room2       |")
    
    print("+" + "-"*18 + "+" + "-"*18 + "+")

    # Bottom Row: Room3 | Room4
    print(f"| {r3_status:<7} {r3_agent} | {r4_status:<7} {r4_agent} |")
    print(f"|      Room3       |      Room4       |")

    print("+" + "-"*18 + "+" + "-"*18 + "+")

def run_simulation(turns=8):
    """
    Runs the main simulation loop for the specified number of turns.
    """
    
    # Step 1: Define the 2x2 environment
    environment = {
        "Room1": "Clean",
        "Room2": "Dirty",  # Start with dirt here
        "Room3": "Clean",
        "Room4": "Clean"
    }
    
    # Agent's planned path. It will visit rooms in this order, then repeat.
    # This path matches the grid layout: Top-Left -> Top-Right -> Bottom-Right -> Bottom-Left
    room_path = ["Room1", "Room2", "Room4", "Room3"]
    
    print("--- Simple Reflex Agent Simulation ---")
    print("Initial Environment State:")
    # Show initial state, agent is not yet placed
    draw_grid(environment, agent_location=None)
    print(f"Agent will follow path: {' -> '.join(room_path)} -> ... and repeat.")

    # Step 6: Run simulation
    for i in range(turns):
        turn_number = i + 1
        
        # 1. Determine agent's location for this turn
        # Use (i % 4) to cycle through the room_path
        current_room = room_path[i % len(room_path)]
        
        print("\n" + "="*30)
        print(f"--- Turn {turn_number} ---")
        print(f"Agent is now in: {current_room}")

        # 2. Agent perceives the environment
        current_state = environment[current_room]
        print(f"Agent perceives state: {current_state}")

        # 3. Agent decides action
        action = simple_reflex_agent(current_room, current_state)
        print(f"Agent's action: {action}")

        # 4. Perform action and update environment
        if action == "Clean":
            environment[current_room] = "Clean"
            print(f"Environment updated: {current_room} is now Clean.")
        else:
            # Action is "Move"
            print("Room is clean. Agent will move to the next room on the next turn.")

        # 5. Draw the current state of the grid
        print("Environment State After Action:")
        draw_grid(environment, agent_location=current_room)
        
        # Pause for readability
        time.sleep(1)
        
    print("\n" + "="*30)
    print("--- Simulation End ---")
    print(f"Final environment state after {turns} turns:")
    draw_grid(environment, agent_location=None)

# --- Main execution ---
if __name__ == "__main__":
    run_simulation(turns=8)
