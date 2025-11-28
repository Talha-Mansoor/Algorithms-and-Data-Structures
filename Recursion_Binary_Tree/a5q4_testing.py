



#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

import treenode as tn
import a5q4
metree = None
atree=tn.treenode(5)
fibonatree = tn.treenode(5,tn.treenode(2,tn.treenode(1,None,None),
                                     tn.treenode(1,tn.treenode(0,None,None),
                                                 tn.treenode(1,None,None))),
                         tn.treenode(3,tn.treenode(1,tn.treenode(0,None,None),
                                                 tn.treenode(1,None,None)),
                                     tn.treenode(2,tn.treenode(1,None,None),
                                                 tn.treenode(1,tn.treenode(0,None,None),
                                                             tn.treenode(1,None,None)))))

Correctree = tn.treenode(5,
                         tn.treenode(3,
                                     tn.treenode(2),tn.treenode(4)),
                         tn.treenode(7,
                                     tn.treenode(6),tn.treenode(8)))

list=[]
list.append(a5q4.ordered(atree)==True)
list.append(a5q4.ordered(metree)==True)
list.append(a5q4.ordered(fibonatree)==False)
list.append(a5q4.ordered(Correctree)==True)

if False not in list:
    print("TESTING DUN> NO ERROR FOUND")
else:
    print("ERROR EXISTS")
