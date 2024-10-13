import pygame

Permutation_Result = []
Combination_Result = []

def Swap(items, a, b):
    items[a], items[b] = items[b], items[a]

x = 0
def Display(items, screen):
    global x
    y = 0
    n = 0
    for item in items:
        for fruits in item:
            resized = pygame.transform.scale(fruits, (50,50))
            screen.blit(resized, (x, y))
            x += 80
        x = 400 * n
        if(y > 600): 
            y = 0
            n += 1
        else:
            y += 60

def Permutation(left, right, items): # left index, right index[last index]
    if left == right:
        Permutation_Result.append(items[:]) # [:] is required to create a new shallow copy of the list and not reference the original list
    else:
        for i in range(left, right + 1):
            # swap index i and left
            Swap(items, left, i)
            Permutation(left+1, right, items)
            # swap index i and left again
            Swap(items, left, i)

def Combination(items, array, number, start, end, index):
    if index == number:
        Combination_Result.append(array[:])
        return

    for i in range(start, end):
        if (end - i) >= number - index:
            array[index] = items[i]
            Combination(items, array, number, i + 1, end, index + 1)