from curses import window
from sys import displayhook
from urllib import response
import pygame
import requests


backgroundColor = (251, 247, 245)
WIDTH = 550
HEIGHT = 550
grid_color = (50,30,150)
boundaryLine = 4

api_response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = api_response.json()['board']
originalGrid = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def checkNumberValidityUtil(number, pos):
    #Check if the row has a value same as current number
    
    for i in range(0, len(grid)):
        if grid[pos[0]][i] == number:
            return False
    
    #Check same condition but for column
    for i in range(0, len(grid)):
        if grid[i][pos[1]] == number:
            return False

    #Check within the box
    x = pos[0]//3
    y = pos[1]//3

    for i in range(0,3):
        for j in range(0,3):
            if grid[x * 3 + i][y * 3 + j] == number:
                return False
    return True


def isEmptyUtil(number):
    if number == 0:
        return 1
    return 0

flag = 0
def solver(displayWindow):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    for i in range(0,len(grid[0])):
        for j in range(0,len(grid[0])):
            if isEmptyUtil(grid[i][j]):
                for k in range(1,10):
                    pygame.display.update()
                    if checkNumberValidityUtil(k, (i,j)):
                        grid[i][j]=k
                        number = font.render(str(k), True, (0,0,0))
                        displayWindow.blit(number, (((j+1)*50 + 15, (i+1)*50)))
                        pygame.display.update()
                        solver(displayWindow)
                        global flag
                        if flag == 1:
                            return
                        grid[i][j]=0
                        pygame.draw.rect(displayWindow , backgroundColor, ((j+1)*50 + boundaryLine, (i+1)*50 + boundaryLine, 50 - boundaryLine, 50 -boundaryLine))
                        pygame.display.update()
                return
    flag = 1


def main():
    pygame.init()
    displayWindow = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption("Sudoku Solver")
    displayWindow.fill(backgroundColor)
    for i in range(0, 10):
        if i%3 == 0:
            pygame.draw.line(displayWindow, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 4)
            pygame.draw.line(displayWindow, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4)

        #Vertical Lines in grid
        pygame.draw.line(displayWindow, (0,0,0), (50 + 50*i, 50), (50 + 50*i, 500), 1)
        #Horizontalal Lines  in grid
        pygame.draw.line(displayWindow, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 1)

    font = pygame.font.SysFont('Comic Sans MS', 30)
    for i in range(0, len(grid[0])):
        for j in range(len(grid[0])):
            if(0 < grid[i][j] < 10):
                number = font.render(str(grid[i][j]), True, grid_color)
                displayWindow.blit(number, ((j+1) * 50+15, (i+1)*50))
    pygame.display.update()
    solver(displayWindow)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            

main()