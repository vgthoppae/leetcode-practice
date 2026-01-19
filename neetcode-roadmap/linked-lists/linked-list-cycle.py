from linked_lists_builder import build_list, printval

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next or not head.next.next:
      return False

    slow = head
    fast = head.next.next
    
    while fast:
      slow = slow.next
      if not fast.next or not fast.next.next: return False
      fast = fast.next.next
      if slow == fast:
        return True

    return False

if __name__ == '__main__':
  s = Solution()
  node1 = ListNode(1)
  node2 = ListNode(2)
  node3 = ListNode(3)
  
  node1.next = node2
  node2.next = node3
  # node3.next = node1

  head = s.hasCycle(node1)
  print(head)


        