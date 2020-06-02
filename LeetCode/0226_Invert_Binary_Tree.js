/*
226. Invert Binary Tree

Q: https://leetcode.com/problems/invert-binary-tree/
A: 
*/

function invertTree(root) {
  if (!root) return root;
  [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
  return root;
}
