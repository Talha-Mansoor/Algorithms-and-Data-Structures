#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long


#Importing numpy module to use arrays to represent sudoku board
import numpy as np
Example=[1,2,3,4,5,6,7,8,9]
temp = []
List = []



def array(x):
    '''
Purpose: Read Data fil, create an array and Assign N
Pre-conditions:
      :param: a txt file with first line with value of N and a 3x3 Sudoku board underneath with integers
Post-conditions:  Nonep
Return: Array with data provided inside it.
'''


    test= open(x,"r")

    #For loop goes through file line by line, cleans the text and then adds it to list  and take out N
    for row in test:
        line=[]
        List.append(line)
        for y in row.rstrip().split():
            line.append(int(y))
    global N
    N=List.pop(0)
    N=N.pop(0)
    print('All Numbers are',List)
    #print('N is', N)
    return np.array(List)



#Calling Array Function
#Name can be changed to change file if in same directory

a=array("sudoku4.txt")
#print("ARRAY is \n",a)
k=a.shape
print("Dimensions are",k)
#print(k[0])



def check (z):
    '''
 Purpose: Check validity of Sudoku puzzle
 Pre-conditions:
       :param: anything. it doesnt matter. Unused
 Post-conditions:
        Variety of New Variables created depending on circumstances
 Return: Prints True or False
 '''

    '''Putting elements of sublitst from original List into a new list.
    for i in List:
    '''

    list_single=[j for i in List for j in i]
    print("List is",list_single)

    #Checking Numbers 1-9. If anything lower or higher is present then it's automatically False
    for row in a:
         for h in row:
             if h>9 or h<1:
                 print("False")
                 return None
                # print("False because number out of range",h)
    #checking squares in larger boards
    #iterating through each square 3x3 block and adding them to a list.
    if N > 3:
        for row in range(0,N,3):
            for column in range(0,N,3):

                f=row+3
                d=column+3

                for r in range(row, f):
                    #print("r",r)
                    for c in range(column, d):
                        #print("c",c)
                        if c==9:
                            if r==9:
                                r-=1
                                c-=1
                                temp.append(a[r,c])
                                print(a[r,c])
                        elif r==9:
                            if c==9:
                                r -= 1
                                c -= 1
                                temp.append(a[r,c])
                        else:

                            temp.append(a[r,c])
        #print("temp",temp)
        #Making Sublists out of every 9 numbers which are the numbers in a block
        Compare= [temp[i:i + 9] for i in range(0, len(temp), 9)]
        #print(Compare)

        #Checking Every block with an Example List of numbers 1-9
        TrueFalse=[]
        for x in Compare:
            if sorted(x)==Example:
                Set = set(x)
                Duplicate = len(x) != len(Set)
                if Duplicate == False:
                    TrueFalse.append(True)
                    #print("True")
            else:
                TrueFalse.append(False)
               # print("False")
        #print(TrueFalse)
        #returning True or False depending on if all Blocks are Valid or not
        def all_true(iterable):
             for item in iterable:
                 if not item:
                     return False
             return True
        l=all_true(TrueFalse)
        print(l)



#For 3x3 Boards, Check for Duplicates and compare the sorted copy of list to exapmle list to check Validity

    if N==3:
        Set = set(list_single)
        Duplicate= len(list_single) != len(Set)
        if Duplicate==False:
            if N==k[0] and N==k[1]:
                if sorted(list_single)==Example:
                    print("True")
                else:
                    print("False")
            else:
                print("False")

        else:
            print("False")
#Calling the check Function to Check size of board and every 3x3 block for duplicates and number range.

check(1)
