# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def dfs(self, root, level):
      if not root:
        return level

      level += 1
      level_left = self.dfs(root.left, level)
      level_right = self.dfs(root.right, level)   
      return max(level_left, level_right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
      return self.dfs(root, 0)

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
    print(s.maxDepth(root)) #1 2 x x 3 4 x x x