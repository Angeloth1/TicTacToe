from pickle import FALSE, TRUE
import pygame, sys
import numpy as np
pygame.init()

#functions
def draw_line():
    pygame.draw.line(screen, LN_COLOR, (0,200), (600,200), LN_WIDTH)
    pygame.draw.line(screen, LN_COLOR, (0,400), (600,400), LN_WIDTH)
    pygame.draw.line(screen, LN_COLOR, (200,0), (200,600), LN_WIDTH)
    pygame.draw.line(screen, LN_COLOR, (400,0), (400,600), LN_WIDTH)
def mark_square(row,col,pl):
    board[row][col]= pl
def available_sq(row,col):
    return board[row][col] == 0
def is_board_full():
    for row in range(BOARD_RC):
        for col in range(BOARD_RC):
            if board[row][col] == 0:
                return FALSE
    return True
def draw_figures():
     for row in range(BOARD_RC):
        for col in range(BOARD_RC):
            if board[row][col] == 1:
                pygame.draw.circle( screen, FG_COLOR, (int( col*200 + 100),int( row*200 + 100 )),CIRCLE_RAD ,CIRCLE_WIDTH )
            elif board[row][col]== 2:
                pygame.draw.line(screen ,FG_COLOR, (col*200+ SPACE, row *200 +200 - SPACE),(col*200+ 200-SPACE, row *200 +SPACE),CIRCLE_WIDTH)
                pygame.draw.line(screen ,FG_COLOR, (col*200+ SPACE, row *200 + SPACE),(col*200+ 200-SPACE, row *200+200-SPACE),CIRCLE_WIDTH)
def check_win(player):
    #vertical
    for col in range(BOARD_RC):
        if board[0][col] ==pl and board[1][col] ==pl and board[2][col] == pl:
            posX = col * 200 + 100
            if player ==1:
                color = (10,10,50)
            elif pl==2:
                color = (50,10,10)
            pygame.draw.line(screen, color,(posX, 15),(posX,HEIGHT-15),15)
            return True
    #horizontal
    for row in range(BOARD_RC):
        if board[0][row] ==pl and board[1][row] ==pl and board[2][row] == pl:
            posY = row * 200 + 100
            if player ==1:
                color = (10,10,50)
            elif pl==2:
                color = (50,10,10)
            pygame.draw.line(screen, color,(posY, 15),(posY,WIDTH-15),15)
            return True
    #asc diagonal
    if board[2][0]== pl and board[1][1]==pl and board[0][2]==pl:
            if player ==1:
                color = (10,10,50)
            elif pl==2:
                color = (50,10,10)
            pygame.draw.line(screen,color,(15, HEIGHT -15),(WIDTH-15,15),15)
            return True
    #desc diagonal
    if board[0][0]== pl and board[1][1]==pl and board[2][2]==pl:
        if player ==1:
            color = (10,10,50)
        elif pl==2:
            color = (50,10,10)
        pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT - 15),15)
        return True
    return False
def restart():
    screen.fill(BG_COLOR)
    draw_line()
    pl=1
    gameover =False
    for row in range(BOARD_RC):
        for col in range(BOARD_RC):
            board[row][col]= 0
    
#vars
pl=1
gameover= False

#const.
WIDTH= 600
HEIGHT= 600
LN_COLOR= (10, 150, 140)
FG_COLOR= (10,50,30)
CIRCLE_RAD= 60
CIRCLE_WIDTH= 15
LN_WIDTH= 15
BG_COLOR= (10, 180, 170)
BOARD_RC= 3
SPACE= 55

#screen
screen = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill( BG_COLOR)
draw_line()

#board
board= np.zeros((BOARD_RC,BOARD_RC))

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            
            mouseX= event.pos[0]
            mouseY= event.pos[1]

            clicked_row= int(mouseY // 200)
            clicked_col= int(mouseX // 200)

            if available_sq(clicked_row,clicked_col):
                if pl== 1:
                    mark_square(clicked_row,clicked_col, 1)
                    if check_win(pl):
                        gameover= True
                    pl= 2
                elif pl== 2:
                    mark_square(clicked_row,clicked_col, 2)
                    if check_win(pl):
                        gameover= True
                    pl =1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()