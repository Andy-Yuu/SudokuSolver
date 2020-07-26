# prints sudoku board
def printBoard(board):
	for i in range(0,9):
		print(board[i])

# finds empty cell
def findEmpty(board):
	rowcol = []
	for x in range(0,9):
		for y in range(0,9):
			if (board[x][y] == 0):
				rowcol.append(x)
				rowcol.append(y)
				return rowcol

# determines which 3x3 grid the cell is in
def getPosition(rowCol):
	position = (rowCol + 1)/3

	shiftedPos = 0
	if (position <= 1):
		shiftedPos = 0
	elif (position <= 2):
		shiftedPos = 3
	else:
		shiftedPos = 6

	return (shiftedPos)

# validates number being placed, checks row, column and 3x3 grid
def isValid(row, col, num, board):
	isRowValid = True
	isColValid = True
	isGridValid = True

	for i in range(0,9):
		if (board[row][i] == num):
			isRowValid = False

	for i in range(0,9):
		if (board[i][col] == num):
			isColValid = False

	xpos = getPosition(col)
	ypos = getPosition(row)

	for i in range(0,3):
		for j in range(0,3):
			if (board[ypos+i][xpos+j] == num):
				isGridValid = False

	return(isRowValid and isColValid and isGridValid)

# utilizes backtracking algorithm to solve board
def solve(board):
	pos = findEmpty(board)

	if(pos == None):
		print("solved")
		return True

	row = pos[0]
	col = pos[1]

	for num in range(1,10):
		if (isValid(row, col, num, board)):
			board[row][col] = num
			if (solve(board)):
				return True
	board[row][col] = 0


board = [
		[0,7,0,0,0,0,0,0,9],
		[5,1,0,4,2,0,6,0,0],
		[0,8,0,3,0,0,7,0,0],
		[0,0,8,0,0,1,3,7,0],
		[0,2,3,0,8,0,0,4,0],
		[4,0,0,9,0,0,1,0,0],
		[9,6,2,8,0,0,0,3,0],
		[0,0,0,0,1,0,4,0,0],
		[7,0,0,2,0,3,0,9,6]
		]

printBoard(board)
solve(board)
printBoard(board)


