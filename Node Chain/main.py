#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long
import a3q3
import node as N
import a3q3 as S #to_string file used for testing


def sumnc(node_chain):
    """
    Purpose:
        Given a node chain with numeric data values, calculate
        the sum of the data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing
                           numeric data values
    Post-condition:
            None
    Return
            :return: the sum of the data values in the node chain
    """
    walker=node_chain
    add=0
    #None case
    if node_chain is None:
        return 0
    #Every node except last is added to add var and then last one too
    while walker.get_next() is not None:
        add+=walker.get_data()
        walker= walker.get_next()
    add+=walker.get_data()
    return add


def count_in(node_chain, value):
    """
    Purpose:
        Counts the number of times a value appears in a node chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param value: a data value
    Return:
        :return: The number times the value appears in the node chain
    """
    #NONE CASE
    if node_chain is None:
        return 0

    walker=node_chain
    count=0
    #Counting occurence of target in nodechain  by iterating through it
    while walker.get_next() is not None:
        if walker.get_data()==value:
            count+=1
        walker=walker.get_next()
    if walker.get_data()==value:
        count+=1
    return count


def replace_in(node_chain, target, replacement):
    """
    Purpose:
        Replaces each occurrence of the target value with the replacement
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a value that might appear in the node chain
        :param replacement: the value to replace the target
    Post-conditions:
        Each occurrence of the target value in the chain is replaced with
        the replacement value.
    Return:
        None
    """
    walker = node_chain
    previous = None
    target_node=walker

    #None case
    if walker is None:
        return "EMPTY"
    #EVery node except last in loop, check for target value and replace and connect it, if first then no connecting.
    else:
        while walker.get_next() is not None:
            if walker.get_data() == target:
                new=N.node(replacement)
                new.set_next(walker.get_next())
                if previous != None:
                    previous.set_next(new)
                    previous=new
                    walker = walker.get_next()
                    continue
                else:
                    node_chain.set_data(replacement)

            previous=walker
            walker = walker.get_next()

        if walker.get_data() == target and walker.get_next() is None:  #last node

            new = N.node(replacement)
            if previous !=None:
                previous.set_next(new)
            else:
                node_chain = node_chain.set_data(replacement)
    return None


'''
TESTING
chain=N.node(1,N.node(1,N.node(1,N.node(1,N.node(8,N.node(1,N.node(5,N.node(1))))))))
c=N.node(1)
em=None

print(a3q3.to_string(chain))

print(a3q3.to_string(replace_in(chain,1,10)))
print(a3q3.to_string(chain))

print(a3q3.to_string(chain))
print(a3q3.to_string(replace_in(c,1,0)))'''


#<node.node object at 0x0000023F62B5BAF0>