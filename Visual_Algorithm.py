import pygame
import Algorithms.Dijkstra as Dijkstra
import Algorithms.Kruskal as Kruskal
import Algorithms.Permutation_and_Combination as Permutation_Combination
import Algorithms.DFS_BFS as DFS_BFS
import Algorithms.MaxFlow as MaxFlow
from Utility.Utility import SCREEN, GRAPH2, Buttons
import sys

pygame.init()

GRAPH = GRAPH2

def Algorithms(Screen, Algorithm):
    if Algorithm == "Dijkstra":
        Dijkstra.Display(Screen.screen, 8)
    elif Algorithm == "Kruskal":
        Kruskal.Display(Screen.screen)
    elif Algorithm == "DFS":
        DFS_BFS.Display(Screen.screen, DFS_BFS.DFS)
    elif Algorithm == "BFS":
        DFS_BFS.Display(Screen.screen, DFS_BFS.BFS)
    elif Algorithm == "Max Flow":
        maxflow = MaxFlow.Max_Flow(0,8,Screen.screen)
        SCREEN.Text(f"Max Flow: {maxflow}", 35, (0,0,0), SCREEN.WIDTH/2, SCREEN.HEIGHT/2)
    elif Algorithm == "Permutation":
        Permutation_Combination.Display(Permutation_Combination.Permutation_Result, Screen.screen)
    elif Algorithm == "Combination":
        Permutation_Combination.Display(Permutation_Combination.Combination_Result,Screen.screen)
    else:
        pass

def WelcomeScreen():
    Running = True

    Clicked = False

    Display = "Algorithm"

    while Running:
        Mouse_Pos_X,Mouse_Pos_Y = pygame.mouse.get_pos()
        Cursor = pygame.Rect(Mouse_Pos_X, Mouse_Pos_Y,20,20)

        SCREEN.screen.fill(SCREEN.COLOR)

        SCREEN.Text(f"Visual Representation Of {Display} Algorithm", 48, (0,0,0), SCREEN.WIDTH/2, SCREEN.HEIGHT/15)
        if Display != "Permutation" and Display != "Combination":
            GRAPH.DisplayVertex(SCREEN)
            GRAPH.DisplayPath(SCREEN, True)

        Algorithms(SCREEN, Display)

        for Button in Buttons:
            Button.Create(SCREEN.screen)
         
            if Cursor.colliderect(Button.Rect) and Clicked == True:
                Display = Button.Name
        
        Clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Clicked = True

        pygame.display.update()

WelcomeScreen()

# [[3, 7, 4], [0, 1, 6], [2, 3, 7], [9, 8, 7], [1, 2, 8], [8, 7, 8], [4, 9, 9], [6, 5, 9], [2, 6, 10]]
# 2->6->7->8->9->4->0->5->3->1
# 2->1->0->4->3->7->6->5->8->9
# 2->1->0->4->9->8->7->5->3->6