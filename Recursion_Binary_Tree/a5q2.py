#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

import treenode as tn
import treefunctions as  tf
def subst(tnode, t, r):
    '''
    Purpose:
        To substitute a target value t with a replacement value r wherever it
        appears in the given tree.
    PreConditions:
        :param tnode: treenode
        :param t: target val
        :param r: replacement val
    Post Conditions:
        modifies the given tree.
    :return:
        Returns None
    '''

    #BASE CASE: checks for None and for target value
    if tnode==None:
        return None
    elif tnode.data==t:
        tnode.data=r

    #RECURSSIVE CASE: recurses through all of left and right sides of tree
    else:
        return subst(tnode.left,t,r) or subst(tnode.right,t,r)


def copy(tnode):
    '''
    Purpose:
        To create an exact copy of the given tree, with completely new treenodes, but
        exactly the same data values, in exactly the same places.

    Preconditions:
        :param tnode: Treenode to be copied
    Post Conditions:
        Original Tree unmodified
    :return:
        If tnode is None, return None.
        If tnode is not None, return a reference to the new tree.
    '''
    # Check None Base case
    if tnode==None:
        return None
    #Clone root then recurse through left and then right sides to copy them.
    else:
         clone=tn.treenode(tnode.data)
         clone.left = copy(tnode.left)
         clone.right = copy(tnode.right)

         return clone



List=[]
def collect_data_inorder(tnode):
    """
    Purpose:
        To collect all the data values in the given tree.
    Pre Conditions:
        :param tnode: Treenode
    Post Conditions:
        Treenode unchanged.
    :return:
        Returns a list of all the data values, and the data values appear in the list
        according to the in-order sequence.
    """
    #BASE CASE: NONE
    if tnode is None:
        return []
    #RECURSIVE CASE: Recurse through tree in-order and append values to list
    else:
        data = collect_data_inorder(tnode.left)
        data.append(tnode.data)
        data += collect_data_inorder(tnode.right)
        return data




def count_smaller(tnode, target):
    """
    Purpose:
        Count the number of data values in the given tree that are less than the given target value.
    Pre Conditions:
         Assume that the given tree has data values that are number only.
        :param tnode: Treenode
        :param target: Integer Value to compare rest to.
    Post Conditions:
        None
    :return:
         Number of values smaller than target
    """
    #Similar to count function. Return 0 for None Base case
    if tnode is None:
        return 0
    #For target value add 1 and recurse through left and right
    elif tnode.data<target:
        return 1+count_smaller(tnode.left,target)+count_smaller(tnode.right,target)
    #For rest keep on recursing
    else:
      return count_smaller(tnode.left,target)+count_smaller(tnode.right,target)

