from urllib import response
import pygame
import requests


backgroundColor = (251, 247, 245)
WIDTH = 550
HEIGHT = 550
grid_color = (50,30,150)

api_response = requests.get("https://sugoku.heroku.com/board?difficulty=easy")
grid = response.json()['board']
originalGrid = [[grid[x][y] for y in range(len(grid[0]))] for x in range(grid[len(grid)])]

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
    pygame.display.update()

    font = pygame.font.SysFont('Comic Sans MS', 30)
    for i in range(0, len(grid[0])):
        for j in range(len(grid[0])):
            if(0 < grid[i][j] < 10):
                number = font.render(str(grid[i][j]), True, grid_color)
                displayWindow.blit(number, (j+1) * 50, (i+1)*50 + 15)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return

main()