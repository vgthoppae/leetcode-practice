# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def __init__(self):
    self.max_diameter = 0

  def dfs(self, root):
    if not root:
      return 0
    
    left = self.dfs(root.left)
    right = self.dfs(root.right)

    self.max_diameter = max(self.max_diameter, left+right)
    return 1 + max(left, right)

  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.dfs(root)
    return self.max_diameter
      
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return TreeNode(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    s = Solution()
    print(s.diameterOfBinaryTree(root)) #1 2 x x 3 x x, 1 x 2 3 5 x x x 4 x x