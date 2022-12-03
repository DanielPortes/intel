class Node:
    """A node state for water jug problem"""

    def __init__(self, start):
        self.state = start
        self.capacityJugA = 5
        self.capacityJugB = 3
        # self.visited = [self.state]
        # self.visited.extend(visited)

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

    def BFS(self, goal):
        """Breadth First Search"""
        queue = []
        queue.append([self.state])
        visited = []
        while queue:
            path = queue.pop(0)
            node = path[-1]
            jugA = node[0]

            if jugA == goal:
                return path
            else:
                myState = Node(node)
                listOfList = myState.applyOperators(visited)
                for i in listOfList:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)

    def DFS(self, goal):
        """Depth First Search"""
        stack = []
        stack.append([self.state])
        visited = []
        closed = []
        while stack:
            path = stack.pop()
            node = path[-1]
            jugA = node[0]

            if jugA == goal:
                print("open: ", stack)
                print("closed: ", closed)
                return path
            else:
                myState = Node(node)
                listOfList = myState.applyOperators(visited)
                for i in listOfList:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                closed.append(myState.state)
    print("")


    def backtracking(self, goal):
        """iterative Backtracking"""
        stack = []
        stack.append([self.state])
        closed = []
        while stack:
            path = stack.pop()
            node = path[-1]
            print("node: ", node)
            jugA = node[0]

            if jugA == goal:
                print("open: ", stack)
                print("closed: ", closed)
                return path
            else:
                myState = Node(node)
                listOfList = myState.applyOperators(visited=[])
                for i in listOfList:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
                        closed.append(myState.state)
                        break
