# Copyright 2023, Oliver S. Schneider
# Copyright 2013, Michael H. Goldwasser
#
# Adapted from the Dynamic Array object, which was
# developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author: Karla Castro
# Student ID: 20745522
# Email: kmcastro
# Assingment 3
# Date: Dec 04, 2023
# Description: This program implements a linked list class and its methods

class ListNode:
  """A node in a linked list"""

  def __init__(self, data, next=None):
    """Constructor"""
    self.data = data # value
    self.next = next # reference to next node


class LinkedList:
  """ LinkedList
    A simplified List implemented using linked nodes.
    Uses explicit "get" and "set" functions rather
    than sequence indexing notation.
  """

  def __init__(self):
    """Create an empty list."""
    self.head = None # empty list with no head
    self._length = 0 # empty list with 0 length


  ###################
	#    Accessors    #
	###################

  def length(self) -> int:
    """Return number of elements stored in the linked list."""
    return self._length
  

  def contains(self, value, map_to_key=lambda x : x) -> bool:
    """ contains
      Returns True if value is in the list, False otherwise
      
      map_to_key: an optional mapping function from the stored
        object type to the key to compare with.
    """
    # Returns True if the value is in the list
    return self.find_index_byvalue(value, map_to_key=map_to_key) >= 0


  def find_index_byvalue(self, value, map_to_key=lambda x : x) -> int:
    """ find_index_byvalue
      Returns the first index of value, or -1 if not found
      
      value: the value to find as an object,
        or the key to compare to (if using map_to_key)

      map_to_key: an optional mapping function from the stored
        object type to the key to compare with.
    """
    # for loop to iterate through the linked list
    for i in range(self.length()):
      # checks if the value is in the list
      # compares the value to the key of the current node
      if map_to_key(self.get(i)) == value:
        # returns the index of the value
        return i
    return -1


  def get(self, k : int) -> object:
    """Return element at index k
      k: index of element to retrieve
      returns: current.data
    """
    # check if k is in range
    if not 0 <= k < self._length:
      # raise an error if k is out of range
      raise IndexError("Index k out of range")
    # set current to reference the head of the linked list
    current = self.head
    # iterate through the list until current reaches the kth node
    for i in range (k):
      # check if current is not None and the node is valid at the current position
      if current is not None:
        # set current to reference the next node
        current = current.next
      else:
        # raise an error if current is None
        raise IndexError("Index out of range")
    # returns the data stored in the kth node
    return current.data
    

  ##################
	#    Mutators    #
	##################

  # def _get_node_k(self, k):
  #   """ Optional private helper function """
  #   # TODO: stub
  #   return None


  def set(self, k, value):
    """Set element at index k
      k: index of element to set
      value: value to set
    """
    # check if k is in range
    if not 0 <= k < self._length:
      # raise an error if k is out of range
      raise IndexError("Index k our of range")
    # set current to reference the head of the linked list
    current = self.head
    # iterate through the list until current reaches the kth node
    for i in range(k):
      # Update current to point to the next node in the list
      current = current.next
      # check if current index is out of range by checking if it is None 
      if current is None:
        raise IndexError("Index out of range")
    # set the data of the kth node to the value
    current.data = value


  def append(self, obj):
    """Add object to end of the array
      obj: object to add
    """
    # create a new list node with obj
    new_list_node = ListNode(obj)
    if not self.head:
      # if the list is empty, set the new node as the head
      self.head = new_list_node
    else:
      # if the list is not empty, set current to the head
      current = self.head
      while current.next:
        # iterate until the last node is reached
        current = current.next
      # set the next node to reference the new node
      current.next = new_list_node
    # increment the length of the list
    self._length += 1


  def insert(self, k, value):
    """Insert value at index k, shifting subsequent values rightward.
      k: index to insert value at
      value: value to insert
    """
    # NOTE: 0 <= k <= n is okay
    # TODO: stub
    # check if k is in range
    if k < 0 or k > self._length:
      raise IndexError("Index out of range")
    # create a new node
    new_node = ListNode(value)
    # check first index
    if k == 0:
      # sets the new node to reference the head
      new_node.next = self.head
      # adjust the next pointer
      self.head = new_node
    else:
      current = self.head
      for i in range(k -1):
        # iterate through the list to the node before the kth node
        current = current.next
      # set the next node of the new node to the next node of the current node
      new_node.next = current.next
      # set the next node to the new node
      current.next = new_node
    # increment the length of the list
    self._length += 1


  def remove(self, k : int) -> object:
    """Remove the value at index k, returning it
      k: index of element to remove
      returns: the removed value
    """
    # check if k is in range
    if k < 0 or k >= self._length:
      # raise an error if k is out of range
      raise IndexError("Index out of range")
    if k == 0:
      # update head when removing at index 0
      removed_value = self.head.data
      # sets head to reference the next node
      self.head = self.head.next

    else:
      # set current to the head
      current = self.head
      for i in range(k - 1):
        # iterate through the list to the node before the kth node
        current = current.next
      # set the removed value to the data of the kth node
      removed_value = current.next.data
      current.next = current.next.next
    # reduce the length of the list
    self._length -= 1
    return removed_value 


	#################
	#    Sorting    #
	#################

  # def _swap(self, i : int, j : int):
  #   """_swap
  #     Optional private helper function to swap two objects in place.
  #     Intended to help with sorting algorithms
  #   """
  #   # TODO: stub
  #   pass


  def sort(self, map_to_key=lambda x : x, descending=False):
    """ sort
      Sorts the list in-place using <TODO> algorithm.
      Default is to sort in ascending order.

      map_to_key: an optional mapping function from the stored
        object type to the key to sort by with.

      descending: an optional boolean to declare if the sort
      should be descending rather than ascending.
    """
    # check if list is length 1 or 0
    if self._length <= 1:
      return
    
        # Iterate through each element in the list
    for i in range(self._length):
        current = self.head
        # Iterate trhough the unsorted part of the list
        for j in range(0, self._length - i - 1):
            # Create key for the current element in the unsorted part
            key1 = map_to_key(self.get(j))
            # Create key for next element in the unsorted part
            key2 = map_to_key(self.get(j+1))
            # Swap if the keys are not in order
            # Compare keys based on the specified order (ascending or descending).
            if ((key1 > key2) if not descending else (key1 < key2)):
                # Swap the elements
                temp = current.data
                current.data = current.next.data
                current.next.data = temp
            current = current.next



# Test Examples
# a typical case - tuples (to test maps)
# typical2_tuple = LinkedList()
# typical2_tuple.append( ('Latte', 5.49) )
# typical2_tuple.append( ('Drip Coffee', 2.19) )
# typical2_tuple.append( ('Caramel Frappuccino', 6.79) )
# map_to_second_key = lambda x : x[1]
# print(typical2_tuple.contains(6.79, map_to_key=map_to_second_key))

# typical1_int = LinkedList()
# typical1_int.append(5)
# typical1_int.append(9)
# typical1_int.append(0)
# typical1_int.append(4)
# typical1_int.append(5)
# typical1_int.append(-2)
# # typical1_int.sort(map_to_key=lambda x : x, descending=False)
# print(typical1_int.get(0))
# print(typical1_int.get(5))
# typical1_int.sort( map_to_key=lambda x : x, descending=False)
# print(typical1_int.get(1))
# print(typical1_int.get(5))
