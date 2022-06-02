package dataStuctureJava;


public class Stack<T> {
    /**A stack of data, using LIFO (last-in first-out) ordering.

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
    */

    private int len;
    private Node<T> top;

    private static class Node<U> {
        private U data;
        private Node<U> prev;

        public Node(U d) {
            data = d;
            prev = null;
        }
    }
    
    public Stack() {
        /**Create an empty stack.*/
        len = 0;
        top = null;
    }
    
    public int length() {
        return len;
    }
    
    public boolean isempty() {
        /**Return True if and only if the stack is empty.*/
        return len == 0;
    }

    public void peek() {
        /**Remove the top of the stack.*/
        if (isempty())
            throw new IllegalStateException("The stack is empty");
        if (len == 1)
            top = null;
        else
            top = top.prev;
        len -= 1;
    }

    public T pop() {
        /**Return the top of the stack.*/
        if (isempty())
            throw new IllegalStateException("The stack is empty");
        return top.data;
    }
    
    public void push(T d) {
        /**Add an item at the top of the stack.*/
        Node<T> new_node = new Node<T>(d);
        new_node.prev = top;   //works with empty stacks too
        top = new_node;
        len += 1;
    }
}
