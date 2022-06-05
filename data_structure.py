from typing import Any, Dict, List, Optional

class LinkedList:
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

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None
    
    def __init__(self, collection: Optional[list] = []):
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


class Stack:
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

    class Node:
        def __init__(self, d):
            self.data = d
            self.prev = None
    
    def __init__(self):
        """Create an empty stack."""
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


class Queue:
    """
    A queue of data, using FIFO (first-in first-out) ordering.

    Computational complexity (N = length of the queue):
    <table>
        <tr><td>Length                  </td><td>O(1)</td></tr>
        <tr><td>Get the i-th item       </td><td>Not available</td></tr>
        <tr><td>Add first               </td><td>Not available</td></tr>
        <tr><td>Add at the end          </td><td>O(1)</td></tr>
        <tr><td>peek = Get first        </td><td>O(1)</td></tr>
        <tr><td>Get last                </td><td>Not available</td></tr>
        <tr><td>Insert at the i-th index</td><td>Not available</td></tr>
        <tr><td>Remove (first)          </td><td>O(1)</td></tr>
        <tr><td>Remove last             </td><td>Not available</td></tr>
        <tr><td>Set the i-th item       </td><td>Not available</td></tr>
    </table>
    """

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None
    
    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self._len = 0
    
    def __len__(self):
        return self._len
    
    def isempty(self):
        """Return True if and only if the queue is empty."""
        return self._len == 0
    
    def add(self, d):
        """Add an item to the end of the queue."""
        new_node = self.Node(d)
        if self._len == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self._len += 1

    def peek(self):
        """Return the top of the queue."""
        if self.isempty():
            raise ValueError("The queue is empty")
        return self.head.data
    
    def remove(self):
        """Remove the first item of the queue."""
        if self.isempty():
            raise ValueError("The queue is empty")
        if self._len == 1:
            self.tail = None
        self.head = self.head.next   # Works with len = 1 too.
    

class Tree:
    """
    A Tree is a data structure made of nodes, such that
    - has a root node;
    - every node has zero or more child nodes.
    We allow the existence of and empty tree (with no nodes at all).
    """
    class Node:
        def __init__(self, d):
            self.data = d
            self.children = []
            self.parent = None
        
        def copy(self):
            """A shallow copy ot the node keeping only the data attribute."""
            return type(self)(self.data)

        def deep_copy(self):
            """A deep copy of the node, except for the parent, aliased with the original one."""
            node = self._deep_copy_no_parent(self)
            node._set_descendent_parents(self.parent)
            return node
        
        def _deep_copy_no_parent(self):
            """A deep copy of the node which however ignores the parent."""
            Node = type(self)
            node = Node(self.data)
            node.children = [self._deep_copy_no_parent(child) for child in self.children]
            return node
        
        def _set_descendent_parents(self, parent):
            for child in self.children:
                child._set_descendent_parents(self)
            self.parent = parent
    
    def __init__(self, leaves_dict: dict = {}):
        """
        Create a Tree with the structure saved in `leaves_dict`,

        Params
        ------
        leaves_dict: A dictionary containing all nested pair
            key-value with key the value
            of a node and, as value, the list of other dicts with
            the same structure. Therefore, it should be a dictionary
            with at most an item.
        
        Example
        -------
        >>> Tree(
        ...     {8: [
        ...         {4: [
        ...             {2: []},
        ...             {6: []}
        ...         ]},
        ...         {12: [
        ...             {10: []},
        ...             {14: []}
        ...         ]}
        ...     ]}
        ... )
        """
        if len(leaves_dict) == 0:
            self.root = None
        else:
            self.root = self._populate_node(leaves_dict, None)
    
    def _populate_node(self, leaves_dict: Dict[Any, List[Any]], parent: Optional[Node]):
        [(d, children_dict)] = leaves_dict.items()
        node = self.Node(d)
        node.parent = parent
        node.children = [self._populate_node(child, node) for child in children_dict]
        return node

    def deep_copy(self):
        tree = Tree()
        tree.root = None if self.root is None else self.root.deep_copy()
        return tree

    def __getitem__(self, indexes: List[int]):
        """Get the value of the node from the sequence of indexes.
        Iterating among them it navigates through
        the descendentes. In other words, it returns
        the value of the indexes[-1]-th child of the indexes[-2]-th child
        of the indexes[0]-th child of the root node."""
        if self.root is None:
            raise ValueError("The tree is empty.")
        node = self.root
        for i in indexes:
            node = node.children[i]
        return node.data
    
    def get_subtree(self, indexes: List[int]):
        """Get the subtree whose root node is determined by the sequence of indexes.
        Iterating among them it navigates through
        the descendentes. In other words, it returns
        the tree whose root is the indexes[-1]-th child of the indexes[-2]-th child
        of the indexes[0]-th child of the root node."""
        if self.root is None:
            raise ValueError("The tree is empty.")    
        node = self.root
        for i in indexes:
            node = node.children[i]
        tree = Tree()
        tree.root = node.deep_copy()
        return tree

class Graph:
    class Node:
        def __init__(self, d):
            self._id = -1
            self.data = d
            self.children = []
    
    def __init__(self, values: List[Any], edges: List[List[int]]):
        """
        Create a Graph with nodes with the corresponding values
        linked according to the index pairs in edges.
        """
        self.nodes = [self.Node(value) for value in values]
        self.edges = [[0,0] for _ in range(len(edges))]
        for i in range(len(edges)):
            edge = edges[i]
            if len(edge) != 2:
                raise ValueError("Exactly 2 indexes must be provided to define an edge.")
            self.nodes[edge[0]].children.append(self.nodes[edge[1]])
            self.edges[i] = edge
        assert all(node._id == -1 for node in self.nodes)
        for i,node in enumerate(self.nodes):
            node._id = i
    
    def get_adjacency_list(self):
        return {
            (i, node.data): [
                (child._id, child.data)
                for child in node.children
            ]
            for i,node in enumerate(self.nodes)
        }