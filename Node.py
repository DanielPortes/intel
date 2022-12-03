class Node:
    """A node state for water jug problem"""
    def __init__(self, start):
        self.state = start
        self.capacityJugA = 5
        self.capacityJugB = 3
        self.visited = [[self.state]]

    def fillA(self):
        if self.state[0] < self.capacityJugA and ([self.capacityJugA, self.state[1]] not in self.visited):
            self.visited.append([self.capacityJugA, self.state[1]])
            return [self.capacityJugA, self.state[1]]
        else:
            return None


    def fillB(self):
        if self.state[1] < self.capacityJugB and ([self.state[0], self.capacityJugB] not in self.visited):
            self.visited.append([self.state[0], self.capacityJugB])
            return [self.state[0], self.capacityJugB]
        else:
            return None

    def emptyA(self):
        if self.state[0] > 0 and ([0, self.state[1]] not in self.visited):
            self.visited.append([0, self.state[1]])
            return [0, self.state[1]]
        else:
            return None

    def emptyB(self):
        if self.state[1] > 0 and ([self.state[0], 0] not in self.visited):
            self.visited.append([self.state[0], 0])
            return [self.state[0], 0]
        else:
            return None

    def pourAtoB(self):
        if self.state[0] > 0 and self.state[1] < self.capacityJugB:
            if self.state[0] + self.state[1] <= self.capacityJugB:
                if ([0, self.state[0] + self.state[1]] not in self.visited):
                    self.visited.append([0, self.state[0] + self.state[1]])
                    return [0, self.state[0] + self.state[1]]
                else:
                    return None
            else:
                if ([self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB] not in self.visited):
                    self.visited.append([self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB])
                    return [self.state[0] - (self.capacityJugB - self.state[1]), self.capacityJugB]
                else:
                    return None
        else:
            return None

    def pourBtoA(self):
        if self.state[1] > 0 and self.state[0] < self.capacityJugA:
            if self.state[0] + self.state[1] <= self.capacityJugA:
                if ([self.state[0] + self.state[1], 0] not in self.visited):
                    self.visited.append([self.state[0] + self.state[1], 0])
                    return [self.state[0] + self.state[1], 0]
                else:
                    return None
            else:
                if ([self.capacityJugA, self.state[1] - (self.capacityJugA - self.state[0])] not in self.visited):
                    self.visited.append([self.capacityJugA, self.state[1] - (self.capacityJugA - self.state[0])])
                    return [self.capacityJugA, self.state[1] - (self.capacityJugA - self.state[0])]
                else:
                    return None
        else:
            return None

    def applyOperators(self):
        return [self.fillA(), self.fillB(), self.emptyA(), self.emptyB(), self.pourAtoB(), self.pourBtoA()]


    def BFS(self, goal):
        """Breadth First Search"""
        queue = []
        queue.append([self.state])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            jugA = node[0]

            if jugA == goal:
                return path
            else:
                myState = Node(node)
                listOfList = myState.applyOperators()
                for i in listOfList:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)

    def DFS(self, goal):
        """Depth First Search"""
        stack = []
        stack.append([self.state])

        while stack:
            path = stack.pop()
            node = path[-1]
            jugA = node[0]

            if jugA == goal:
                return path
            else:
                myState = Node(node)
                listOfList = myState.applyOperators()
                for i in listOfList:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)


    def backtracking(self, goal):
        """iterative Backtracking"""
        stack = []
        stack.append([self.state])

        while stack:
            path = stack.pop()
            node = path[-1]
            jugA = node[0]

            if jugA == goal:
                return path
            else:
                myState = Node(node)
                listOfList = myState.applyOperators()
                for i in listOfList:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                        break

    def backtracking2(self, goal):
        """testando backtracking"""
        stack = []
        stack.append([self.state])

        while stack:
            path = stack.pop()
            lastState = path[-1]
            jugA = lastState[0]

            if jugA == goal:
                return path
            else:
                listOfList = self.applyOperators() # para a funcao funcionar tem que alterar a logica das regras, remover o self.visited.append delas e colocar aqui
                for i in listOfList:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                        self.visited.append(i) # substituindo por esse append aqui
                        self.state = i
                        break
