def rec_helper(node, visited, adj):
    if node in visited:
        return visited
    visited.append(node)
    for neighbor in adj[node]:
        visited = rec_helper(neighbor, visited, adj)
    return visited

def rec_dfs(start, adj):
    visited = rec_helper(start, [], adj)
    print(visited)