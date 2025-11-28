#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

import a5q5_Container as C

class Stack(C.Container):

    def __init__(self):
        C.Container.__init__(self)

    def push(self, value):
        """
        Purpose
            adds the given data value to the stack
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)"""
        return C.Container.insert_into_front(self,value)
    def pop(self):
        """
        Purpose
            Removes and returns a data value from the stack.
            Note: the stack cannot be empty!
        Post-condition:
            the first value is removed from the stack
        Return:
            the first value in the stack, or None"""

        C.Container.remove_from_front(self)

        #TO REMOVE ACCESS TO REMOVE FROM BACK
    def Queue_remove_back(self):
        raise AttributeError("'Stack cannot remove from back'")

stack=Stack()
print("EMPTY:",stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.to_string())
stack.pop()
print(stack.to_string())
print(stack.peek())


