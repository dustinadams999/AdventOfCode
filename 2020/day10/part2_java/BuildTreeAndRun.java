import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;
import java.util.HashMap;
import java.io.File;

public class BuildTreeAndRun {
    public static void main(String[] args) {
        ArrayList<Integer> factors = new ArrayList<Integer>();
        Scanner input = new Scanner(System.in);
        HashMap<Integer, Node> dict = new HashMap<Integer, Node>();
        ArrayList<Integer> allItems = new ArrayList<Integer>();

        try {
            input = new Scanner(new File(args[0]));
            System.out.println("test 3 successful");
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        // build the tree
        while (input.hasNext()) {
            Integer num = input.nextInt();
            allItems.add(num);
        }

        System.out.println(allItems);
        Collections.sort(allItems);
        
        allItems.add(0, 0);
        allItems.add(allItems.size(), allItems.get(allItems.size()-1) + 3);
        System.out.println(allItems);
        Node head = null;
        for (int i = 0; i < allItems.size(); i++) {
            Node curr = null;
            if (!dict.containsKey(allItems.get(i))) { // create Node, add to dict
                curr = new Node(allItems.get(i));
                dict.put(allItems.get(i), curr);
                if (allItems.get(i) == 0) { // special case for first
                    head = curr;
                }
            }
            else {
                curr = dict.get(allItems.get(i));
            }
            int j = i+1;
            while (j < allItems.size() && allItems.get(j) <= allItems.get(i) + 3) {
                if (!dict.containsKey(allItems.get(j))) {
                    Node n = new Node(allItems.get(j));
                    dict.put(allItems.get(j), n);
                }
                dict.get(allItems.get(i)).children.add(dict.get(allItems.get(j)));
                j++;
            }
        }

        Node currStart = head;
        for (int i = 0; i < allItems.size()-1; i++) {
            if ((allItems.get(i+1) - allItems.get(i)) == 3) {
                factors.add(countTree(currStart, allItems.get(i)));
                currStart = dict.get(allItems.get(i));
            }
        }

        System.out.println(factors);

        int product = 1;
        for (Integer i : factors) {
            product *= i;
        }
        System.out.println(product);

        
    }

    public static int countTree (Node curr, int end) {
        if (curr.name == end || curr.children.size() == 0) {
            return 1;
        }
        else {
            int total = 0;
            for (Node c : curr.children) {
                total += countTree(c, end);
            }
            return total;
        }
    }

    public static void processTree (Node curr) {
        if (curr != null) {
            System.out.println(curr.name);
            for (Node c : curr.children) {
                processTree(c);
            }
        }
    }
}









