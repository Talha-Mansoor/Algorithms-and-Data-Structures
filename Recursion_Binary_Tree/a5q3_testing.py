#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long
import treenode as tn
import a5q3


#TREES \/_____________________________________________________________
expr_tree = tn.treenode('*',
                  tn.treenode('+',
                            tn.treenode('+',
                                      tn.treenode(2.0, None, None),
                                      tn.treenode(3.0, None, None)),
                            tn.treenode(3.0, None, None)),
                  tn.treenode('+',
                            tn.treenode(4.0, None, None),
                            tn.treenode('/',
                                      tn.treenode(2.0, None, None),
                                      tn.treenode('+',
                                                tn.treenode(89.0, None, None),
                                                tn.treenode(3.0, None, None)))))


atree = tn.treenode(2)
mtree = None
e_tree =tn.treenode('-',
                            tn.treenode('+',
                                      tn.treenode(1, None, None),

                            tn.treenode(4, None, None)),
                  tn.treenode('+',
                            tn.treenode(4.7, None, None),
                            tn.treenode('*',
                                      tn.treenode(2.6, None, None),
                                      tn.treenode('+',
                                                None,
                                                tn.treenode(3.9, None, None)))))


example = tn.treenode('*',
                            tn.treenode('+',
                                      tn.treenode(4, None, None),
                                      tn.treenode(13, None, None)),
                  tn.treenode('-',
                            tn.treenode(9, None, None),
                            tn.treenode(5,None,None)))




#CHECKS___________________________________________________

check=[]
#Multiple branches
if a5q3.expression(expr_tree) == '(((2.0 + 3.0) + 3.0) * (4.0 + (2.0 / (89.0 + 3.0))))':
    check.append(True)
else:
    check.append(False)

#Empty
if a5q3.expression(mtree) == 0:
    check.append(True)
else:
    check.append(False)

#One node
if a5q3.expression(atree) == 2:
    check.append(True)
else:
    check.append(False)

#Single sided Branches
if a5q3.expression(e_tree) == '((1 + 4) - (4.7 + (2.6 * (0 + 3.9))))':
    check.append(True)
else:
    check.append(False)

#ASSIGNMENT EXAMPLE
if a5q3.expression(example)=="((4 + 13) * (9 - 5))":
    check.append(True)
else:
    check.append(False)

#CHECK IF ALL CORRECT
if False not in check:
    print("TESTING DONE. ALL CORRECT.")
else:
    print("ERROR EXISTS")
