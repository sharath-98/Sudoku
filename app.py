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


def insertNum(window, pos):
    inputFont = pygame.font.SysFont('Comic Sans MS', 35)
    i,j = pos[1], pos[0]
    print(1," ",j)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                # Restrict modufying original value
                if originalGrid[i-1][j-1] != 0:
                    return
                # Update Value in grid
                #----Check for zero ----
                if e.key == 48:
                    grid[i-1][j-1] = e.key - 48
                    pygame.draw.rect(window , backgroundColor, (pos[0]*50 + boundaryLine, pos[1]*50 + boundaryLine, 50 - boundaryLine, 50 - boundaryLine))
                    pygame.display.update()
                    return
                #Check proper number is entered
                if (0 < e.key - 48 < 10):
                    pygame.draw.rect(window , backgroundColor, (pos[0]*50 + boundaryLine, pos[1]*50 + boundaryLine, 50 - boundaryLine, 50 - boundaryLine))
                    number = inputFont.render(str(e.key - 48), True, (0,0,0))
                    window.blit(number, (pos[0]*50+15, pos[1]*50))
                    grid[i-1][j-1] = e.key - 48
                    pygame.display.update()
                    return
                return

                # New Entry in grid


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

    while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                pos = pygame.mouse.get_pos()
                insertNum(displayWindow , (pos[0]//50, pos[1] // 50))
            if e.type == pygame.QUIT:
                pygame.quit()
                return

            

main()