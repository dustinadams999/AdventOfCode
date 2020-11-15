import java.util.Scanner;
import java.io.File;
import java.util.Arrays;
import java.util.Stack;
import java.util.HashMap;
import java.util.ArrayList;

public class Orbit{
    public static HashMap<String,Node> nodes;
    public static HashMap<String,Node> library;
    public static ArrayList<String> path1;
    public static ArrayList<String> path2;
    public static void main(String[] args){
        path1 = new ArrayList<String>();
        path2 = new ArrayList<String>();
        library = new HashMap<String,Node>();
        nodes = new HashMap<String,Node>();
        Scanner file = new Scanner(System.in);
        try{
            file = new Scanner(new File("input"));
        }
        catch(Exception e){
            e.printStackTrace();
        }
        Node head = new Node("none", 0);
        while(file.hasNext()){
            String dep = file.next();
            String[] deps = dep.split("\\)");
            String parent = deps[0];
            String child = deps[1];
            Node parentNode = null;
            Node childNode = null;
            if(!library.containsKey(parent)) {
                parentNode = new Node(parent, -1);
                library.put(parent, parentNode);
            }
            else {
                parentNode = library.get(parent);
            }
            if(!library.containsKey(child)) {
                childNode = new Node(child, -1);
                library.put(child, childNode);
            }
            else {
                childNode = library.get(child);
            }
            parentNode.children.add(childNode);

            if(parent.equals("COM")) {
                head = parentNode;
            }
        }

        // Now assign level values to every Node
        fill(head, 0);

        int total = findTotal(head);
        System.out.println("Total is: " + total);

        System.out.println("===COMMON ANCESTOR===");
        System.out.println(findLCA(head, "YOU", "SAN"));

        System.out.println("Path1: " + path1);
        System.out.println("Path2: " + path2);

        int min_index = Math.min(path1.size(), path2.size());
        int i;
        for(i = 0; i < min_index; i++) {
            if(!path1.get(i).equals(path2.get(i))) {
                break;
            }
        }
        int dist = (path1.size() - i) + (path2.size() - i) - 2;
        System.out.println("i: " + i + ", shortest dist: " + dist);
    }

    public static void fill(Node n, int level) {
        n.level = level;
        if(n.children.size() != 0) {
            for(Node c : n.children) {
                fill(c, level+1);
            }
        }
    }

    public static String findLCA(Node head, String first, String second) {
        path1.clear();
        path2.clear();
        return findLCAInternal(head, first, second);
    }

    public static String findLCAInternal(Node head, String first, String second) {
        if (!findPath(head, first, path1) || !findPath(head, second, path2)) {
            System.out.println((path1.size() > 0) ? "first is present" : "first is missing");
            System.out.println((path2.size() > 0) ? "second is present" : "second is missing");
            return "";
        }

        int i;
        for (i = 0; i < path1.size() && i < path2.size(); i++) {     
            if (!path1.get(i).equals(path2.get(i))) {
                break;
            }
        }
 
        return path1.get(i-1);
    }

    public static boolean findPath(Node head, String n, ArrayList<String> path)
    {
        // base case
        if (head == null) {
            return false;
        }
         
        // Store this node . The node will be removed if
        // not in path from root to n.
        path.add(head.name);
 
        if (head.name.equals(n)) {
            return true;
        }
 

        for (Node c : head.children) {
            if (c != null && findPath(c, n, path)) {
                return true;
            }
        }
 
        // If not present in subtree rooted with root, remove root from
        // path[] and return false
        path.remove(path.size()-1);
 
        return false;
    }

    public static int findTotal(Node curr) {
        Stack<Node> stack = new Stack<Node>();
        int total = 0;
        stack.push(curr);
        while(!stack.empty()) {
            Node tmp = stack.pop();
            total += tmp.level;
            for(Node c : tmp.children) {
                stack.push(c);
            }
        }
        
        return total;
    }
}
