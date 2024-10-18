import pygame
from Utility.Utility import GRAPH2

INFINITE = float('INF')
GRAPH = GRAPH2
VERTEX = len(GRAPH.MATRIX)

def MinimumDistance(distance, processed):
    MIN = INFINITE
    nextVertex = 0
    for i in range(0,VERTEX):
        if(processed[i] == 0 and distance[i] < MIN):
            MIN = distance[i]
            nextVertex = i

    return nextVertex

def Dijkstra(GRAPH, source):
    distance = [INFINITE]*VERTEX
    processed = [0]*VERTEX
    parent = [-1]*VERTEX

    distance[source] = 0

    for i in range(0, VERTEX - 1):
        currentVertex = MinimumDistance(distance, processed)
        processed[currentVertex] = 1 

        for j in range(0, VERTEX):
            if(not processed[j] and distance[currentVertex] != INFINITE and GRAPH[currentVertex][j] and distance[j] > distance[currentVertex] + GRAPH[currentVertex][j]):
                distance[j] = distance[currentVertex] + GRAPH[currentVertex][j]
                parent[j] = currentVertex

    return parent

parent = Dijkstra(GRAPH.MATRIX, 0)

def Display(SCREEN, destination):
    if parent[destination] == -1:
        return
    pygame.draw.line(SCREEN, GRAPH.PATH_HIGHLIGHT_COLOR, GRAPH.VERTEX_COORDINATE[destination], GRAPH.VERTEX_COORDINATE[parent[destination]],5)
    Display(SCREEN, parent[destination])

