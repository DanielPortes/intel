from Node import Node

if __name__ == '__main__':
    print("BFS")
    node = Node([0, 0])
    print(node.BFS(1))

    print("DFS")
    node = Node([0, 0])
    print(node.DFS(1))

    print("Backtracking")
    node = Node([0, 0])
    print(node.backtracking(1))

