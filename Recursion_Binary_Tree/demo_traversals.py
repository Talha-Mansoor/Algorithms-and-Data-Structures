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
#   A demonstation of the script traversals.py

import treenode as tn
from traversals import pre_order, in_order, post_order, breadth_order
import treefunctions as tf
import exampletrees as egt

# Create the tree we've been using in class
#  - this is one of the dozens of ways to create the tree
root = tn.treenode(2)
a = tn.treenode(7)
b = tn.treenode(5)
root.left = a
root.right = b
c =  tn.treenode(11)
d =  tn.treenode(6)
a.left = c
a.right = d

print("Pre-order traversal:", end=" ")
pre_order(root)
print()
print("In-order traversal:", end=" ")
in_order(root)
print()
print("Post-order traversal:", end=" ")
post_order(root)
print()
print("Breadth-order traversal:", end=" ")
breadth_order(root)
print()

print(tf.to_string(egt.fibonatree))