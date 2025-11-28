#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long


import math as m

def ordered(tnode):
    def checker(new, min, max):
        #Base case None check
        if new is None:
            return True
        #Left and right values checked for min and max, Left and right subtrees checked recursively
        if new.data < min or new.data > max:
            return False
        return (checker(new.left, min, new.data -1) and checker(new.right, 1 + new.data, max))

    return checker(tnode, -m.inf, m.inf)

