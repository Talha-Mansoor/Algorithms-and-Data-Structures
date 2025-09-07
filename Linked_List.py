#Name: Talha Mansoor
#NSID: kgy284
#Student Number:11346490
#Course Number: CMPT-145
#Instructor: Jeff Long


class node(object):
    """ A version of the Node class with public attributes.
        This makes the use of node objects a bit more convenient for
        implementing LList class.

        Since there are no setters and getters, we use the attributes directly.

        This is safe because the node class is defined in this module.
        No one else will use this version of the class.
    """

    def __init__(self, data, next=None):
        """
        Create a new node for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the node
            next:  Another node (or None, by default)
        """
        self.data = data
        self.next = next

    # Note: use the attributes directly; no setters or getters!


class LList(object):
    def __init__(self):
        """
        Purpose
            creates an empty list
        """
        self._size = 0  # how many elements in the stack
        self._head = None  # the node chain starts here; initially empty
        self._tail = None

    def is_empty(self):
        """
        Purpose
            Checks if the given list has no data in it
        Return:
            :return True if the list has no data, or False otherwise
        """

        return self._size ==0

    def size(self):
        """
        Purpose
            Returns the number of data values in the given list
        Return:
            :return The number of data values in the list
        """
        return self._size

    def prepend(self, val):
        """
        Purpose
            Insert val at the front of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is at index 0.
            The values previously in the list appear after the new value.
        Return:
            :return None
        """
        # MAke new node and assign it to the head. Make previous head the next for it. Special case for empty
        new_node=node(val,self._head)
        if self._head==None:
            self._head = new_node
            self._tail = self._head
        else:
            self._head=new_node
        self._size+=1


        pass

    def append(self, val):
        """
        Purpose
            Insert val at the end of the node chain
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            The list increases in size.
            The new value is last in the list.
        Return:
            :return None
        """
        #Make new node with given value and add it to the tail and attach the previous tail's next to it.
        # If empty then its the only node
        new_node = node(val, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            self._size+=1

        else:
            previous_tail = self._tail
            self._tail = new_node
            previous_tail.next = self._tail
            self._size+=1

        pass

    def get_index_of_value(self, val):
        """
        Purpose
            Return the smallest index of the given val.
        Preconditions:
            :param val:   a value of any kind
        Post-conditions:
            none
        Return:
            :return True, idx if the val appears in self
            :return False, None if the vale does not appear in self
        """

        index=0
        walker=self._head
        while walker:
            if walker.data == val:
                return True, index
            else:
                walker=walker.next
                index+=1
        return False


    def remove_from_front(self):
        """
        Purpose
            Removes and returns the first value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair (True, value) if self is not empty
            :return The pair (False, None) if self is empty
        """
        if self.size==0:
            return False,None
        elif self.size() == 1:
            self._tail = None
        remove_node = self._head
        self._head = remove_node.next
        self._size -= 1
        return True, remove_node.data


    def remove_from_back(self):
        """
        Purpose
            Removes and returns the last value
        Post-conditions:
            The list decreases in size.
            The returned value is no longer in in the list.
        Return:
            :return The pair True, value if self is not empty
            :return The pair False, None if self is empty
        """
        if self._size==0:
            return False, None

        elif self.size() == 1:

            removed = self._head
            self._size = 0
            self._tail = None
            self._head = None
            return True, removed.data

        #Size 1 and 0 have special case
        #while loop iterates through node chain makes second last the tail and makes it's next None

        walker = self._head
        Next_node = walker.next
        while Next_node.next is not None:
            walker = Next_node
            Next_node = Next_node.next

        self._tail = walker
        walker.next = None
        self._size -= 1
        return True, Next_node.data

    def retrieve_data(self, idx):
        """
        Purpose
            Return the value stored at the index idx
        Preconditions:
            :param idx:   a non-negative integer
        Post-conditions:
            none
        Return:
            :return (True, val) if val is stored at index idx and idx is valid
            :return (False, None) if the idx is not valid for the list
        """
        # Checking Correctness of Index
        if idx < 0:
            return False, None
        elif idx >= self.size():
            return False, None
        walker = self._head
        count = 0

        #Walker walks to node index through comparison of indx and count and then retrives data
        while walker is not None and count < idx:
            walker = walker.next
            count += 1
        return True, walker.data


    def set_data(self, idx, val):
        """
        Purpose
            Store val at the index idx
        Preconditions:
            :param val:   a value of any kind
            :param idx:   a non-negative integer
        Post-conditions:
            The value stored at index idx changes to val
        Return:
            :return True if the index was valid, False otherwise
        """
        #Checking Correctness of Index
        if idx < 0:
            return False
        elif idx >= self.size():
            return False
        walker = self._head
        count = 0

        #walk to index and put data equal to value
        while walker is not None and count < idx:
            count += 1
            walker = walker.next

        walker.data = val
        return True


'''
list=LList()

print(list.append(3))
print(list.append(7))
print(list.append(5))
print(list.size())
print(list.get_index_of_value(7))
'''