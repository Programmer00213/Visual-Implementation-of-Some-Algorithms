import Utility.Utility as Utility
import pygame

VERTEX = len(Utility.MST_GRAPH)

parent = [i for i in range(VERTEX)]
rank = [0] * VERTEX

def Find(vertex):
    if(parent[vertex] != vertex):
        parent[vertex] = Find(parent[vertex])

    return parent[vertex]

def Union(vertex1, vertex2):
    rootX = Find(vertex1)
    rootY = Find(vertex2)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootX] = rootY
            rank[rootX] = rank[rootX] + 1

Minimum_Spanning_Tree = []

def KruskalMST(GRAPH):
    GRAPH.sort(key = lambda x : x[2])

    for i in range(VERTEX - 1): # Because a tree has Vertex - 1 Edges

        parent1 = Find(GRAPH[i][0])
        parent2 = Find(GRAPH[i][1])

        if parent1 != parent2:
            Minimum_Spanning_Tree.append(GRAPH[i])
            Union(parent1, parent2)

    return Minimum_Spanning_Tree

def Display(MST, SCREEN):
    for edge in MST:
        pygame.draw.line(SCREEN, (0,200,0), Utility.VERTEX[edge[0]], Utility.VERTEX[edge[1]], 5)