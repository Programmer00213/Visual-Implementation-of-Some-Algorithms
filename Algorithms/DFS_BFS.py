from collections import deque
import pygame
from Utility.Utility import GRAPH2

GRAPH = GRAPH2
VERTEX = GRAPH.VERTEX_COORDINATE

DFS = []
BFS = []

def Depth_First_Search(GRAPH, visited, start): # Depth_First_Search is also called "Backtracking" Recursive Version
    visited[start] = True

    for i in range(len(GRAPH)):
        if GRAPH[start][i] != 0 and not visited[i]:
            DFS.append([start, i])
            Depth_First_Search(GRAPH, visited, i)

visited = [False]*len(VERTEX)

Depth_First_Search(GRAPH.MATRIX, visited, 2)

def Breadth_First_Search(start, GRAPH):
    visited = [False] * len(GRAPH)
    queue = deque([start])
    visited[start] = True

    while queue: # Run as long as queue is not empty
        vertex = queue.popleft() # Dequeue the first element (Vertex)
        
        for i in range(len(GRAPH)):
            if GRAPH[vertex][i] != 0 and not visited[i]:
                BFS.append([vertex, i])
                queue.append(i)
                visited[i] = True

Breadth_First_Search(2, GRAPH.MATRIX)

def Display(screen, List): # Display Function for Depth_First_Search, Because it is Recursive
    for vertex in List:
        pygame.draw.line(screen, GRAPH.PATH_HIGHLIGHT_COLOR, VERTEX[vertex[0]], VERTEX[vertex[1]], 5)
