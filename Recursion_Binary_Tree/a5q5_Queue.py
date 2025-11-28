#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

import a5q5_Container as C

class Queue(C.Container):
    def __init__(self):
       C.Container.__init__(self)
       self.__back = None

    def enqueue(self, value):
        """
        Purpose
            adds the given data value to the queue
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the queue
        Return:
            (none)
        """
        C.Container.insert_into_front(self, value)

    def dequeue(self):
        """
        Purpose
            removes and returns a data value from the queue
            Note: the queue cannot be empty!
        Post-condition:
            the first value is removed from the queue
        Return:
            the first value in the queue, or None
        """
        return C.Container.Queue_remove_back(self)

    # TO REMOVE ACCESS TO REMOVE FROM FRONT
    def remove_from_front(self):
        raise AttributeError("'Queue cannot remove from front'")

queue= Queue()
print("EMPTY:",queue.is_empty())
queue.insert_into_front(7)
queue.insert_into_front(8)
print("FRONT:",queue.peek())
queue.enqueue(9)
queue.enqueue(10)
print("SIZE:",queue.size())
print(queue.to_string())
queue.dequeue()
print(queue.to_string())



