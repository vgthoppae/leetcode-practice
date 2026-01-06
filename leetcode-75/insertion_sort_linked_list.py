class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

class Solution:
  def sortLinkedList(self, head:ListNode) -> ListNode:
    curr = head
    while curr.next:
      cnode = curr
      while cnode.next.val > cnode.val:
        temp = cnode.next.val
        cnode.next.val = cnode.val
        cnode.val = temp
    curr = head.next
    return