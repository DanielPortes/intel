import glob
import os
import platform
import subprocess
import sys
import datetime
from Node import Node


def choiceAlgorithm():
    print("1. BFS")
    print("2. DFS")
    print("3. Backtracking")
    print("4. Uniform Cost Search")
    print("5. Greedy Search")
    print("6. A* Search")
    print("7. Exit")
    print("Enter your choice: ", end="")
    choice = int(input())
    return choice


def choiceOrder():
    print("1. Ascendant order")
    print("2. Descendent order")
    print("Enter your choice: ", end="")
    choice = int(input())
    if choice == 1:
        return "Ascendant"
    elif choice == 2:
        return "Descendent"
    else:
        print("Invalid choice")
        return choiceOrder()


def main():
    while True:
        algorithm = choiceAlgorithm()
        if algorithm == 7:
            sys.exit()
        order = choiceOrder()
        node = Node([0, 0], order)
        if algorithm == 1:
            print("BFS")
            print("Solution: ", str(node.BFS(1)) + "\n")
        elif algorithm == 2:
            print("DFS")
            print("Solution: ", str(node.DFS(1)) + "\n")
        elif algorithm == 3:
            print("Backtracking")
            print("Solution: " + str(node.backtracking(1)) + "\n")
        elif algorithm == 4:
            print("Uniform Cost Search")
            print("Solution: " + str(node.uniformCostSearch(1)) + "\n")
        elif algorithm == 5:
            print("Greedy Search")
            print("Solution: " + str(node.GreedySearchy(1)) + "\n")
        elif algorithm == 6:
            print("A* Search")
            print("Solution: " + str(node.AStarSearch(1)) + "\n")
        openGraph()


def openGraph():
    dotGraph = getLastestFile()
    imageGraph = dotGraph.replace(".dot", ".png")
    command = " dot -Tpng " + dotGraph + " -o " + imageGraph
    os.system(command)
    try:
        if platform.system() == 'Darwin':
            subprocess.call(('xdg-open', dotGraph))
            subprocess.call(('xdg-open', imageGraph))

        elif platform.system() == 'Windows':
            os.startfile(dotGraph)
            os.startfile(imageGraph)

        else:
            subprocess.call(('open', dotGraph))
            subprocess.call(('open', imageGraph))
    except OSError:
        print("\nWARNING:\t Was not possible to open the graph\n")


def getLastestFile():
    list_of_files = glob.glob('./output/*.dot')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


if __name__ == '__main__':

    message = f"""NOTE: the graph file created is like .output/graph_{datetime.datetime.today():_%m-%d__%H-%M-%S}.dot
NOTE: if installed graphviz, the graph is also generated in the file with the same name + .png
 
Optional arguments:
  -s    to not open the graph after create it
  -h2   to change the heuristic function
  -c2   to change the real cost function\n"""

    print(message)

    if len(sys.argv) > 1:
        if sys.argv[1] == "-s":
            openGraph = lambda: None

    main()
