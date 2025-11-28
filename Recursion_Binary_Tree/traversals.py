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
#   Defines simple traversals for treenode (primitive) trees.
#
#   A primitive tree is is like a node-chain; treenodes linked together
#   We will build different kinds of Trees using primitive trees,
#   just as we built Stacks, QUeues and LLists out of node-chains
#
# These traversals print the data values stored in a primitive tree.

import treenode as tn
import SimpleQueue as Q

def in_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        in_order(tnode.left)
        print(tnode.data, end=" ")
        in_order(tnode.right)


def pre_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        print(tnode.data, end=" ")
        pre_order(tnode.left)
        pre_order(tnode.right)


def post_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        post_order(tnode.left)
        post_order(tnode.right)
        print(tnode.data, end=" ")


def breadth_order(tnode):
    """
    Display the nodes of a tree in breadth-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    explore = Q.SimpleQueue()
    explore.enqueue(tnode)

    while explore.size() > 0:
      current = explore.dequeue()
      print(current.data, end=" ")
      if current.left is not None:
          explore.enqueue(current.left)
      if current.right is not None:
          explore.enqueue(current.right)

