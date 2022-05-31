import array


class LinkedList():
    """
    A sequence of nodes one linked by the previous one.

    Computational complexity (N = length of the linked list):
    <table>
        <tr><td>Length                  </td><td>O(1)</td></tr>
        <tr><td>Get the i-th item       </td><td>O(i)</td></tr>
        <tr><td>Append = Add last       </td><td>O(1)</td></tr>
        <tr><td>Add first               </td><td>O(1)</td></tr>
        <tr><td>Get first               </td><td>O(1)</td></tr>
        <tr><td>Get last                </td><td>O(1)</td></tr>
        <tr><td>Insert at the i-th index</td><td>O(i)</td></tr>
        <tr><td>Remove the i-th item    </td><td>O(i)</td></tr>
        <tr><td>Set the i-th item       </td><td>O(i)</td></tr>
    </table>
    """

    class Node():
        def __init__(self, d):
            self.data = d
            self.next = None
    
    def __init__(self, collection: list):
        """Create a linked list from a list."""
        self._len = len(collection)
        if self._len == 0:
            self.start_node = None
            self.end_node = None
        elif self._len == 1:
            self.start_node = self.Node(collection[0])
            self.end_node = self.Node(collection[-1])
        else:
            self.start_node = self.Node(collection[0])
            self.end_node = self.Node(collection[-1])
        
            # Instantiate all the nodes
            next_node = self.end_node
            for i in reversed(range(1,self._len - 1)):
                node = self.Node(collection[i])
                node.next = next_node
                next_node = node
            self.start_node.next = next_node

    def __len__(self):
        return self._len

    def __getitem__(self, index: int):
        if index < 0 or index >= self._len:
            raise IndexError(f"Index {index} out of bound: len={self._len}")
        else:
            node = self.start_node
            for i in range(index):
                node = node.next
            return node.data
    
    def append(self, d):
        """Appends the specified element to the end of this list."""
        if self._len == 0:
            self.start_node = self.Node(d)
            self.end_node = self.Node(d)
        else:
            new_end = self.Node(d)
            self.end_node.next = new_end
            self.end_node = new_end
        self._len += 1
    
    def add_first(self, d):
        """Inserts the specified element at the beginning of this list."""
        if self._len == 0:
            self.start_node = self.Node(d)
            self.end_node = self.Node(d)
        else:
            new_start = self.Node(d)
            new_start.next = self.start_node
            self.start_node = new_start
        self._len += 1
    
    def add_last(self, d):
        """Appends the specified element to the end of this list."""
        self.append(d)
    
    def get_first(self):
        """Returns the first element in this list."""
        if self._len == 0:
            raise IndexError("Cannot get an item from an empty list.")
        return self.start_node.data
    
    def get_last(self):
        """Returns the first element in this list."""
        if self._len == 0:
            raise IndexError("Cannot get an item from an empty list.")
        return self.end_node.data

    def insert(self, index: int, d):
        """Inserts the specified element at the specified position in this list."""
        if index == 0:
            self.add_first(d)
        elif index == self._len:
            self.append(d)
        elif 0 < index < self._len:
            node = self[index-1]
            new_node = self.Node(d)
            new_node.next = node.next
            node.next = new_node
        else:
            raise IndexError(f"{index} out of bound: len={self._len}")
        self._len += 1
    
    def remove_first(self):
        """Removes and returns the first element from this list."""
        if self._len == 0:
            raise IndexError("Cannot remove an item from an empty list.")
        removed_node = self.start_node
        self.start_node = removed_node.next
        if self._len == 1:
            self.end_node = None
        removed_node.next = None
        self._len -= 1
        return removed_node
    
    def remove_last(self):
        """Removes and returns the last element from this list."""
        if self._len == 0:
            raise IndexError("Cannot get an item from an empty list.")
        elif self._len == 1:
            removed_node = self.start_node
            self.start_node = None
            self.end_node = None
        else:
            new_end_node = self[self._len-2]
            removed_node = self.end_node
            self.end_node = new_end_node
            self.end_node.next = None
        self._len -= 1
        return removed_node

    def remove(self, index: int):
        """Removes the element at the specified position in this list."""
        if index == 0:
            self.remove_first()
        elif index == self._len - 1:
            self.remove_last()
        elif 0 < index < self._len - 1:
            node = self[index-1]
            node.next = node.next.next
        else:
            raise IndexError(f"{index} out of bound: len={self._len}")
        self._len -= 1

    def set(self, index: int, d):
        """Replaces the element at the specified position in this list with the specified element."""
        if index < 0 or index >= self._len:
            raise IndexError(f"Index {index} out of bound: len={self._len}")
        else:
            node = self.start_node
            for i in range(index):
                node = node.next
            node.data = d


class Stack():
    """
    A stack of data, using LIFO (last-in first-out) ordering.

    Computational complexity (N = length of the stack):
    <table>
        <tr><td>Length                  </td><td>O(1)</td></tr>
        <tr><td>Get the i-th item       </td><td>Not available</td></tr>
        <tr><td>Push = Add on the top   </td><td>O(1)</td></tr>
        <tr><td>Add first               </td><td>Not available</td></tr>
        <tr><td>Get first               </td><td>Not available</td></tr>
        <tr><td>peek = Get last         </td><td>O(1)</td></tr>
        <tr><td>Insert at the i-th index</td><td>Not available</td></tr>
        <tr><td>pop = Remove last       </td><td>O(1)</td></tr>
        <tr><td>Remove the i-th item    </td><td>Not available</td></tr>
        <tr><td>Set the i-th item       </td><td>Not available</td></tr>
    </table>
    """

    class Node():
        def __init__(self, d):
            self.data = d
            self.prev = None
    
    def __init__(self):
        self._len = 0
        self.top = None
    
    def __len__(self):
        return self._len
    
    def isempty(self):
        """Return True if and only if the stack is empty."""
        return self._len == 0

    def peek(self):
        """Remove the top of the stack."""
        if self.isempty():
            raise ValueError("The stack is empty")
        self.top = None if self._len == 1 else self.top.prev
        self._len -= 1
    
    def pop(self):
        """Return the top of the stack."""
        if self.isempty():
            raise ValueError("The stack is empty")
        return self.top.data
    
    def push(self, d):
        """Add an item at the top of the stack."""
        new_node = self.Node(d)
        new_node.prev = self.top   # works with empty stacks too
        self.top = new_node
        self._len += 1
