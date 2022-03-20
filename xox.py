import numpy as np 
import pygame
import math
#rows and columns to represent the board of the game

rows=3
columns=3
#variables required for pygame window
width=600
height=600
size=(width,height)
#creating colors using rgb values 
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
#importing images 
circle=pygame.image.load('circle.png')
cross=pygame.image.load('cross.png')

#The following is the function used to print the mark representing the player whoc clicked it.
def mark(row,col,player):
	board[row][col] = player
#The following function to check whether choosen square on the board is empty or not.
def is_valid_mark(row,col):
	return board[row][col]==0
#The following function  is to check whether all squares are filled if yes the game is over and need to be restarted

def is_board_full():
	for c in range(columns):
		for r in range(rows):
			if(board[r][c]==0):
				return False
	return True
#Function to draw respective symbols representing player.

def draw_board():
	for c in range(columns):
		for r in range(rows):
			if(board[r][c]==1):
				window.blit(circle,((c*200)+50,(r*200)+50))  # blit function is used to display image on window by taking arguments 1-image to be displayed, 2-tuple of x,y representing position of where image to be displayed.
				#x=col*200 + 50 where 50 represents an offset to make the image centered similarly y=row*200 +50
			elif(board[r][c]==2):
				window.blit(cross,((c*200)+50,(r*200)+50))
				
	pygame.display.update()


#Function to sperate pygame window into 9 squares with displaying black lines.

def draw_lines():
	#vertical lines
	pygame.draw.line(window,black,(200,0),(200,600),10) # draw function is used to draw different symbols on the window here we want to draw a line.
	#It takes the arguments 1-surface to draw 2-color 3-start position  4-end position 5-width.
	pygame.draw.line(window,black,(400,0),(400,600),10)

    #horizontal lines
	pygame.draw.line(window,black,(0,200),(600,200),10)
	pygame.draw.line(window,black,(0,400),(600,400),10)



#Function used to check whether it is a win 

def is_winning_move(player):
	if(player==1):
		winning_color=blue 
	else:
		winning_color=red
	for r in range(rows):
		#horizontal check
		if(board[r][0]==player and board[r][1]==player and board[r][2]==player):
			pygame.draw.line(window,winning_color,(10,(r*200)+100),(width-10,(r*200)+100),10)
			#here starting position of line is 10 and ending is width-10 that is t is leaving some gap between border of window and line on both sides
			#here y value remains same as it is a horizontal line the y value will (r*200)+100 where 100 is an offset added to make the line to be placed exactly in the center.

			return True 
	for c in range(columns):
		#vertical check
		if(board[0][c]==player and board[1][c]==player and board[2][c]==player):
			pygame.draw.line(window,winning_color,((c*200)+100, 10),((c*200)+100,height-10),10) 
			
			return True 
	#positive diagonal check
	if(board[0][0]==player and board[1][1]==player and board[2][2]==player):
			pygame.draw.line(window,winning_color,(10,10),(590,590),10)
			return True 
	#negative diagonal check
	if(board[2][0]==player and board[1][1]==player and board[0][2]==player):
			pygame.draw.line(window,winning_color,(590,10),(10,590),10)
			return True 
board=np.zeros((rows,columns))#zeros is a numpy method used to create the board.
game_over=False
 
pygame.init()#Initialize the pygame modules that are imported
window = pygame.display.set_mode(size) #creates a display surface with set_mode() function taking attributes of size od surface.
pygame.display.set_caption("Tic Tac Toe By SWETHA") #Setting a title for pygame display window.
window.fill(white) #Applying background color to window using fill function.
draw_lines()
pygame.display.update() #whenever  we change something for display we need to update the display.
pygame.time.wait(2000) #function wait is used as a delay,it makes our screen hang in for 2000 ms as the argument given.


Turn=0
game_close=False
while not game_over:
	for event in pygame.event.get():
		#checking whether the close button of the pygame window is clicked if yes the game will be over 
		if(event.type==pygame.QUIT):
			game_close=True
		if(event.type==pygame.MOUSEBUTTONDOWN):
			#print(event.pos) #prints the position where the mouse clicked.

			if((Turn%2)==0):
				#Player 1
				#the row  and column of the matrix can be calculated by dividing clicked position by 200
				ro=math.floor(event.pos[1]/200)
				co=math.floor(event.pos[0]/200)
				if(is_valid_mark(ro,co)):
					mark(ro,co,1)
					if(is_winning_move(1)):
						game_over=True 
				else:
					Turn-=1 
			else:
				ro=math.floor(event.pos[1]/200)
				co=math.floor(event.pos[0]/200)
				if(is_valid_mark(ro,co)):
					mark(ro,co,2)
					if(is_winning_move(2)):
						game_over=True 
				else:
					Turn -=1
			Turn+=1
			#print(board)
			draw_board()
	if is_board_full():
		game_over=True
	if(game_over ==True):
		print("Game Over")
		pygame.time.wait(2000)
		#as game over it restarts again from initial state
		board.fill(0)
		window.fill(white)
		draw_lines()
		draw_board()
		game_over=False 
		pygame.display.update()
	if(game_close==True):
		pygame.quit()