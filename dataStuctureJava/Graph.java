package dataStuctureJava;

import java.util.ArrayList;
import java.util.HashMap;

public class Graph<T> {
    
    private Node<T>[] nodes;
    private int[][] edges;

    public static class Node<U> {
        private int id = -1;
        private U data;
        private ArrayList<Node<U>> children;

        public Node(U d) {
            data = d;
            children = new ArrayList<>();
        }
    }

    public Graph(T[] values, int[][] edges) {
        /**
         * Create a Graph with nodes with the corresponding values
         * linked according to the index pairs in edges
         */
        if (edges == null) throw new NullPointerException("Null edges.");
        this.nodes = new Node[values.length];
        this.edges = new int[edges.length][2];
        for (int i = 0; i < values.length; i++)
            this.nodes[i] = new Node<T>(values[i]);
        for (int i = 0; i < edges.length; i++) {
            int[] edge = edges[i];
            if (edge.length != 2)
                throw new IllegalStateException("Exactly 2 indexes must be provided to define an edge.");
            this.nodes[edge[0]].children.add(this.nodes[edge[1]]);
            this.edges[i] = edge;
        }
        for (Node<T> node : this.nodes)
            assert (node.id == -1);
        for (int i = 0; i < this.nodes.length; i++)
            this.nodes[i].id = i;
    }

    public Graph() {
        this.nodes = new Node[0];
        this.edges = new int[0][];
    }
    
    public HashMap<String, String[]>[] getAdjacencyList() {
        HashMap<String, String[]>[] adjacencyList = new HashMap[nodes.length];
        for (int i = 0; i < nodes.length; i++) {
            Node<T> node = nodes[i];
            String nodeRepr = "(" + i + ", " + node.data + ")";
            String[] childrenRepr = new String[node.children.size()];
            for (int j = 0; j < node.children.size(); j++) {
                Node<T> child = node.children.get(j);
                childrenRepr[j] = "(" + child.id + ", " + child.data + ")";
            }
            adjacencyList[i] = new HashMap<>(1);
            adjacencyList[i].put(nodeRepr, childrenRepr);
        }
        return adjacencyList;
    }
}
