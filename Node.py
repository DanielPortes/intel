import os
import sys
from datetime import datetime


def timestamp():
    return datetime.now().strftime('_%m-%d__%H-%M-%S')


def printLists(open, closed, current, cost=None):
    print("open: ", open)
    print("closed: ", closed)
    print("current: ", current)
    if cost:
        print("cost: ", cost)


def getFirstLetters(string):
    return ''.join([word[0] for word in string.split()])


class Node:
    """A node state for water jug problem"""

    def __init__(self, start, order):
        self.state = start
        self.capacityJugA = 5
        self.capacityJugB = 3

        self.orderRules = order

    def fillA(self, visited):
        if self.state[0] < self.capacityJugA and ([self.capacityJugA, self.state[1]] not in visited):
            visited.append([self.capacityJugA, self.state[1]])
            return [self.capacityJugA, self.state[1]]
        else:
            return None

    def fillB(self, visited):
        if self.state[1] < self.capacityJugB and ([self.state[0], self.capacityJugB] not in visited):
            visited.append([self.state[0], self.capacityJugB])
            return [self.state[0], self.capacityJugB]
        else:
            return None

    def emptyA(self, visited):
        if self.state[0] > 0 and ([0, self.state[1]] not in visited):
            visited.append([0, self.state[1]])
            return [0, self.state[1]]
        else:
            return None

    def emptyB(self, visited):
        if self.state[1] > 0 and ([self.state[0], 0] not in visited):
            visited.append([self.state[0], 0])
            return [self.state[0], 0]
        else:
            return None

    def pourAtoB(self, visited):
        if self.state[0] > 0 and self.state[1] < self.capacityJugB:
            if self.state[0] + self.state[1] <= self.capacityJugB:
                if [0, self.state[0] + self.state[1]] not in visited:
                    visited.append([0, self.state[0] + self.state[1]])
                    return [0, self.state[0] + self.state[1]]
                else:
                    return None
            else:
                if [self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB] not in visited:
                    visited.append([self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB])
                    return [self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB]
                else:
                    return None
        else:
            return None

    def pourBtoA(self, visited):
        if self.state[1] > 0 and self.state[0] < self.capacityJugA:
            if self.state[0] + self.state[1] <= self.capacityJugA:
                if [self.state[0] + self.state[1], 0] not in visited:
                    visited.append([self.state[0] + self.state[1], 0])
                    return [self.state[0] + self.state[1], 0]
                else:
                    return None
            else:
                if [self.capacityJugA, self.state[1] - (self.capacityJugA - self.state[0])] not in visited:
                    visited.append([self.capacityJugA, self.state[1] - (self.capacityJugA - self.state[0])])
                    return [self.capacityJugA, self.state[1] - (self.capacityJugA - self.state[0])]
                else:
                    return None
        else:
            return None

    def applyOperators(self, visited):
        return [self.fillA(visited), self.fillB(visited), self.emptyA(visited), self.emptyB(visited),
                self.pourAtoB(visited), self.pourBtoA(visited)]

    def writeSolutionToFile(self, path):
        self.file.write("\n\tsubgraph Solution {\n")
        for i in path:
            self.file.write("\t" + str(i[0]) + "." + str(i[1]) + " [color=red];\n")
        self.file.write("\t}\n}\n")
        self.file.close()

    def createGraphvizFile(self, title):
        if not os.path.exists("output"):
            os.makedirs("output")

        self.file = open(
            "./output/graph" + "-(" + getFirstLetters(title) + "," + self.orderRules + ")" + str(timestamp()) + ".dot",
            "w")
        self.file.write('strict graph G {\n')
        self.file.write("labelloc=\"t\";\n"
                        "label=\"" + title + ": " + self.orderRules + "\";\n\n")

    def BFS(self, goal):
        """Breadth First Search"""
        self.createGraphvizFile("Breadth First Search")
        queue = [[self.state]]
        visited = []
        closed = []
        open = [[self.state]]
        current = []
        while queue:
            path = queue.pop(0)
            node = path[-1]
            jugA = node[0]

            open.pop(0)
            current.append(node)

            if jugA == goal:
                printLists(open, closed, current)
                self.writeSolutionToFile(path)

                return path
            else:
                myState = Node(node, self.orderRules)
                states = myState.applyOperators(visited)
                states = self.applyReorderningRules(states)
                for i in states:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)
                        open.append(i)
                        self.writeEdgesToGraphviz(node, i, states.index(i))
                closed.append(myState.state)

    def applyReorderningRules(self, listOfList):
        if not (self.orderRules == "Ascendant"):
            listOfList.reverse()
        return listOfList

    def DFS(self, goal):
        """Depth First Search"""
        self.createGraphvizFile("Depth First Search")
        stack = []
        stack.append([self.state])
        visited = []
        closed = []
        open = [[self.state]]
        current = []
        while stack:
            path = stack.pop()
            open.pop()
            node = path[-1]
            jugA = node[0]
            current.append(node)

            if jugA == goal:
                printLists(open, closed, current)
                self.writeSolutionToFile(path)
                return path
            else:
                myState = Node(node, self.orderRules)
                listOp = myState.applyOperators(visited)
                listOp = self.applyReorderningRules(listOp)
                for i in listOp:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                        open.append(i)
                        self.writeEdgesToGraphviz(node, i, listOp.index(i))
                closed.append(myState.state)

    def backtracking(self, goal):
        """iterative Backtracking"""
        self.createGraphvizFile("Iterative Backtracking")
        stack = []
        stack.append([self.state])
        closed = []
        current = []
        while stack:
            path = stack.pop()
            node = path[-1]
            jugA = node[0]
            current.append(node)
            if jugA == goal:
                printLists(stack, closed, current)
                self.writeSolutionToFile(path)
                return path
            else:
                myState = Node(node, self.orderRules)
                listOp = myState.applyOperators(visited=[])
                listOp = self.applyReorderningRules(listOp)
                for i in listOp:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                        closed.append(myState.state)
                        self.writeEdgesToGraphviz(node, i, listOp.index(i))
                        break

    def writeEdgesToGraphviz(self, nodeA, nodeB, index):
        valueAToWrite = str(nodeA[0]) + "." + str(nodeA[1])
        valueBToWrite = str(nodeB[0]) + "." + str(nodeB[1])
        if self.orderRules == "Ascendant":
            corretRuleValue = (str(index + 1))
        else:
            corretRuleValue = str(6 - index)
        self.file.write(valueAToWrite + ' -- ' + valueBToWrite + "[label= R" + corretRuleValue + "];\n")

    def realCost(self, path):
        if len(sys.argv) > 1:
            if "-c2" in sys.argv:
                return self.costAlt(path)
        return self.cost(path)

    def cost(self, path):
        cost = 0
        for i in path[1:]:
            cost += abs(i[0] - 1)
        return cost

    def costAlt(self, path):
        cost = 0
        for i in path[1:]:
            cost += abs(i[0] + i[1] - 1)
        return cost

    def heValues(self, path):
        if len(sys.argv) > 1:
            if "-h2" in sys.argv:
                return self.heuristicAlt(path)
        return self.heuristic(path)

    def heuristic(self, path):
        heuristic = abs(5 - path[-1][0]) + abs(3 - path[-1][1])
        return heuristic

    def heuristicAlt(self, path):
        heuristic = abs(5 - path[-1][0] + 1) + abs(3 - path[-1][1] + 1)
        return heuristic

    def uniformCostSearch(self, goal):
        """Uniform Cost Search"""
        self.createGraphvizFile("Uniform Cost Search")
        queue = [[self.state]]
        visited = []
        closed = []
        open = [[self.state]]
        current = []

        while queue:
            path = queue.pop(0)
            open.pop(0)
            state = path[-1]
            jugA = state[0]
            current.append(state)
            if jugA == goal:
                printLists(open, closed, current, self.realCost(path))
                self.writeSolutionToFile(path)
                return path
            else:
                currentState = Node(state, self.orderRules)
                states = currentState.applyOperators(visited)
                states = self.applyReorderningRules(states)

                for i in states:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)
                        open.append(i)
                        self.writeEdgesToGraphviz(state, i, states.index(i))
                queue = sorted(queue, key=lambda path: self.realCost(path))
                closed.append(currentState.state)

    def GreedySearchy(self, goal):
        """Greedy Search"""
        self.createGraphvizFile("Greedy Search")
        queue = []
        queue.append([self.state])
        visited = []
        closed = []
        open = [[self.state]]
        current = []

        while queue:
            path = queue.pop(0)
            open.pop(0)
            state = path[-1]
            jugA = state[0]
            current.append(state)

            if jugA == goal:
                printLists(open, closed, current, self.realCost(path))
                self.writeSolutionToFile(path)
                return path
            else:
                currentState = Node(state, self.orderRules)
                states = currentState.applyOperators(visited)
                states = self.applyReorderningRules(states)

                for i in states:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)
                        open.append(i)
                        self.writeEdgesToGraphviz(state, i, states.index(i))

                queue = sorted(queue, key=lambda path: self.heValues(path))
                closed.append(currentState.state)

    def AStarSearch(self, goal):
        """A* Search"""
        self.createGraphvizFile("A* Search")
        queue = []
        queue.append([self.state])
        visited = []
        closed = []
        open = [[self.state]]
        current = []

        while queue:
            path = queue.pop(0)
            open.pop(0)
            state = path[-1]
            jugA = state[0]
            current.append(state)

            if jugA == goal:
                printLists(open, closed, current, self.realCost(path))
                self.writeSolutionToFile(path)
                return path
            else:
                currentState = Node(state, self.orderRules)
                states = currentState.applyOperators(visited)
                states = self.applyReorderningRules(states)

                for i in states:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)
                        open.append(i)
                        self.writeEdgesToGraphviz(state, i, states.index(i))

                queue = sorted(queue, key=lambda path: (self.realCost(path)) + self.heValues(path))
                closed.append(currentState.state)
