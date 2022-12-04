from Node import Node
import subprocess, os, platform


def choiceAlgorithm():
    print("1. BFS")
    print("2. DFS")
    print("3. Backtracking")
    print("4. Exit")
    print("Enter your choice: ", end="")
    choice = int(input())
    return choice


def choiceOrder():
    print("1. Ascendent order")
    print("2. Descendent order")
    print("Enter your choice: ", end="")
    choice = int(input())
    if choice == 1:
        return "asc"
    elif choice == 2:
        return "desc"
    else:
        print("Invalid choice")
        return choiceOrder()


def main():
    algorithm = choiceAlgorithm()
    order = choiceOrder()
    while choiceAlgorithm != 4:
        if algorithm == 1:
            print("BFS")
            node1 = Node([0, 0], order)
            print("Solution: ", str(node1.BFS(1)) + "\n")
            openGraph()
        elif algorithm == 2:
            print("DFS")
            node2 = Node([0, 0], order)
            print("Solution: ", str(node2.DFS(1)) + "\n")
            openGraph()
        elif algorithm == 3:
            print("Backtracking")
            node3 = Node([0, 0], order)
            print("Solution: " + str(node3.backtracking(1)) + "\n")
            openGraph()
        else:
            print("Invalid choice")
        algorithm = choiceAlgorithm()
        order = choiceOrder()


def openGraph():
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', "graph.dot"))
    elif platform.system() == 'Windows':  # Windows
        os.startfile("graph.dot")
    else:  # linux variants
        subprocess.call(('xdg-open', "graph.dot"))


if __name__ == '__main__':
    main()
