import java.util.ArrayList;

public class Node {
	public ArrayList<Node> children;
	public String name;
	public int level;
	public Node(String name, int level) {
		children = new ArrayList<Node>();
		this.name = name;
		this.level = level;
	}

	public String toString() {
		if(children.size() == 0) {
			return "{" + name + ", " + level + "}";
		}
		else {
			return "{" + this.name + ", " + level + ": " + children + "}";
		}
	}
}