def Depth_First_Search(GRAPH, visited, vertex): # Depth_First_Search is also called "Backtracking"
    visited[vertex] = True

    # print the vertex

    for i in range(len(GRAPH)):
        if GRAPH[vertex][i] != 0 and not visited[i]:
            Depth_First_Search(GRAPH, visited, i)


visited = [False]*5

[
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

Depth_First_Search(GRAPH, visited, vertex)
