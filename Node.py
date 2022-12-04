class Node:
    """A node state for water jug problem"""

    def __init__(self, start, order):
        self.state = start
        self.capacityJugA = 5
        self.capacityJugB = 3

        self.ascendingOrder = order
        self.ascendingOrder.lower()
        # pura gambiarra isso, nao consegui fazer dentro de cada metodo, erro de 'compilacao'
        self.file = open('graph.dot', 'w')
        self.file.write('strict graph G {\n')

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
                if ([0, self.state[0] + self.state[1]] not in visited):
                    visited.append([0, self.state[0] + self.state[1]])
                    return [0, self.state[0] + self.state[1]]
                else:
                    return None
            else:
                if ([self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB] not in visited):
                    visited.append([self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB])
                    return [self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB]
                else:
                    return None
        else:
            return None

    def pourBtoA(self, visited):
        if self.state[1] > 0 and self.state[0] < self.capacityJugA:
            if self.state[0] + self.state[1] <= self.capacityJugA:
                if ([self.state[0] + self.state[1], 0] not in visited):
                    visited.append([self.state[0] + self.state[1], 0])
                    return [self.state[0] + self.state[1], 0]
                else:
                    return None
            else:
                if ([self.capacityJugA, self.state[1] - (self.capacityJugA - self.state[0])] not in visited):
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
        self.file.write("subgraph Solution {\n")
        for i in path:
            self.file.write(str(i[0]) + "." + str(i[1]) + " [color=red];\n")
        self.file.write("}\n")
    def BFS(self, goal):
        """Breadth First Search"""
        queue = []
        queue.append([self.state])
        visited = []
        closed = []
        open = [[self.state]]
        current = []
        while queue:
            path = queue.pop(0)
            open.pop(0)
            node = path[-1]
            jugA = node[0]
            current.append(node)

            if jugA == goal:
                print("open: ", open)
                print("closed: ", closed)
                print("current: ", current)
                self.writeSolutionToFile(path)
                self.file.write('}')
                self.file.close()
                return path
            else:
                myState = Node(node, self.ascendingOrder)
                listOp = myState.applyOperators(visited)
                listOp = self.applyReorderningRules(listOp)
                for i in listOp:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)
                        open.append(i)
                        self.writeEdges(node, i, listOp.index(i))
                closed.append(myState.state)

    def applyReorderningRules(self, listOfList):
        if not (self.ascendingOrder == "asc"):
            listOfList.reverse()
        return listOfList

    def DFS(self, goal):
        """Depth First Search"""

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
                print("open: ", open)
                print("closed: ", closed)
                print("current: ", current)
                self.writeSolutionToFile(path)
                self.file.write('}')
                self.file.close()
                return path
            else:
                myState = Node(node, self.ascendingOrder)
                listOp = myState.applyOperators(visited)
                listOp = self.applyReorderningRules(listOp)
                for i in listOp:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                        open.append(i)
                        self.writeEdges(node, i, listOp.index(i))
                closed.append(myState.state)

    print("")

    def backtracking(self, goal):
        """iterative Backtracking"""
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
                print("open: ", stack)
                print("closed: ", closed)
                print("current: ", current)
                self.writeSolutionToFile(path)
                self.file.write('}')
                self.file.close()
                return path
            else:
                myState = Node(node, self.ascendingOrder)
                listOp = myState.applyOperators(visited=[])
                listOp = self.applyReorderningRules(listOp)
                for i in listOp:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                        closed.append(myState.state)
                        self.writeEdges(node, i, listOp.index(i))
                        break

    def writeEdges(self, nodeA, nodeB, index):
        valueAToWrite = str(nodeA[0]) + "." + str(nodeA[1])
        valueBToWrite = str(nodeB[0]) + "." + str(nodeB[1])
        if self.ascendingOrder == "asc":
            corretRuleValue = (str(index + 1))
        else:
            corretRuleValue = str(6 - index)
        self.file.write(valueAToWrite + ' -- ' + valueBToWrite + "[label= R" + corretRuleValue + "];\n")

