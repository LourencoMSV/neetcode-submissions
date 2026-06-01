/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null){
            return null;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while(!q.isEmpty()){
            TreeNode actual = q.poll();
            TreeNode tmp = actual.left;
            actual.left = actual.right;
            actual.right = tmp;
            if (actual.left != null){
                q.offer(actual.left);
            }
            if(actual.right != null){
                q.offer(actual.right);
            }
        }
        return root;
    }
}
