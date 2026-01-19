from linked_lists_builder import build_list, printval
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
      tmp = curr.next
      curr.next = prev
      prev = curr
      curr = tmp

    return prev

if __name__ == "__main__":
  head = build_list([1,2,3])
  printval(head, [])
  s = Solution()
  new_head = s.reverseList(head)
  printval(new_head, [])
        

#1,2,3
#2,1 
#         