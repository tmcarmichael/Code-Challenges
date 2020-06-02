/*
226. Invert Binary Tree

Q: https://leetcode.com/problems/invert-binary-tree/
A: https://leetcode.com/problems/invert-binary-tree/discuss/665457/recursive-python3-and-js-solutions
*/

function invertTree(root) {
  if (!root) return root;
  [root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
  return root;
}
