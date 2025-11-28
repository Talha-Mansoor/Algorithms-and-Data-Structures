#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long


def expression(t):
    #checks for None case and one node
    if t is None:
        return 0

    elif not t.left and not t.right:
        return t.data
    #recurses through left and right sides. Converts values to strings and adds spaces for signs
    else:
        left_side=expression(t.left)
        right_side=expression(t.right)
        return "(" + str(left_side) +" " + str(t.data)+ " " + str(right_side) + ")"
