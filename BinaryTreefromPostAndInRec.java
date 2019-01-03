/* -----------------------------------
 *  WARNING:
 * -----------------------------------
 *  Your code may fail to compile
 *  because it contains public class
 *  declarations.
 *  To fix this, please remove the
 *  "public" keyword from your class
 *  declarations.
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public HashMap<Integer, Integer> inKeyList;
    public int[] inorder;
    public int[] postorder;
    public boolean debug = true;
    
    public void setKeys(int[] inorder, int[] postorder) {
        inKeyList = new HashMap<Integer, Integer>();
        for (int i = 0; i < inorder.length; i++) {
            inKeyList.put(inorder[i], i);
            if (debug) {
                System.out.println("key: " + inorder[i] + " val: " + i);
            }
        }
    }
    
    public void setData(int[] inorder, int[] postorder) {
        this.inorder = inorder;
        this.postorder = postorder;
    }
    
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder.length == 0 || inorder.length != postorder.length) {
            return null;
        } 
        setData(inorder, postorder);
        setKeys(inorder, postorder);
        if (debug) {
            System.out.println("inorder length = " + inorder.length);
        }
        return build(0, inorder.length - 1, 0, postorder.length - 1);
    }

    public TreeNode build(int startIn, int endIn, int startPost, int endPost) {
        if (startIn > endIn || startPost > endPost) {
            return null;
        }
        int rootVal = postorder[endPost];
        int rootIn = inKeyList.get(rootVal);
        TreeNode root = new TreeNode(rootVal);
        if (debug) {
            System.out.println("Current root val = " + rootVal);
        }
        root.left = build(startIn, rootIn - 1, startPost, 
                          startPost + (rootIn - 1 -startIn));
        root.right = build(rootIn + 1, endIn, startPost + (rootIn -startIn), endPost - 1);
        return root;
    }
}

public class BinaryTreefromPostAndInRec {
    public static int[] stringToIntegerArray(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
          return new int[0];
        }
    
        String[] parts = input.split(",");
        int[] output = new int[parts.length];
        for(int index = 0; index < parts.length; index++) {
            String part = parts[index].trim();
            output[index] = Integer.parseInt(part);
        }
        return output;
    }
    
    public static String treeNodeToString(TreeNode root) {
        if (root == null) {
            return "[]";
        }
    
        String output = "";
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);
        while(!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();
    
            if (node == null) {
              output += "null, ";
              continue;
            }
    
            output += String.valueOf(node.val) + ", ";
            nodeQueue.add(node.left);
            nodeQueue.add(node.right);
        }
        return "[" + output.substring(0, output.length() - 2) + "]";
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int[] inorder = stringToIntegerArray(line);
            line = in.readLine();
            int[] postorder = stringToIntegerArray(line);
            
            TreeNode ret = new Solution().buildTree(inorder, postorder);
            
            String out = treeNodeToString(ret);
            
            System.out.print(out);
        }
    }
}