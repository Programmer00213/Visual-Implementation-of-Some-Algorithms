from collections import deque

def Depth_First_Search(GRAPH, visited, start): # Depth_First_Search is also called "Backtracking"
    visited[start] = True

    # print the vertex
    print(start, end="->")

    for i in range(len(GRAPH)):
        if GRAPH[start][i] != 0 and not visited[i]:
            Depth_First_Search(GRAPH, visited, i)


def Breadth_First_Search(GRAPH, start):
    visited = [False] * len(GRAPH)

    queue = deque([start])
    visited[start] = True

    while queue: # Run as long as queue is not empty
        vertex = queue.popleft() # Dequeue the first element (Vertex)
        print(vertex, end="->")

        for i in range(len(GRAPH)):
            if GRAPH[vertex][i] != 0 and not visited[i] == False:
                queue.append(i)
                visited[i] = True


visited = [False]*5

GRAPH = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

Depth_First_Search(GRAPH, visited, 2)
Breadth_First_Search(GRAPH,0)
