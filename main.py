from Tkinter import *

'''
The Board is a 15x13 matrix
We will be using a symbolic dictionary to represent the board.
There will be NO POWER UPS until the game is solid 
# -> Wall
B -> Bomb
F -> Fire
SPACE -> Empty 
1,2,3,4,5 -> Is the agent number
'''

class Board:
	WIDTH, HEIGHT = 15, 13
	BOARD = [] #This board is TEXT BASED
	_BOARD = [] #This is a visual Board. It will be filled based on the text based Board
	CANVAS = None
	BLOCKSIZE = 32

	def __init__(self, parent):
		self.BOARD = [["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
		["#","1"," "," "," "," "," "," "," "," "," "," "," "," ","#"],
		["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
		["#"," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
		["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
		["#"," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
		["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
		["#"," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
		["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
		["#"," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
		["#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"," ","#"],
		["#"," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
		["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]]

		self._BOARD = [[None for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
		self.CANVAS = parent
		
		for i in range(len(self.BOARD)):
			for j in range(len(self.BOARD[0])):
				if self.BOARD[i][j] == "#":
					self._BOARD = self.DrawBlock(i,j)

	def DrawBlock(self,i,j):
		self.CANVAS.create_rectangle(j*self.BLOCKSIZE, i*self.BLOCKSIZE, j*self.BLOCKSIZE+self.BLOCKSIZE, i*self.BLOCKSIZE+self.BLOCKSIZE, outline="black", fill="#aaa")

WIDTH = 480
HEIGHT = 416

top = Tk()
top.resizable(0,0)

canvas = Canvas(top, bg="white", height=HEIGHT, width=WIDTH)
canvas.pack()

b = Board(canvas)

while 1:
	top.update()