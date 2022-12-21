from Node import Node
import subprocess, os, platform

def choiceAlgorithm():
    print("1. BFS")
    print("2. DFS")
    print("3. Backtracking")
    print("4. Uniform Cost Search")
    print("5. Exit")
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
    while True:
        algorithm = choiceAlgorithm()
        order = choiceOrder()
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
        elif algorithm == 4:
            print("Uniform Cost Search")
            node4 = Node([0, 0], order)
            print("Solution: " + str(node4.uniformCostSearch(1)) + "\n")
            openGraph()
        else:
            break



def openGraph():
    command = " dot -Tpng graph.dot -o graph.png"
    res = os.system(command)
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', "graph.dot"))
        if os.path.isfile("graph.png"):
            subprocess.call(('open', "graph.png"))
    elif platform.system() == 'Windows':  # Windows
        os.startfile("graph.dot")
        if os.path.isfile("graph.png"):
            os.startfile("graph.png")
    else:  # linux variants
        subprocess.call(('xdg-open', "graph.dot"))
        if os.path.isfile("graph.png"):
            subprocess.call(('xdg-open', "graph.png"))

    print(res)


if __name__ == '__main__':
    print("NOTE: the graph generated is in the file graph.dot")
    print("NOTE: if installed graphviz, the graph is also generated in the file graph.png")
    main()
