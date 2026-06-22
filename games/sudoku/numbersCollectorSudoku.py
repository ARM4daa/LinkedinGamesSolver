"""
numbersCollectorSudoku

Collect the lines with the good values in the scrapped HTML and clean the lines just to have the numbers

Author : Baptiste FARCY (ARM4da)
Date : June 2026
"""

def numbersCollectorHtml(fileToRead:str) -> list[str] :
    
    """
        Collect the lines with the sudoku numbers in the HTML and put the lines in a list
        
        Args :
            - fileToRead (str) : Name of the file with the sudoku HTML
        
        Returns :
            - dirtyNumbers (list[str]) : List with the not cleaned values in string, found right after the "sudoku-cell-content" tag
    """
    
    dirtyNumbers = []
    next = False
    with open(fileToRead, "r") as file :
        for line in file :
            if "sudoku-cell-content" in line : #The name of the HTML tag before the sudoku values
                next = True
            elif next == True :
                dirtyNumbers.append(line)
                next = False
    print("Lines collected")
    return dirtyNumbers

def numbersCleaner(dirtyNumbers:list[str]) -> list[list[int]] :
    """
        Clean the lines to have the sudoku values and convert the numbers from string to integer
        
        Args :
            - dirtyNumbers (list[str]) : List of not cleaned lines extract from the HTML

        Returns :
            - cleanedList (list[list[int]]) : List with the cleaned values in integer who represents the 6x6 grid
    """
    cleanedList = []
    line = []
    count = 0
    for value in dirtyNumbers :
        if count == 6 :
            cleanedList.append(line.copy())
            line.clear()
            count = 0
        if value.isspace() :
            line.append(0)
        else :
            line.append(int(value.replace(" ","").replace("\n", "")))
        count += 1
    cleanedList.append(line)
    print("Lines cleaned")
    return cleanedList