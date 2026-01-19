class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = None
class Solution:
  def revList(self, head: ListNode) -> ListNode:
    dummy = ListNode(None)

    curr = head
    while curr:
      next = curr.next
      curr.next = dummy.next
      dummy.next = curr
      curr = next

    return dummy.next

if __name__ == "__main__":
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  ret = Solution().revList(head)
  print('done')
