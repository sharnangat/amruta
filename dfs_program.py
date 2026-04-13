"""
Depth First Search (DFS) Program in Python
"""


def dfs_recursive(graph, node, visited, result):
    visited.add(node)
    result.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)


def dfs(graph, start_node):
    if start_node not in graph:
        return []

    visited = set()
    result = []
    dfs_recursive(graph, start_node, visited, result)
    return result


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    print("Graph:", graph)
    start = input("Enter start node (example: A): ").strip().upper()
    traversal = dfs(graph, start)

    if not traversal:
        print("Start node not found in graph.")
    else:
        print("DFS Traversal:", " -> ".join(traversal))


if __name__ == "__main__":
    main()
