from typing import List
from linked_lists_builder import ListNode

class LinkedList:
  def __init__(self):    
    self.head = ListNode(-1)
    self.tail = self.head
    
  def get(self, index: int) -> int:
    curr = self.head.next
    i = 0
    while curr:
      if i == index:
        return curr.val
      i += 1
      curr = curr.next
    return -1
  
  def insertHead(self, val: int) -> None:
    node = ListNode(val)
    node.next = self.head.next
    self.head.next = node
    if not node.next:
      self.tail = node
    
  def insertTail(self, val: int) -> None:
    node = ListNode(val)
    self.tail.next = node
    self.tail = node

  def remove(self, index: int) -> bool: #-1, 1, 2
    i = 0
    curr = self.head
    while i < index and curr:
      i += 1
      curr = curr.next
    
    # Remove the node ahead of curr
    if curr and curr.next:
      if curr.next == self.tail:
          self.tail = curr
      curr.next = curr.next.next
      return True
    return False

  def getValues(self) -> List[int]:
    vals = []
    curr = self.head.next
    while curr:
      vals.append(curr.val)
      curr = curr.next
    return vals
    
      
if __name__ == "__main__":
  # head = build_list([1,2,3,4,5])
  s = LinkedList()
  s.insertTail(1)
  s.insertTail(2)
  print(s.get(1))
  s.remove(1)
  s.insertTail(2)
  print(s.get(1))
  print(s.get(0))
  

#-1,1,2

  