from Tkinter import *

'''
The Board is a 15x13 matrix
We will be using a symbolic dictionary to represent the board.
There will be NO POWER UPS until the game is solid 
# -> Permanent Wall
_ -> Destroyable Wall
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

	agentList = []
	agentNumber = 0

	agentStartPositions = [[1,1],[11,13],[11,1],[1,13], [5,7]]

	def __init__(self, parent):
		self.BOARD = [["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"],
		["#"," "," "," "," "," "," "," "," "," "," "," "," "," ","#"],
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

		self.InsertNewAgent()
		self.InsertNewAgent()
		
		for i in range(len(self.BOARD)):
			for j in range(len(self.BOARD[0])):
				if self.BOARD[i][j] == "#":
					self._BOARD = self.DrawBlock(i,j)
				elif self.BOARD[i][j] == "0" or self.BOARD[i][j] == "1":
					self._BOARD = self.DrawAgent(i,j)

	def DrawBlock(self,i,j):
		self.CANVAS.create_rectangle(j*self.BLOCKSIZE, i*self.BLOCKSIZE, j*self.BLOCKSIZE+self.BLOCKSIZE, i*self.BLOCKSIZE+self.BLOCKSIZE, outline="black", fill="#aaa")

	def DrawAgent(self,i,j):
		self.CANVAS.create_rectangle(j*self.BLOCKSIZE, i*self.BLOCKSIZE, j*self.BLOCKSIZE+self.BLOCKSIZE, i*self.BLOCKSIZE+self.BLOCKSIZE, fill="#f00")

	def InsertNewAgent(self):
		if len(self.agentList) > 4:
			return
		x, y = self.agentStartPositions[self.agentNumber][0], self.agentStartPositions[self.agentNumber][1]
		self.BOARD[x][y] = str(self.agentNumber)
		a = Agent(self.agentNumber,x,y)
		self.agentList.append(a)
		self.agentNumber += 1
		return a

	#this function verifies the position and the + shape located positions around the agent. Then it returns a list of possible moves.
	def GetValidActions(self, agent):
		positions = []
		positions.append(agent.x, agent.y)
		if self._BOARD[agent.x][agent.y] != "#" and self._BOARD[agent.x + 1][agent.y] != "B" and self._BOARD[agent.x][agent.y] != "_":
			positions.append(agent.x+1, agent.y)
		if self._BOARD[agent.x][agent.y] != "#" and self._BOARD[agent.x - 1][agent.y] != "B" and self._BOARD[agent.x][agent.y] != "_":
			positions.append(agent.x-1, agent.y)
		if self._BOARD[agent.x][agent.y] != "#" and self._BOARD[agent.x][agent.y + 1] != "B" and self._BOARD[agent.x][agent.y] != "_":
			positions.append(agent.x, agent.y+1)
		if self._BOARD[agent.x][agent.y] != "#" and self._BOARD[agent.x][agent.y - 1] != "B" and self._BOARD[agent.x][agent.y] != "_":
			positions.append(agent.x, agent.y-1)
		return positions


class Agent:
	id = 0
	x, y = 0, 0

	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y


WIDTH = 480
HEIGHT = 416

top = Tk()
top.resizable(0,0)

canvas = Canvas(top, bg="white", height=HEIGHT, width=WIDTH)
canvas.pack()

b = Board(canvas)

while 1:
	top.update()