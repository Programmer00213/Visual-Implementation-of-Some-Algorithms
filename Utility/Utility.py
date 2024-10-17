import json
import pygame

pygame.init()

# Screen Class
class Screen:
    def __init__(self, WIDTH, HEIGHT, COLOR):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.COLOR = COLOR

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def Text(self, text, size, color, x, y):
        textFont = pygame.font.SysFont("Arial",size)
        text = textFont.render(text, True, color)
        offset = text.get_rect()
        self.screen.blit(text, (x - offset.width/2, y - offset.height/2))

SCREEN = Screen(1300,720,(150,170,200))

def getData(fileName): # the file must be of type json
    if not fileName: return 1
    file = open(f"Utility/../Algorithms/Graphs/{fileName}.json", 'r')
    Data = json.load(file)    
    file.close()
    return Data

# Graph Class
class Graph:
    def __init__(self, GRAPH_FILE, VERTEX_FILE, VERTEX_COLOR, PATH_HIGHLIGHT_COLOR, PATH_COLOR):
        self.VERTEX_COLOR = VERTEX_COLOR
        self.PATH_HIGHLIGHT_COLOR = PATH_HIGHLIGHT_COLOR
        self.PATH_COLOR = PATH_COLOR
        self.MATRIX = getData(GRAPH_FILE)
        self.VERTEX_COORDINATE = getData(VERTEX_FILE)
        
    # Function to display vertex
    def DisplayVertex(self, Screen):
        i = 0
        for coordinate in self.VERTEX_COORDINATE:
            Screen.Text(chr(65 + i), 25, (0,0,0), coordinate[0]-17, coordinate[1] - 25)
            i += 1
            # to display vertex
            pygame.draw.circle(Screen.screen, self.VERTEX_COLOR, coordinate, 10)

    def DisplayPath(self, Screen, show_Weight = False):
        for i in range(0,len(self.VERTEX_COORDINATE)):
            for j in range(0, len(self.VERTEX_COORDINATE)):
                if(self.MATRIX[i][j] != 0):
                    # to display path
                    pygame.draw.line(Screen.screen, (0,0,0), self.VERTEX_COORDINATE[i], self.VERTEX_COORDINATE[j])
                    # to calculate coordinate for weight
                    if show_Weight:
                        x = (self.VERTEX_COORDINATE[i][0] + self.VERTEX_COORDINATE[j][0])/2
                        y = (self.VERTEX_COORDINATE[i][1] + self.VERTEX_COORDINATE[j][1])/2
                        Screen.Text(f"{self.MATRIX[i][j]}", 25, (0,0,0), x+15, y-25)

GRAPH = Graph("Graph", "Vertex", (100,100,255), (0,255,0), (0,0,0))
MST_GRAPH = getData("MST_GRAPH")

class Button:
    def __init__(self, Name, x, y, Color):
        self.Name = Name
        self.x = x
        self.y = y
        self.Width = 200
        self.Height = 50
        self.Color = Color
        self.Rect = pygame.Rect(self.x, self.y, self.Width, self.Height)
        
    def Create(self, screen):
        pygame.draw.rect(screen, self.Color, self.Rect)
        SCREEN.Text(self.Name, 25, (255,255,255), self.x + self.Width/2, self.y + self.Height/2)

Dijkstra_Button = Button("Dijkstra", SCREEN.WIDTH - 250, 120, (0,200,0))
Kruskal_Button = Button("Kruskal", SCREEN.WIDTH - 250, 200, (0,200,0))
DFS_Button = Button("DFS", SCREEN.WIDTH - 250, 280, (0,200,0))
BFS_Button = Button("BFS", SCREEN.WIDTH - 250, 360, (0,200,0))
MaxFlow_Button = Button("Max Flow", SCREEN.WIDTH - 250, 440, (0,200,0))
Permutation_Button = Button("Permutation", SCREEN.WIDTH - 250, 520, (0,200,0))
Combination_Button = Button("Combination", SCREEN.WIDTH - 250, 600, (0,200,0))

Buttons = [Dijkstra_Button, Kruskal_Button, DFS_Button, BFS_Button, MaxFlow_Button, Permutation_Button, Combination_Button]

# For Permutation and Combination
Fruit_Image = ["Utility/../Assets/Fruit1.png",
               "Utility/../Assets/Fruit2.png",
               "Utility/../Assets/Fruit3.png",
               "Utility/../Assets/Fruit4.png"]

Fruit = [pygame.image.load(image) for image in Fruit_Image]