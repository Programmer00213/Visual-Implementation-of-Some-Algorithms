import pygame
import Algorithms.Dijkstra as Dijkstra
import Algorithms.Kruskal as Kruskal
import Algorithms.Permutation_and_Combination as Permutation_Combination
import Utility.Utility as Utility
import sys

pygame.init()

# window setup
WIDTH = 1000
HEIGHT = 700
BACKGROUND_COLOR = (150,170,200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Shortest Path")

running = True

# Vertex A = 0, j = 9

# program loop
MST = Kruskal.KruskalMST(Utility.MST_GRAPH)
#parent = Dijkstra.Dijkstra(Utility.GRAPH, 0)
#Permutation_Combination.Permutation(0,3,Utility.Fruit)
#number = 2
#data = [0] * number
#Permutation_Combination.Combination(Utility.Fruit, data, number, 0, 4, 0)
#print(Permutation_Combination.Combination_Result)

while running:
    screen.fill(BACKGROUND_COLOR)
    Utility.DisplayPath(screen)
    #Dijkstra.Display(screen, parent, 8)
    Kruskal.Display(MST,screen)
    Utility.DisplayVertex(screen)
    #Permutation_Combination.Display(Permutation_Combination.Permutation_Result, screen)
    #Permutation_Combination.Display(Permutation_Combination.Combination_Result, screen)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

# [[3, 7, 4], [0, 1, 6], [2, 3, 7], [9, 8, 7], [1, 2, 8], [8, 7, 8], [4, 9, 9], [6, 5, 9], [2, 6, 10]]