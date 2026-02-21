# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def dfs(self, root) -> bool:
    if not root:
      return 0

    left_edge = self.dfs(root.left)
    left_edge += 1
    right_edge = self.dfs(root.right)
    right_edge += 1

    return 0

  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    pass

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
    print(s.isBalanced(root)) #1 2 x x 3 4 x x x
        