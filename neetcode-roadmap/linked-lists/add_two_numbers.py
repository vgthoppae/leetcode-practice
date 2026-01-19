from linked_lists_builder import build_list, printval

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def form_digit(self, head):
    stack = []
    while head:
      stack.append(str(head.val))
      head = head.next

    stack.reverse()
    str_digit = "".join(stack)    
    return int(str_digit)

  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    digit1 = self.form_digit(l1)
    digit2 = self.form_digit(l2)
    val = str(digit1 + digit2)

    next = None
    for c in range(len(val)):
      node = ListNode(int(val[c]))
      node.next = next
      next = node

    return node

if __name__ == '__main__':
  s = Solution()
  l1 = build_list([9])
  l2 = build_list([9])
  list = s.addTwoNumbers(l1, l2)
  printval(list, [])
  
        