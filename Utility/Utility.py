import json
import pygame

pygame.init()

VERTEX_COLOR = (100,100,255)

def ExtractFileData(fileName):
    file = open(f"Utility/../Algorithms/{fileName}", 'r')
    
    Data = json.load(file)    

    file.close()

    return Data

VERTEX = ExtractFileData("Vertex.json")
GRAPH = ExtractFileData("Graph.json")
MST_GRAPH = ExtractFileData("MST_GRAPH.json")

# Function
    # Functon to show text in screen
textFont = pygame.font.SysFont("Arial",25)
def Text(text, font, color, x, y, screen):
    text = font.render(text, True, color)
    offset = text.get_rect()
    screen.blit(text, (x - offset.width, y - offset.height))

    # Function to display vertex
def DisplayVertex(screen):
    i = 0
    for coordinate in VERTEX:
        Text(chr(65 + i), textFont, (0,0,0), coordinate[0], coordinate[1] - 10,screen)
        i += 1
        pygame.draw.circle(screen, VERTEX_COLOR, coordinate, 10)

    # Function to display all possible path
def DisplayPath(screen):
    for i in range(0,len(VERTEX)):
        for j in range(0, len(VERTEX)):
            if(GRAPH[i][j] != 0):
                pygame.draw.line(screen, (0,0,0), VERTEX[i], VERTEX[j])
                x = (VERTEX[i][0] + VERTEX[j][0])/2
                y = (VERTEX[i][1] + VERTEX[j][1])/2
                Text(f"{GRAPH[i][j]}", textFont, (0,0,0), x, y, screen)

Fruit_Image = ["Utility/../Assets/Fruit1.png", "Utility/../Assets/Fruit2.png", "Utility/../Assets/Fruit3.png", "Utility/../Assets/Fruit4.png"]
Fruit = [pygame.image.load(image) for image in Fruit_Image]