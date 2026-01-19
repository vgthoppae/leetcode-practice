class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def build_list(vals:list, curr=None, index=0):  
  if index == len(vals):
    return

  node = ListNode(vals[index])
  node.next = build_list(vals, node, index+1)
  return node

def printval(curr, vals=[]):
  if curr:
    vals.append(str(curr.val))
    printval(curr.next, vals)
  else:
    print("->".join(vals))

if __name__ == "__main__":
  head = build_list([1,2,3,4,5])
  printval(head)


  
  
