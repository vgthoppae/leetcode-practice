# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def dfs(self, p_root, q_root):
    if not p_root and not q_root:
      return True
    if p_root and not q_root:
      return False
    if not p_root and q_root:
      return False

    if p_root.val != q_root.val:
      return False

    left_ret = self.dfs(p_root.left, q_root.left)
    if not left_ret: return False
    right_ret = self.dfs(p_root.right, q_root.right)
    if not right_ret: return False
    return True


  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    return self.dfs(p, q)

def build_tree(nodes, f):
  val = next(nodes)
  if val == "x":
      return None
  left = build_tree(nodes, f)
  right = build_tree(nodes, f)
  return TreeNode(f(val), left, right)

if __name__ == "__main__":
  tree1 = build_tree(iter(input().split()), int)
  tree2 = build_tree(iter(input().split()), int)
  s = Solution()
  print(s.isSameTree(tree1, tree2)) #1 2 x x 3 x x, 4 7 x x x, 4 x 7 x x
      