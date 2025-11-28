#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

import a5q2
import treenode as tn


atree = tn.treenode(2)
mtree = None

# a tree with one node only.  Yes, a bad pun too.
ctree = tn.treenode('si')

# a larger more e-xtree-me tree
xtree = tn.treenode(5,
              tn.treenode(1,None,
                        tn.treenode(4,
                                  tn.treenode(3,tn.treenode(2,None,None),None),
                                  None)),
              tn.treenode(9,tn.treenode(8,tn.treenode(7,tn.treenode(6,None,None),None),None),
                          tn.treenode(1,tn.treenode(3,None,None),tn.treenode(3,None,None))))


# and you thought puns wouldn't get worse...
fibonatree = tn.treenode(5,tn.treenode(2,tn.treenode(1,None,None),
                                     tn.treenode(1,tn.treenode(0,None,None),
                                                 tn.treenode(1,None,None))),
                         tn.treenode(3,tn.treenode(1,tn.treenode(0,None,None),
                                                 tn.treenode(1,None,None)),
                                     tn.treenode(2,tn.treenode(1,None,None),
                                                 tn.treenode(1,tn.treenode(0,None,None),
                                                             tn.treenode(1,None,None)))))


# a tree with some meaning
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



def identicalTrees(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left) and
                identicalTrees(a.right, b.right))

#subst() testing:
subst_check=[]
#TEST 1 empty tree
x=a5q2.subst(mtree,8,7)
if x ==None:
    subst_check.append(True)
else:
    subst_check.append(False)


#TEST 2 Multiple children and roots
a5q2.subst(xtree,7,0)
new=tn.treenode(5,
              tn.treenode(1,None,
                        tn.treenode(4,
                                  tn.treenode(3,tn.treenode(2,None,None),None),
                                  None)),
              tn.treenode(9,tn.treenode(8,tn.treenode(0,tn.treenode(6,None,None),None),None),
                          tn.treenode(1,tn.treenode(3,None,None),tn.treenode(3,None,None))))


if identicalTrees(xtree,new):
    subst_check.append(True)
else:
    subst_check.append(False)




#TEST 3 one node
a5q2.subst(atree,2,3)
new=tn.treenode(3)

if identicalTrees(atree,new):
     subst_check.append(True)
else:
    subst_check.append(False)



if False not in subst_check:
    print("subst() corect")
else:
    print("error found in subst")

#_________________________________________________________________________________________

#Copy() testing:
#TEST 1 Empty
copy_check=[]
x= a5q2.copy(mtree)
if x==None:
    copy_check.append(True)
else:
    copy_check.append(False)

#TEST 2 MOre than one node
x=a5q2.copy(xtree)



copy_check.append(identicalTrees(mtree,xtree))


#TEST 3 One node
x=a5q2.copy(atree)

copy_check.append(identicalTrees(x,atree))


if False not in copy_check:
    print("copy() corect")
else:
    print("error found in copy()")

#----------------------------------------------------------------------------------------------

#collect_data_inorder
collect_check=[]
#TEST 1
list=[]
x=a5q2.collect_data_inorder(mtree)

if x==list:
    collect_check.append(True)
else:
    collect_check.append(False)



#TEST 2 One node
atree = tn.treenode(2)
x=a5q2.collect_data_inorder(atree)
list=[2]
if x==list:
    collect_check.append(True)
else:
    collect_check.append(False)



#TEST 3 Multiple Nodes
xtree = tn.treenode(5,
              tn.treenode(1,None,
                        tn.treenode(4,
                                  tn.treenode(3,tn.treenode(2,None,None),None),
                                  None)),
              tn.treenode(9,tn.treenode(8,tn.treenode(7,tn.treenode(6,None,None),None),None),
                          tn.treenode(1,tn.treenode(3,None,None),tn.treenode(3,None,None))))

x=a5q2.collect_data_inorder(xtree)
list=[1,2,3,4,5,6,7,8,9,3,1,3]
if x==list:
    collect_check.append(True)
else:
    collect_check.append(False)


if False not in collect_check:
    print("collect_data_inorder corect")
else:
    print("error found in collect_data_inorder")

#----------------------------------------------------------------------------------------------
#count_smaller
smaller_check=[]
#TEST 1 None

if a5q2.count_smaller(mtree,3)==0:
    smaller_check.append(True)
else:
    smaller_check.append(False)

#TEST 2 One node

if a5q2.count_smaller(atree,3)==1:
    smaller_check.append(True)
else:
    smaller_check.append(False)

#TEST 3 None

if a5q2.count_smaller(xtree,4)==6:
    smaller_check.append(True)
else:
    smaller_check.append(False)

if False not in smaller_check:
    print("count_smaller() corect")
else:
    print("error found in count_smaller()")

if False not in smaller_check or collect_check or copy_check or subst_check:
    print("*_______________________________*\nTESTING COMPLETE NO ERRORS FOUND")