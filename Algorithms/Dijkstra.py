import pygame
import Utility.Utility as Utility

INFINITE = 10**100
VERTEX = len(Utility.VERTEX)

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


def Display(SCREEN, parent, destination):

    if parent[destination] == -1:
        return
    pygame.draw.line(SCREEN, (0,200,0),Utility.VERTEX[destination], Utility.VERTEX[parent[destination]],5)
    Display(SCREEN, parent, parent[destination])
