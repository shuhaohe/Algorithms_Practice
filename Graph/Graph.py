class Vertex(object):
    def __init__(self, element, degree=0):
        self.element = element
        self.degree = degree

    def __str__(self):
        return str(self.element)

    def __repr__(self):
        return self.__str__()


class Edge(object):
    def __init__(self, u, v, weight=0):
        """
        由于是无向图，所以在命名的时候就不叫origin和destination这种带方向含义的名字。
        :param weight:
        :param u:
        :param v:
        """
        self.weight = weight
        self.u = u
        self.v = v

    def __str__(self):
        return str(self.weight)

    def __repr__(self):
        return self.__str__()


class Graph(object):
    def __init__(self):
        self.vertexList = dict()

    def __getitem__(self, item):
        return self.vertexList[item]

    def __setitem__(self, key, value=[]):
        self.vertexList[key] = value

    def addVertex(self, vertex):
        if vertex in self.vertexList:
            return False

        self.vertexList[vertex] = []
        return True

    def addEdge(self, edge):
        u = edge.u
        v = edge.v

        if u not in self.vertexList:
            self.vertexList[u] = [v]
        else:
            self.vertexList[u].append(v)

        if v not in self.vertexList:
            self.vertexList[v] = [u]
        else:
            self.vertexList[v].append(u)

    def delVertex(self, vertex):
        if vertex in self.vertexList:
            del self.vertexList[vertex]

        for k, v in self.vertexList:
            if vertex in v:
                v.remove(vertex)

    def delEdge(self, edge):
        u, v = edge.u, edge.v
        if u in self.vertexList:
            if v in self.vertexList[u]:
                self.vertexList[u].remove(v)

        if v in self.vertexList:
            if u in self.vertexList[v]:
                self.vertexList[v].remove(u)

    def adj(self, vertex):
        return self.vertexList.get(vertex)

    @staticmethod
    def DFS_recursive(graph, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node, end=" ")

        for nextNode in graph.vertexList[start_node]:
            if nextNode not in visited:
                Graph.DFS_recursive(graph, nextNode, visited)
        return visited

    @staticmethod
    def DFS_non_recursive(graph, start_node):
        stack = [start_node]
        visited = set()
        while stack:  # not empty
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for next in graph.vertexList[node]:
                    if next not in visited:
                        stack.append(next)

        return visited


    @staticmethod
    def BFS_non_recursive(graph, start_node):
        visited = set()
        queue = [start_node]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node, end=" ")

            for nextNode in graph.vertexList[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
        print("\n")
        return visited


def main():
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addEdge(Edge(1,2))
    g.addEdge(Edge(1,3))
    g.addEdge(Edge(2,4))
    g.addEdge(Edge(3,4))
    g.addEdge(Edge(4,5))

    print("DFS")
    Graph.DFS_recursive(g, 1)
    print("\nBFS")
    Graph.BFS_non_recursive(g, 1)
    # pass

    g.delEdge(Edge(4,5))
    Graph.BFS_non_recursive(g, 1)

if __name__ == '__main__':
    main()




