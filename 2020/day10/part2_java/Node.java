import java.util.ArrayList;

public class Node {
    public Integer name;
    public ArrayList<Node> children;
    public Node(Integer name) {
        this.name = name;
        children = new ArrayList<Node>();
    }

    public String toString() {
        return "{" + name + "}";
        /*if (children.size() == 0) {
            return "{" + name + "}"; 
        }
        else {
            return "{" + name + ": " +children+ "}";
        }*/
    }
}