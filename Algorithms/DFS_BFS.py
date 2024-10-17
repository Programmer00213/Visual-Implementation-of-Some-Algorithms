from collections import deque
import pygame
from Utility.Utility import GRAPH

VERTEX = GRAPH.VERTEX_COORDINATE

DFS = []

def Depth_First_Search(GRAPH, visited, start): # Depth_First_Search is also called "Backtracking" Recursive Version
    visited[start] = True

    for i in range(len(GRAPH)):
        if GRAPH[start][i] != 0 and not visited[i]:
            DFS.append([start, i])
            Depth_First_Search(GRAPH, visited, i)

visited = [False]*len(VERTEX)
Depth_First_Search(GRAPH.MATRIX, visited, 2)

def Display(screen): # Display Function for Depth_First_Search, Because it is Recursive
    for vertex in DFS:
        pygame.draw.line(screen, (0,200,0), VERTEX[vertex[0]], VERTEX[vertex[1]], 5)


def Breadth_First_Search(start ,screen, GRAPH = GRAPH.MATRIX):
    visited = [False] * len(GRAPH)
    color = 0
    queue = deque([start])
    visited[start] = True

    while queue: # Run as long as queue is not empty
        vertex = queue.popleft() # Dequeue the first element (Vertex)
        
        for i in range(len(GRAPH)):
            if GRAPH[vertex][i] != 0 and not visited[i]:
                pygame.draw.line(screen, (0,200,color), VERTEX[vertex], VERTEX[i],5)
                queue.append(i)
                visited[i] = True
        color += 30
