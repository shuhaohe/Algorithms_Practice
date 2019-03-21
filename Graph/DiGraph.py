# Directed Graph
class DiEdge(object):
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination



class DiGraph(object):
    def __init__(self, vertexNum=0):
        self.vertexNum = vertexNum
        self.edgeNum = 0

        # adj list
        self.graph = {}
        for i in range(vertexNum):
            self.graph[i] = []

    def addVertex(self, vertex):
        self.vertexNum += 1

        # 不允许添加相同的节点。
        if vertex in self.graph:
            return None
        self.graph[vertex] = []

    def addEdge(self, edge):
        orig, dest = edge.origin, edge.destination
        if orig not in self.graph:
            self.graph[orig] = [dest]
        else:
            self.graph[orig].append(dest)
            self.edgeNum += 1

    def delEdge(self, edge):
        orig, dest = edge.origin, edge.destination
        if orig not in self.graph:
            return False
        self.graph[orig].remove(dest)
        self.edgeNum -= 1
        return True

    def delVertex(self, vertex):
        if vertex not in self.graph:
            return False

        # 删除所有以vertex为origin的边
        numOfEdgeFromVertex = len(self.graph[vertex])
        del self.graph[vertex]
        self.vertexNum -= 1
        self.edgeNum -= numOfEdgeFromVertex

        # 删除所有以vertex为destination的边
        for k, v in self.graph:
            if vertex in v:
                v.remove(vertex)
                self.edgeNum -= 1

        return True

    def adj(self, vertex):
        """
        返回以vertex出发的所有边的destination节点，也就是所谓的邻接点。
        :param vertex:
        :return:
        """
        if vertex not in self.graph:
            return None
        return self.graph[vertex]


class DirectedDFS(object):
    def __init__(self, s):
        pass

    def marked(self):
        pass


class DirectedCircle(object):
    pass


class Topologic(object):
    pass



