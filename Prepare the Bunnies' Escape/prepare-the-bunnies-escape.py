def solution(map):
    # A* using Manhattan distance with 1 optional removal of a wall
    
    # Determine the coordinates of the door
    door = (len(map) - 1, len(map[0]) - 1)
    
    # Set to keep track of visited nodes
    visited = set()
    
    # Initialize the queue with the starting node (0, 0)
    queue = [[True, 1, (0, 0)]]
    
    # While the queue is not empty
    while queue:
        # Get the next element from the queue
        e = queue.pop(0)
        
        # Extract the removal flag, steps, and node coordinates from the element
        removal, steps, node = e[0], e[1], e[2]
        
        # If the node (under removal state) has already been visited, continue to the next iteration
        if (removal, node) in visited:
            continue
        
        # Mark the current node as visited
        visited.add((removal, node))
        
        # Explore the neighboring nodes in all four directions
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = node[0] + dy, node[1] + dx
            
            # Check if the neighboring node is within the bounds of the map
            if 0 <= ny <= door[0] and 0 <= nx <= door[1]:
                # If the neighboring node is the door, return steps + 1
                if (ny, nx) == door:
                    return steps + 1
                # If the neighboring node is empty, add it to the queue with the same removal flag and incremented steps
                elif map[ny][nx] == 0:
                    queue += [[removal, steps + 1, (ny, nx)]]
                # If the neighboring node is a wall and removal is allowed, add it to the queue with removal flag set to False
                elif removal:
                    queue += [[False, steps + 1, (ny, nx)]]
        
        # Sort the queue based on steps + Manhattan distance heuristic
        queue = sorted(queue, key=lambda x: x[1] + door[0] - x[2][0] + door[1] - x[2][1] + 1)
    
    # If the door is unreachable, return None or an appropriate value indicating that.
    return None
