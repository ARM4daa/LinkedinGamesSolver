"""
solverSudoku.py

Solve the grid (6x6) of LinkedIn sudoku. The algorithm to solve this problem is a Backtracking algorithm.
Warning : The performance to execute this algorithm aren't the bests in Python.
Advice : If you want a better result, you should used the C or the Rust. 
A bloc has 6 numbers, each bloc has 2 lines and 3 columns.

Author : Baptiste FARCY (ARM4da)
Date : June 2026
"""

def freeCaseFounder(sudoku:list[list[int]]) -> tuple | None:
    
    """
        Find a free case in the sudoku
        
        Args :
            - sudoku (list[list[int]]) : Represent the sudoku grid in a list of list of int

        Returns :
            - (row, column) (tuple[int,int] | None) : The coordinate of the first empty cell found, or None if the grid is full
    """

    for row in range(6):
        for column in range(6) :
            if sudoku[row][column] == 0 :
                return (row,column)
    return None


def possibleValue(sudoku:list[list[int]], row:int, column:int, value:int) -> bool :
    
    """
        Check if a specified value is available in a case defined by (row,column)
        
        Args :
            - sudoku (list[list[int]]) : Represent the sudoku grid in a list of list of int
            - row (int) : Row of the case to test the value
            - column (int) : Column of the case to test the value
            - value (int) : The value to test in the case

        Returns :
            - (bool) : return "True" if the value specified can be in the case (row, column), else return "False" 
    """
    
    if value in sudoku[row]:
        return False
    
    if value in [sudoku[i][column] for i in range(6)]:
        return False
    
    blocRow = (row//2)*2
    blocColumn = (column//3)*3
    for i in range(blocRow, blocRow+2):
        for j in range(blocColumn, blocColumn+3):
            if sudoku[i][j] == value:
                return False
    return True

def solutionFinder(sudoku:list[list[int]]) -> bool :
    
    """
        Verify if the sudoku grid is full. If not, it will find the values to put in the free cases.
        
        Args :
            - sudoku (list[list[int]]) : Represent the sudoku grid in a list of list of int

        Returns :
            - (bool) : return "True" if grid is full, else return "False" 
    """
    
    case_vide = freeCaseFounder(sudoku)
    
    if case_vide is None:
        return True
    
    row, column = case_vide
    
    for value in range(1, 7):
        if possibleValue(sudoku, row, column, value):
            sudoku[row][column] = value
            
            if solutionFinder(sudoku):
                return True
            
            sudoku[row][column] = 0
    
    return False