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
#   Defines some helpful functions for trees
#

def is_leaf(tnode):
    """
    Purpose:
        Determine if tnode is a leaf.
    Pre-conditions:
        :param tnode: a treenode
    Return:
        True if the tnode has zero children
    """
    return tnode.left is None and tnode.right is None


def to_string(tnode, level=0):
    """
    Produce a formatted string to represent the hierarchy of
    a tree.  Tree diagrams usually have the root at the top.
    Here the root is at the top left.
    - every data value appears on its own line
    - the levels of a tree are columns from left to right
    - nodes at the same level start in the same column
    - very long data values might cause the presentation to get messy
    - subtrees appear below a parent
      - left subtree immediately
      - right subtree after the entire left subtree
    Pre-conditions:
        :param tnode: a Binary tree (treenode or None)
        :param level: the level of the tnode (default value 0)
    Return:
        A string with the hierarchy of the tree.
    """
    if tnode is None:
        return 'EMPTY'
    else:
        result = '\t'*level
        result += str(tnode.data)
        if tnode.left is not None:
            result += '\n'+to_string(tnode.left, level+1)
        else:
            result += '\n'
        if tnode.right is not None:
            result += '\n'+to_string(tnode.right, level+1)
        return result
