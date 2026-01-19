from linked_lists_builder import build_list, printval

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def split_list(self, head):
    slow, fast = head, head

    while fast and fast.next:
      slow = slow.next 
      fast = fast.next.next

    first_head= head
    second_head= slow.next
    slow.next = None    
    return (first_head, second_head)

  def reverse_list(self, head):
    prev, curr = None, head

    while curr:
      tmp = curr.next 
      curr.next = prev
      prev = curr
      curr = tmp
    
    return prev

  def reorderList(self, head: Optional[ListNode]) -> None:
    if not head:
      return None

    #divide the list into half
    first_head, second_head= self.split_list(head)

    #reverse the second half: second_head
    rev_second_head = self.reverse_list(second_head)

    # printval(first_head, [])
    # printval(rev_second_head, [])
    
    #merge both
    curr = first_head
    rev = rev_second_head

    ret_node = curr

    while curr and rev:
      #save both lists next
      node1 = curr.next
      node2 = rev.next

      curr.next = rev
      rev.next = node1

      curr = node1
      rev = node2

if __name__ == '__main__':
  s = Solution()
  list = build_list([2,4,6,8,10])
  s.reorderList(list)
  printval(list, [])


        