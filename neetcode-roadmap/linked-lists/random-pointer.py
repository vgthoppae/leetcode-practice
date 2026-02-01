from linked_lists_builder import build_list, printval

# Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random

class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    old_to_copy = {None: None}
    curr = head

    while curr:
      node = Node(curr.val)
      old_to_copy[curr] = node
      curr = curr.next

    curr = head
    while curr:
      node = old_to_copy[curr]
      node.next = old_to_copy[curr.next]
      node.random = old_to_copy[curr.random]
      curr = curr.next

    return old_to_copy[head]
      
if __name__ == '__main__':
  s = Solution()
  n3,n7,n4,n5 = Node(3),Node(7),Node(4),Node(5)
  n3.next=n7
  n7.next=n4
  n4.next=n5
  n5.next=None
  
  n3.random=None
  n7.random=n5
  n4.random=n3
  n5.random=n7
  
  new_head = s.copyRandomList(n3)
  print('done')
        