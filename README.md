# SudokuSolver
Solves a sudoku board using backtracking algorithm. 
To solve the board, I find the first empty cell and I check whether a number from one to nine can be placed there by checking the constraints and rules of sudoku.
If the number is valid and can be placed there, I find the next empty cell and I try to place another number there and so on. 
If a cell cannot place a number from one to nine, I go back to the previous empty cell and try another number and so on. 
The sudoku is solved with backtracking when there are no more empty cells. 
