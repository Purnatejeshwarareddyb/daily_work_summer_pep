def has_cycle(graph):
    """
    Detects if a directed graph contains a cycle using DFS.
    The graph parameter is a dictionary acting as an adjacency list.
    Returns True if a cycle is found, otherwise False.
    """
    # Track nodes that are fully processed
    visited = set()
    # Track nodes in the current DFS recursive path
    rec_stack = set()

    def dfs(node):
        # Add node to both sets when entering
        visited.add(node)
        rec_stack.add(node)
        
        # Check all neighboring connections
        for neighbor in graph.get(node, []):
            # If neighbor is in the current execution path, a cycle exists
            if neighbor in rec_stack:
                return True
            # If neighbor hasn't been visited yet, recurse into it
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
                    
        # Remove the node from the recursion stack before backtracking
        rec_stack.remove(node)
        return False

    # Outer loop to handle disconnected components/graphs
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
                
    return False


# ==========================================
# INPUT EXAMPLES & TEST CASES
# ==========================================

# Example 1: Graph WITH a cycle (A -> B -> C -> A)
graph_with_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],  # This edge closes the loop back to A
    'D': ['E']
}

# Example 2: Graph WITHOUT a cycle (Directed Acyclic Graph - DAG)
graph_without_cycle = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []      # Paths terminate here safely
}

# Example 3: Disconnected components where one part contains a cycle
graph_disconnected_with_cycle = {
    '1': ['2'],
    '2': [],
    '3': ['4'],
    '4': ['5'],
    '5': ['3']   # Cycle exists in the secondary cluster (3 -> 4 -> 5 -> 3)
}

# Execution and verification
print("--- Cycle Detection Results ---")
print(f"Test 1 (Should be True):  {has_cycle(graph_with_cycle)}")
print(f"Test 2 (Should be False): {has_cycle(graph_without_cycle)}")
print(f"Test 3 (Should be True):  {has_cycle(graph_disconnected_with_cycle)}")
