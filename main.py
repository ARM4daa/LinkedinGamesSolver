"""
main.py

Entry point of the program.
The user choose the game to solve and the program use the corresponding scrapping/extractor/solver.

Author : Baptiste FARCY (ARM4da)
Date : June 2026
"""

# -- Importations --
from core.gamesScraper import scraping
from games.sudoku.numbersCollectorSudoku import numbersCollectorHtml, numbersCleaner
from games.sudoku.solverSudoku import solutionFinder

def main() :
    choice = int(input("Which game would you solve ?\n- 1 : Sudoku\nChoice : "))
    match choice :
        case 1 :
            scraping("content.txt","https://www.linkedin.com/games/view/mini-sudoku/desktop")
            sudokuDirtyLines = numbersCollectorHtml("content.txt")
            sudokuCleanedLines = numbersCleaner(sudokuDirtyLines)
            print("Solution :")
            if solutionFinder(sudokuCleanedLines) :
                for line in sudokuCleanedLines :
                    print(line)
            else: 
                print("Solution not found")

if __name__=="__main__":
    main()