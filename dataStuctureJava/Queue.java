package dataStuctureJava;

public class Queue<T> {
    /**
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
    */

    private Node<T> head;
    private Node<T> tail;
    private int len;

    private class Node<U> {
        private U data;
        private Node<U> next;

        public Node(U d) {
            data = d;
            next = null;
        }
    }
    
    public Queue() {
        /**Create an empty queue.*/
        head = null;
        tail = null;
        len = 0;
    }
    
    public int length() {
        return len;
    }
    
    public boolean isempty() {
        /**Return True if and only if the queue is empty.*/
        return len == 0;
    }
    
    public void add(T d) {
        /**Add an item to the end of the queue.*/
        Node<T> new_node = new Node<T>(d);
        if (len == 0)
            head = new_node;
        else
            tail.next = new_node;
        tail = new_node;
        len += 1;
    }

    public T peek() {
        /**Return the top of the queue.*/
        if (isempty())
            throw new IllegalStateException("The queue is empty");
        return head.data;
    }
    
    public void remove() {
        /**Remove the first item of the queue.*/
        if (isempty())
            throw new IllegalStateException("The queue is empty");
        if (len == 1)
            tail = null;
        head = head.next;   //Works with len = 1 too.
    }
}