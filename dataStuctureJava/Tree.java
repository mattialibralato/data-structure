package dataStuctureJava;

import java.util.HashMap;
import java.util.Map;

public class Tree<T> {
    /**
    A Tree is a data structure made of nodes, such that
    - has a root node;
    - every node has zero or more child nodes.
    We allow the existence of and empty tree (with no nodes at all).
    */

    private Node<T> root;

    public static class Node<U> {
        private U data;
        private Node<U>[] children;
        private Node<U> parent;

        public Node(U d) {
            data = d;
            children = new Node[0];
            parent = null;
        }
    
        public Node<U> copy() {
            /**A shallow copy ot the node keeping only the data attribute.*/
            return new Node<U>(data);
        }

        public Node<U> deepCopy() {
            /**A deep copy of the node, except for the parent, aliased with the original one.*/
            Node<U> node = deepCopyNoParent();
            node.setDescendentParents(parent);
            return node;
        }
    
        private Node<U> deepCopyNoParent() {
            /** A deep copy of the node which however ignores the parent.*/
            Node<U> node = new Node<U>(data);
            Node<U>[] copy_children = new Node[children.length];
            for (int i = 0; i < children.length; i++)
                copy_children[i] = children[i].deepCopyNoParent();
            node.children = copy_children;
            return node;
        }
        
        private void setDescendentParents(Node<U> parent) {
            for (Node<U> child : children)
                child.setDescendentParents(this);
            this.parent = parent;
        }
    }

    public Tree(Map<T, Object[]> leaves_dict) {
        /**
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
            HashMap<Integer, Object[]> leaves_map = new HashMap<>(1);
                HashMap<Integer, Object[]> leaves_map1 = new HashMap<>(1);
                    HashMap<Integer, Object[]> leaves_map11 = new HashMap<>(1);
                        leaves_map11.put(2, new HashMap[0]);
                    HashMap<Integer, Object[]> leaves_map12 = new HashMap<>(1);
                        leaves_map12.put(6, new HashMap[0]);
                    leaves_map1.put(4, new HashMap[]{leaves_map11, leaves_map12});
                HashMap<Integer, Object[]> leaves_map2 = new HashMap<>(1);
                    HashMap<Integer, Object[]> leaves_map21 = new HashMap<>(1);
                        leaves_map21.put(10, new HashMap[0]);
                    HashMap<Integer, Object[]> leaves_map22 = new HashMap<>(1);
                        leaves_map22.put(14, new HashMap[0]);
                    leaves_map2.put(12, new HashMap[]{leaves_map21, leaves_map22});
                leaves_map.put(8, new HashMap[]{leaves_map1, leaves_map2});
            Tree<Integer> tree = new Tree<>(leaves_map);
        */

        if (leaves_dict.size() == 0)
            root = null;
        else
            root = populateNode(leaves_dict, null);
    }

    public Tree() {
        this(new HashMap<>(0));
    }

    private Node<T> populateNode(Map<T, Object[]> leaves_dict, Node<T> parent) {
        T d = (T) leaves_dict.keySet().toArray()[0];
        Map<T, Object[]>[] childrenList = (Map<T, Object[]>[]) leaves_dict.values().toArray()[0];
        Node<T> node = new Node<T>(d);
        node.parent = parent;
        Node<T>[] nodeChildren = new Node[childrenList.length];
        for (int i = 0; i < childrenList.length; i++)
            nodeChildren[i] = populateNode(childrenList[i], node);
        node.children = nodeChildren;
        return node;
    }

    public Tree<T> deepCopy() {
        Tree<T> tree = new Tree<T>();
        tree.root = null;
        if (root != null)
            tree.root = root.deepCopy();
        return tree;
    }

    public T getItem(int[] indexes) {
        /** Get the value of the node from the sequence of indexes.
        Iterating among them it navigates through
        the descendentes. In other words, it returns
        the value of the indexes[-1]-th child of the indexes[-2]-th child
        of the indexes[0]-th child of the root node.*/
        if (root == null)
            throw new NullPointerException("The tree is empty.");
        Node<T> node = root;
        for (int i : indexes)
            node = node.children[i];
        return node.data;
    }

    public Tree<T> getSubtree(int[] indexes) {
        /** Get the subtree whose root node is determined by the sequence of indexes.
        Iterating among them it navigates through
        the descendentes. In other words, it returns
        the tree whose root is the indexes[-1]-th child of the indexes[-2]-th child
        of the indexes[0]-th child of the root node.*/
        if (root == null)
            throw new NullPointerException("The tree is empty.");
        Node<T> node = root;
        for (int i : indexes)
            node = node.children[i];
        Tree<T> tree = new Tree<T>();
        tree.root = node.deepCopy();
        return tree;
    }
}