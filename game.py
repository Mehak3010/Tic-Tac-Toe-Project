#TIC TAC TOE
import pygame
import sys
import numpy as np
pygame.init()

#Variables
width=650
height=width
line_width=15
board_row=3
board_col=3
square_size=height//board_row
red=(255,0,0)
circle_radius=square_size//3
circle_width=15
circle_color=(71,70,66)
cross_color=(217,215,210)
cross_width=25
space=square_size//4
bg_color=(80,165,155)
line_color=(23,145,135)

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)

board=np.zeros((board_row,board_col))

def draw_lines():
    pygame.draw.line(screen,line_color,(0,square_size),(width,square_size),line_width)
    pygame.draw.line(screen,line_color,(0,square_size*2),(width,square_size*2),line_width)
    pygame.draw.line(screen,line_color,(square_size,0),(square_size,height),line_width)
    pygame.draw.line(screen,line_color,(square_size*2,0),(square_size*2,height),line_width)
    
def draw_figures():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col]==1:
                pygame.draw.circle(screen,circle_color,(int(col * square_size+square_size//2),int(row * square_size+square_size//2)),circle_radius,circle_width
                                   )
            elif board[row][col]==2:
                pygame.draw.line(screen,cross_color,(col*square_size + space,row*square_size+square_size-space),(col*square_size+square_size-space,row*square_size+space),cross_width) #starts line from bottom left corner,starts line from upper right corner.
                pygame.draw.line(screen,cross_color,(col*square_size + space,row*square_size+space),(col*square_size+square_size-space,row*square_size+square_size-space),cross_width)
def mark_squares(row,col,player):
    board[row][col]=player
def vacant_squares(row,col):
    return board[row][col]==0
def board_full():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col]==0:
                return False
    return True
def winner(player):
    #for vertical winning line
    for col in range(board_col):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            vertical_winning_line(col,player)
            return True
    #for Horizontal winning line
    for row in range(board_row):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            horizontalal_winning_line(row,player)
            return True
    #for diagonal bottom left to top right winning line
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        diagonal_winning_line_1(player)
        return True
     #for diagonal top left to bottom right winning line
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        diagonal_winning_line_2(player)
        return True   
    return False 
def vertical_winning_line(col,player):
    posx = col*square_size + square_size//2
    if player ==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(posx,15),(posx,height-15),15)
def horizontalal_winning_line(row,player):
    posy = row*square_size + square_size//2
    if player ==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(15,posy),(width-15,posy),15)
def diagonal_winning_line_1(player):
    if player ==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(15,height-15),(width-15,15),15)
def diagonal_winning_line_2(player):
    if player ==1:
        color=circle_color
    elif player==2:
        color=cross_color
    pygame.draw.line(screen,color,(15,15),(width-15,height-15),15)
def restart():
    screen.fill(bg_color)
    draw_lines()
    player=1
    for row in range(board_row):
        for col in range(board_col):
            board[row][col]=0
                
draw_lines()
player=1
game_over=False

#Main loop

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x=event.pos[0]
            mouse_y=event.pos[1]
            clicked_row=int(mouse_y//square_size)
            clicked_col=int(mouse_x//square_size)
        
            if vacant_squares(clicked_row,clicked_col):
                mark_squares(clicked_row,clicked_col,player)
                if winner(player):
                    game_over=True
                player=player % 2 + 1
                draw_figures()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                game_over=False
    pygame.display.update()
