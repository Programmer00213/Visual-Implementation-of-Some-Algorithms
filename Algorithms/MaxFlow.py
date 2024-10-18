from collections import deque
from Utility.Utility import GRAPH2
import pygame

GRAPH = GRAPH2

#BFS
def Breadth_First_Search(Residual_Graph, source, sink, parent):
    visited = [False] * len(Residual_Graph)
    queue = deque([source])
    visited[source] = True

    while queue: # Run as long as queue is not empty
        vertex = queue.popleft() # Dequeue the first element (Vertex)
        
        for i in range(len(Residual_Graph)):
            if Residual_Graph[vertex][i] != 0 and not visited[i]:

                parent[i] = vertex

                if i == sink: return True

                queue.append(i)
                visited[i] = True

    return False

# Ford_Fulkerson
def Max_Flow(source, sink, screen,  Graph = GRAPH.MATRIX):
    
    Residual_Graph = [row[:] for row in Graph]
    parent = [-1] * len(Graph)
    max_Flow = 0

    while Breadth_First_Search(Residual_Graph, source, sink, parent):
        path_Flow = float('INF')
        s = sink
        for i in range(len(parent)):
            pygame.draw.line(screen, GRAPH.PATH_HIGHLIGHT_COLOR, GRAPH.VERTEX_COORDINATE[parent[s]], GRAPH.VERTEX_COORDINATE[s], 5)
        while s != source:
            u = parent[s]
            path_Flow = min(path_Flow, Residual_Graph[u][s])
            s = parent[s]

        s = sink
        while s != source:
            u = parent[s]
            Residual_Graph[u][s] -= path_Flow
            Residual_Graph[s][u] += path_Flow
            s = parent[s]

        max_Flow += path_Flow

    return max_Flow



