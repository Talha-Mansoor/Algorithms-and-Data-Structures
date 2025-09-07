#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long


import node as N

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post_conditions:
        None
    Return: A string representation of the nodes.
        NOTE: THIS VERSION OF THE FUNCTION IS KNOWN TO BE BROKEN!!!
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        # print the data
        result = '[ {} |'.format(str(value))

        #checking next value for None to ensure we don't go beyond last node
        while walker.get_next() is not None:
            walker = walker.get_next()
            value = walker.get_data()
            # represent the next with an arrow-like figure and add data of node into string
            result += ' *-]-->[ {} |'.format(str(value))

        # at the end of the chain, use '/'
        result += ' / ]'

    return result
'''
For testing purposes

chain=N.node(1,N.node('two',N.node(3)))
chain1=None

print ('chain --------->', to_string(chain))'''