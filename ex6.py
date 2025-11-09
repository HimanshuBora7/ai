def is_valid(region, color, solution, neighbors):
    """
    Step 5: Function to check if the current color assignment is valid.
    
    Checks if assigning 'color' to 'region' conflicts with any
    already-colored neighbors.
    """
    for neighbor in neighbors[region]:
        # Check if the neighbor is already colored
        if neighbor in solution:
            # If the neighbor has the same color, this is invalid
            if solution[neighbor] == color:
                return False
    # No conflicts found
    return True

def solve_csp_recursive(regions, colors, neighbors, solution):
    """
    Step 6: Backtracking function (recursive part).
    
    Tries to find a valid coloring for all regions.
    """
    
    # Base case: If all regions are in the solution, we are done
    if len(solution) == len(regions):
        return True # Solution found

    # Step 7: Select an unassigned region
    # Find the first region in the list that is not yet in the solution
    region = None
    for r in regions:
        if r not in solution:
            region = r
            break
    
    # If region is still None, something is wrong (should be caught by base case)
    if region is None:
        return True # Should not be hit if base case is correct

    # Try each color from the domain
    for color in colors:
        # Check if this color assignment is valid
        if is_valid(region, color, solution, neighbors):
            
            # Assign the color
            solution[region] = color
            print(f"  -> Trying: {region} --> {color} (Current Solution: {len(solution)}/{len(regions)})")

            # Step 8: Recursive call for the next region
            if solve_csp_recursive(regions, colors, neighbors, solution):
                return True # Success, propagate it up

            # Step 9: Backtrack
            # If the recursive call failed, undo the assignment
            print(f"  -> BACKTRACK: Removing {region} --> {color}")
            del solution[region]

    # If all colors were tried and none worked, return False
    return False

def solve_map_coloring(neighbors, colors):
    """
    Step 10: Start solving.
    This function sets up and kicks off the recursive solver.
    """
    regions = list(neighbors.keys())
    solution = {} # This dictionary will store the final coloring
    
    print("--- Starting CSP Backtracking Solver ---")
    if solve_csp_recursive(regions, colors, neighbors, solution):
        return solution
    else:
        return None

# --- Main execution ---
if __name__ == "__main__":
    
    # Step 3: Define the map (neighbors)
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []  # Tasmania has no neighbors
    }

    # Step 4: Define the colors (domain)
    colors = ['Red', 'Green', 'Blue']

    # Solve the problem
    solution = solve_map_coloring(neighbors, colors)

    print("\n" + "="*40)
    # Display result
    if solution:
        print("Solution found:")
        # Sort by region name for consistent output
        for region in sorted(solution.keys()):
            color = solution[region]
            print(f"{region} --> {color}")
    else:
        print("No solution exists.")
