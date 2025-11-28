#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long

import node as N
class Container(object):
    def __init__(self):
        self.__size = 0  #
        self.__front = None  # We will use front as top

    def size(self):
        """
        Purpose
            returns the number of data values in the stack or queue
        Return:
            The number of data values in the stack or queue
        """
        return self.__size

    def is_empty(self):
        """
        Purpose
            checks if the stack or queue has no data in it
        Return:
            True if the stack or queue has no data, or false otherwise
        """
        return self.__size == 0

    def remove_from_front(self):
        """
    Purpose
        Removes and returns a data value from the stack or queue.
        Note: the stack or queue cannot be empty!
    Post-condition:
        the first value is removed from the stack or queue
    Return:
        the first value in the stack or queue, or None
        """
        assert not self.is_empty()

        result = self.__front
        self.__front = self.__front.get_next()

        # check if it was last node.
        if self.__front is None:
            self.__back = None

        self.__size -= 1
        return result.get_data()
    def Queue_remove_back (self):
        assert not self.is_empty()

        if self.__size == 1:
            return self.remove_from_front()

        prev = self.__front
        current = prev.get_next()

        while current.get_next() is not None:
            prev = current
            current = current.get_next()

        prev.set_next(None)
        self.__back = prev
        self.__size -= 1
        return current.get_data()


    def insert_into_front(self, value):
        """
               Purpose
                   adds the given data value to the stack or queue
               Pre-conditions:
                   value: data to be added
               Post-condition:
                   the value is added to the stack or queue
               Return:
                   (none)
               """
        new_node = N.Node(value, self.__front)
        self.__front = new_node
        self.__size += 1


    def peek(self):
            """
            Purpose
                returns the value from the top of given stack or queue
                without removing it
                Note: the stack or queue cannot be empty!
            Post-condition:
                None
            Return:
                the value at the top of the stack or queue
            """
            assert not self.is_empty(), 'peeked into an empty stack'

            first_node = self.__front
            result = first_node.get_data()
            return result


    def to_string(self):
        if self.is_empty():
            result = 'EMPTY'
        else:
            walker = self.__front

            value = walker.get_data()
            result = str(value) + ' |'

            while walker.get_next() is not None:
                walker = walker.get_next()

                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'

        return result


