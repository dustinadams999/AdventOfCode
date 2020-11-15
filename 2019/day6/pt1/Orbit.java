import java.util.Scanner;
import java.io.File;
import java.util.Arrays;
import java.util.Stack;
import java.util.HashMap;

public class Orbit{
	public static HashMap<String,Node> nodes;
	public static HashMap<String,Node> library;
	public static void main(String[] args){
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

		//System.out.println("\n==========CURRENT STATE==========\n");
		//System.out.println(head);

		int total = findTotal(head);
		System.out.println("Total is: " + total);
	}

	public static void fill(Node n, int level) {
		n.level = level;
		if(n.children.size() != 0) {
			for(Node c : n.children) {
				fill(c, level+1);
			}
		}
	}

	public static int findTotal(Node curr) {
		//Node
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