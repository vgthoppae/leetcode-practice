# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:   
  def check_match(self, root1, root2):
    if not root1 and not root2:
      return True
    if root1 and not root2:
      return False
    if not root1 and root2:
      return False

    if root1.val != root2.val:
      return False

    left_ret = self.check_match(root1.left, root2.left)
    if not left_ret: return False
    right_ret = self.check_match(root1.right, root2.right)
    if not right_ret: return False
    return True

  def find_sub_root_match(self, root, sub_root):
    if not root:
      return

    if root.val == sub_root.val:
      if self.check_match(root, sub_root): 
        return True

    left_ret = self.find_sub_root_match(root.left, sub_root)
    if left_ret: return True
    right_ret = self.find_sub_root_match(root.right, sub_root)
    if right_ret: return True
    return False
      
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    return self.find_sub_root_match(root, subRoot)

def build_tree(nodes, f):
  val = next(nodes)
  if val == "x":
      return None
  left = build_tree(nodes, f)
  right = build_tree(nodes, f)
  return TreeNode(f(val), left, right)

if __name__ == "__main__":
  root = build_tree(iter(input().split()), int)
  sub_root = build_tree(iter(input().split()), int)
  s = Solution()
  print(s.isSubtree(root, sub_root)) #1 2 4 x x 5 x x 3 x x, 2 4 x x 5 x x
        