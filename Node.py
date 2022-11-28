class Node:
    def __init__(self, start):
        self.estado = start
        self.capacidadeJarroA = 5
        self.capacidadeJarroB = 3
        self.visitados = []

    def encheA(self):
        if self.estado[0] < self.capacidadeJarroA and ([self.capacidadeJarroA, self.estado[1]] not in self.visitados):
            self.visitados.append([self.capacidadeJarroA, self.estado[1]])
            return [self.capacidadeJarroA, self.estado[1]]
        else:
            return None


    def encheB(self):
        if self.estado[1] < self.capacidadeJarroB and ([self.estado[0], self.capacidadeJarroB] not in self.visitados):
            self.visitados.append([self.estado[0], self.capacidadeJarroB])
            return [self.estado[0], self.capacidadeJarroB]
        else:
            return None

    def esvaziaA(self):
        if self.estado[0] > 0 and ([0, self.estado[1]] not in self.visitados):
            self.visitados.append([0, self.estado[1]])
            return [0, self.estado[1]]
        else:
            return None

    def esvaziaB(self):
        if self.estado[1] > 0 and ([self.estado[0], 0] not in self.visitados):
            self.visitados.append([self.estado[0], 0])
            return [self.estado[0], 0]
        else:
            return None

    def AparaB(self):
        if self.estado[0] > 0 and self.estado[1] < self.capacidadeJarroB:
            if self.estado[0] + self.estado[1] <= self.capacidadeJarroB:
                if ([0, self.estado[0] + self.estado[1]] not in self.visitados):
                    self.visitados.append([0, self.estado[0] + self.estado[1]])
                    return [0, self.estado[0] + self.estado[1]]
                else:
                    return None
            else:
                if ([self.estado[0] - (self.capacidadeJarroB - self.estado[1]), self.capacidadeJarroB] not in self.visitados):
                    self.visitados.append([self.estado[0] - (self.capacidadeJarroB - self.estado[1]), self.capacidadeJarroB])
                    return [self.estado[0] - (self.capacidadeJarroB - self.estado[1]), self.capacidadeJarroB]
                else:
                    return None
        else:
            return None

    def BparaA(self):
        if self.estado[1] > 0 and self.estado[0] < self.capacidadeJarroA:
            if self.estado[0] + self.estado[1] <= self.capacidadeJarroA:
                if ([self.estado[0] + self.estado[1], 0] not in self.visitados):
                    self.visitados.append([self.estado[0] + self.estado[1], 0])
                    return [self.estado[0] + self.estado[1], 0]
                else:
                    return None
            else:
                if ([self.capacidadeJarroA, self.estado[1] - (self.capacidadeJarroA - self.estado[0])] not in self.visitados):
                    self.visitados.append([self.capacidadeJarroA, self.estado[1] - (self.capacidadeJarroA - self.estado[0])])
                    return [self.capacidadeJarroA, self.estado[1] - (self.capacidadeJarroA - self.estado[0])]
                else:
                    return None
        else:
            return None

    def operadores(self):
        return [self.encheA(), self.encheB(), self.esvaziaA(), self.esvaziaB(), self.AparaB(), self.BparaA()]


    def BFS(self, objetivoY):
        queue = []
        queue.append([self.estado])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            y = node[1]

            if y == objetivoY:
                return path
            else:
                objEstado = Node(node)
                regras = objEstado.operadores()
                for i in regras:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        queue.append(newPath)

    def DFS(self, objetivoY):
        stack = []
        stack.append([self.estado])

        while stack:
            path = stack.pop()
            node = path[-1]
            y = node[1]

            if y == objetivoY:
                return path
            else:
                objEstado = Node(node)
                regras = objEstado.operadores()
                for i in regras:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)


    def backtracking(self, objetivoY):
        stack = []
        stack.append([self.estado])

        while stack:
            path = stack.pop()
            node = path[-1]
            y = node[1]

            if y == objetivoY:
                return path
            else:
                objEstado = Node(node)
                regras = objEstado.operadores()
                for i in regras:
                    if i and i not in path:
                        newPath = list(path)
                        newPath.append(i)
                        stack.append(newPath)
