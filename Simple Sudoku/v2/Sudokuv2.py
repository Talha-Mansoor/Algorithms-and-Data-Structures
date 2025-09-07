#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

def load_sudoku(fname):
    """
    Purpose: load a potential sudoku puzzle from given file name.
    Pre-conditions: fname refers to a text file.  First line is the sudoku dimension,
    subsequent lines are space-separated integers, one line per row
    Post-conditions: The file is unmodified.
    Return: A list-of-lists; each sublist contains the integers from each row
    of the input file
    """
    f = open(fname, "r")
    N = int(f.readline())
    sudoku = []
    for line in f:
        line = line.rstrip().split()
        for sindex in range(len(line)):
            line[sindex] = int(line[sindex])
        sudoku.append(line)

    f.close()
    return sudoku


def checkMini(sudoku):
    """
    Purpose: check 3x3 list of lists for integers 1-9
    Pre-conditions: S is list of 3 lists with 3 integers each.
    Post-conditions: None
    Return: True if S has all 9 integers and vice versa
    """

    CheckList = 9*[False]
    for row in sudoku:
        for column in row:

            if int(column) > 0 and int(column) < 10:
                CheckList[int(column) - 1] = True
    #print(CheckList)
    if False not in CheckList:
        return True
    else:
        return False

def check(Sudoku):
    """
    Purpose: checks 3x3 block of sudoku for 9 digits
    Pre-conditions: Sudoku is a list of lists of square dimensions of integers 1-9
    Post-conditions: unmodified Sudoku.
    Return: True if Sudoku is Valid and vice versa
    """
    # safety check to make sure we have a sudoku square
    if len(Sudoku) % 3 != 0:
        return False
    for row in Sudoku:
        if len(row) != len(Sudoku):
            return False
    # iterate through 3x3 blocks of sudoku one by one and check validity of each one
    Answer = True
    for x in range(0, len(Sudoku), 3):
        for y in range(0, len(Sudoku), 3):

            square = [Sudoku[r][y:y + 3] for r in range(x, x + 3)]
            # print(square)
            Answer = Answer and checkMini(square)

    return Answer



'''Change this to change files 
        \/                     '''
fname = "sudoku4.txt"


sudoku_global = load_sudoku(fname)
print(sudoku_global)

# open file to get value for N
f = open(fname, "r")
N = int(f.readline())
#print(N)


if N == 3:
    print(checkMini(sudoku_global))
elif N>3:
    print(check(sudoku_global))
