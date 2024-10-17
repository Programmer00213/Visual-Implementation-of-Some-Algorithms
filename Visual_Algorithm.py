import pygame
import Algorithms.Dijkstra as Dijkstra
import Algorithms.Kruskal as Kruskal
import Algorithms.Permutation_and_Combination as Permutation_Combination
import Algorithms.DFS_BFS as DFS_BFS
from Utility.Utility import SCREEN, GRAPH, Buttons
import sys

pygame.init()

def test():
    # # window setup
    # WIDTH = 1000
    # HEIGHT = 700
    # BACKGROUND_COLOR = (150,170,200)

    # screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # pygame.display.set_caption("Shortest Path")

    # running = True

    # # Vertex A = 0, j = 9

    # # program loop
    # MST = Kruskal.KruskalMST(Utility.MST_GRAPH)
    # #parent = Dijkstra.Dijkstra(Utility.GRAPH, 0)
    # #Permutation_Combination.Permutation(0,3,Utility.Fruit)
    # #number = 2
    # #data = [0] * number
    # #Permutation_Combination.Combination(Utility.Fruit, data, number, 0, 4, 0)
    # #print(Permutation_Combination.Combination_Result)

    # visited = [False]*len(Utility.VERTEX)
    # DFS_BFS.Depth_First_Search(Utility.GRAPH, visited, 2, screen)

    # print(DFS_BFS.DFS)

    # while running:
    #     screen.fill(BACKGROUND_COLOR)

    #     Utility.DisplayPath(screen)
    #     #Dijkstra.Display(screen, parent, 8)
    #     #Kruskal.Display(MST,screen)
    #     Utility.DisplayVertex(screen)

    #     #Permutation_Combination.Display(Permutation_Combination.Permutation_Result, screen)
    #     #Permutation_Combination.Display(Permutation_Combination.Combination_Result, screen)
    
    #     #DFS_BFS.Breadth_First_Search(Utility.GRAPH, 2, screen)
    #     DFS_BFS.Display(screen)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #     pygame.display.update()
    pass

def Algorithms(screen, Algorithm):
    if Algorithm == "Dijkstra":
        Dijkstra.Display(screen, 8)
    elif Algorithm == "Kruskal":
        Kruskal.Display(screen)
    elif Algorithm == "DFS":
        DFS_BFS.Display(screen)
    elif Algorithm == "BFS":
        DFS_BFS.Breadth_First_Search(2,screen)
    elif Algorithm == "Max Flow":
        pass
    elif Algorithm == "Permutation":
        Permutation_Combination.Display(Permutation_Combination.Permutation_Result, screen)
    elif Algorithm == "Combination":
        Permutation_Combination.Display(Permutation_Combination.Combination_Result,screen)
    else:
        pass

def WelcomeScreen():
    Running = True

    Clicked = False

    Display = ""

    while Running:
        Mouse_Pos_X,Mouse_Pos_Y = pygame.mouse.get_pos()
        Cursor = pygame.Rect(Mouse_Pos_X, Mouse_Pos_Y,20,20)

        SCREEN.screen.fill(SCREEN.COLOR)

        if Display != "Permutation" and Display != "Combination":
            SCREEN.Text("Visual Representation Of Algorithm", 48, (0,0,0), SCREEN.WIDTH/2, SCREEN.HEIGHT/15)
            GRAPH.DisplayVertex(SCREEN)
            GRAPH.DisplayPath(SCREEN, True)

        Algorithms(SCREEN.screen, Display)

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