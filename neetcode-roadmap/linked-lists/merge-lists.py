# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = node = ListNode()

    while list1 and list2:
      if list1.val<list2.val:
        node.next = list1.val
        list1 = list1.next
      else:
        node.next = list2.val
        list2 = list2.next
      node = node.next
    
    return nummmy.next

if __name__ == '__main__':
  s = Solution()
  target = 12
  position = [10,8,0,5,3]
  speed = [2,4,1,1,3]
  print(s.mergeTwoLists(target, position, speed))      

        