# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Defines a few example trees

import treenode as tn


atree = tn.treenode(2)
a = tn.treenode(7)
b = tn.treenode(5)
atree.left = a
atree.right =  b
c = tn.treenode(11)
d = tn.treenode(6)
a.left = c
a.right = d

# an empty tree with a bad pun: it's empty.  Say mtree out loud.  
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
