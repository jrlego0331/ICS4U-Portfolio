import pygame as pg
import numpy as np
import sys

#score displaying 
class score():
    def __init__(self, deductions = -5000, addition = 100):
        self.font = pg.font.Font('resources/fonts.ttf', 14)
        self.value = 0
        self.deductions = deductions
        self.additions = addition
        self.validMove = True

    def display(self):
        screen.blit(self.font.render(str(self.value), 0, (255, 255, 255)), (0, screenHeight+scoreBarHeight/2))    

#screen initialize & game settings
pg.init()
screenWidth, screenHeight = 320, 640
scoreBarHeight = 40
screen = pg.display.set_mode((screenWidth, screenHeight+scoreBarHeight))
pg.display.set_caption("gemiarow")
clock = pg.time.Clock()
FPS = 10

#tile IMG loading, index -5 to -1 is assigned to empty tile
tileImg = [pg.image.load('resources/gem1.png'), pg.image.load('resources/gem2.png'), pg.image.load('resources/gem3.png'),
           pg.image.load('resources/gem4.png'), pg.image.load('resources/gem5.png'), pg.image.load('resources/gem6.png'),
           pg.image.load('resources/effect1.png'), pg.image.load('resources/effect2.png'), pg.image.load('resources/effect3.png'),
           pg.image.load('resources/effect4.png'), pg.image.load('resources/effect5.png')]
effectTileCount = 5

#IMG size
tileSize = (32, 32)

#tile Status 2Darray
matrix = np.random.rand(int(screenWidth / tileSize[0]), int(screenHeight / tileSize[1]))
matrix = np.int_(np.rint(np.dot(matrix, len(tileImg)-effectTileCount-1)))

#user selected tile
selected = []

track = score()

#main loop
while True:

    #event checking
    for event in pg.event.get():
        #memory friendly quit
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()

        #Mouse events
        if event.type == pg.MOUSEBUTTONDOWN:
            for x in range(int(screenWidth / tileSize[0])):
                for y in range(int(screenHeight / tileSize[1])):
                    mousePos = pg.mouse.get_pos()
                    #when clicked, append closetest tile coordinate
                    if mousePos[0] > x*tileSize[0] and mousePos[0] < (x+1)*tileSize[0] and mousePos[1] > y*tileSize[1] and mousePos[1] < (y+1)*tileSize[1]:
                        selected.append((x, y))
    
    #init screen
    screen.fill((0, 0, 0))

    #switch selected tiles
    if len(selected) == 2:
        track.validMove = False
        #check for index difference of selected tiles
        if (abs(selected[0][0] - selected[1][0]) == 1 and abs(selected[0][1] - selected[1][1]) == 0) or (abs(selected[0][0] - selected[1][0]) == 0 and abs(selected[0][1] - selected[1][1]) == 1):
            matrix[selected[0][0]][selected[0][1]], matrix[selected[1][0]][selected[1][1]] = matrix[selected[1][0]][selected[1][1]], matrix[selected[0][0]][selected[0][1]]
        selected = []

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            #update tile after effect reaches its final stage
            if matrix[x][y] == -1: 
                #if top, regenerate below tiles with index -1
                if y == 0:
                    scopeY = 0 
                    while matrix[x][scopeY] == -1:
                        matrix[x][scopeY] = np.random.randint(0, len(tileImg)-effectTileCount)                    
                        scopeY+=1
                #fall if not top layer
                else: 
                    for lensY in range(y, 0, -1): matrix[x][lensY] = matrix[x][lensY-1]

            #five in a row
            if matrix[x][y] >= 0 and x + 4 < len(matrix) and matrix[x][y] == matrix[x+1][y] == matrix[x+2][y] == matrix[x+3][y] == matrix[x+4][y]: 
                matrix[x][y], matrix[x+1][y], matrix[x+2][y], matrix[x+3][y], matrix[x+4][y] = -effectTileCount, -effectTileCount, -effectTileCount, -effectTileCount, -effectTileCount
                track.value += 4 * 5 * track.additions
                track.validMove = True
            
            #five in a column
            if matrix[x][y] >= 0 and y + 4 < len(matrix[x]) and matrix[x][y] == matrix[x][y+1] == matrix[x][y+2] == matrix[x][y+3] == matrix[x][y+4]:
                matrix[x][y], matrix[x][y+1], matrix[x][y+2], matrix[x][y+3], matrix[x][y+4] = -effectTileCount, -effectTileCount, -effectTileCount, -effectTileCount, -effectTileCount
                track.value += 4 * 5 * track.additions
                track.validMove = True

            #four in a row
            if matrix[x][y] >= 0 and x + 3 < len(matrix) and matrix[x][y] == matrix[x+1][y] == matrix[x+2][y] == matrix[x+3][y]: 
                matrix[x][y], matrix[x+1][y], matrix[x+2][y], matrix[x+3][y] = -effectTileCount, -effectTileCount, -effectTileCount, -effectTileCount
                track.value += 2 * 4 * track.additions
                track.validMove = True
            
            #four in a column
            if matrix[x][y] >= 0 and y + 3 < len(matrix[x]) and matrix[x][y] == matrix[x][y+1] == matrix[x][y+2] == matrix[x][y+3]:
                matrix[x][y], matrix[x][y+1], matrix[x][y+2], matrix[x][y+3] = -effectTileCount, -effectTileCount, -effectTileCount, -effectTileCount
                track.value += 2 * 4 * track.additions
                track.validMove = True
            

            #three in a row
            if matrix[x][y] >= 0 and x + 2 < len(matrix) and matrix[x][y] == matrix[x+1][y] == matrix[x+2][y]: 
                matrix[x][y], matrix[x+1][y], matrix[x+2][y] = -effectTileCount, -effectTileCount, -effectTileCount
                track.value += 3 * track.additions
                track.validMove = True
            
            #three in a column
            if matrix[x][y] >= 0 and y + 2 < len(matrix[x]) and matrix[x][y] == matrix[x][y+1] == matrix[x][y+2]:
                matrix[x][y], matrix[x][y+1], matrix[x][y+2] = -effectTileCount, -effectTileCount, -effectTileCount
                track.value += 3 * track.additions
                track.validMove = True
            

            #effect update
            if matrix[x][y] < -1 : matrix[x][y]+=1

            #draw tile
            screen.blit(tileImg[matrix[x][y]], (x*tileSize[0], y*tileSize[1]))

    #score layer
    #deduct socore if the move did not success
    if track.validMove == False: 
        track.value += track.deductions
        track.validMove = True
    if track.value <= 0: track.value = 0

    #draw score
    track.display()

    #draw emphasis on selected tiles:
    for selectedTile in selected:
        pg.draw.rect(screen, (255, 255, 255), (tileSize[0]*selectedTile[0], tileSize[1]*selectedTile[1], tileSize[0], tileSize[1]), 2)

    #update&tick
    pg.display.update()
    clock.tick(FPS)