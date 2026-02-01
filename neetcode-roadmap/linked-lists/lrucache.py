# Definition for a Node.
class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None    
    
class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.head, self.tail = Node(-1,-1), Node(-1,-1)
    self.head.next = self.tail
    self.tail.prev = self.head

  def remove(self, node):
    prev = node.prev 
    nxt = node.next
    prev.next = nxt
    nxt.prev = prev

  def insert(self, node):
    prev = self.tail.prev
    nxt = self.tail
    prev.next = node
    node.prev = prev
    nxt.prev = node
    node.next = nxt

  def get(self, key: int) -> int:
    if key not in self.cache: return -1
    node = self.cache[key]
    #remove from the current pos
    self.remove(node)
    #insert at the tail
    self.insert(node)
    return node.val

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      node = self.cache[key]
      self.remove(node)

    new_node = Node(key, value)
    self.cache[key] = new_node
    self.insert(new_node)

    if len(self.cache) > self.capacity:
      lru = self.head.next
      self.remove(lru)
      del self.cache[lru.key]


if __name__ == "__main__":
  # lRUCache = LRUCache(2)
  # lRUCache.put(1, 10)  
  # print(lRUCache.get(1))
  # lRUCache.put(2, 20)
  # lRUCache.put(3, 30)
  # print(lRUCache.get(2))
  # print(lRUCache.get(1))

  lRUCache = LRUCache(2)
  lRUCache.put(1, 1) # -1,1,-1
  lRUCache.put(2, 2) # -1,1,2,#-1
  print(lRUCache.get(1))#-1,2,1,#-1
  lRUCache.put(3, 3) #-1,2,3#-1
  print(lRUCache.get(2))#-1,3,2,#-1
  lRUCache.put(4, 4) 
  print(lRUCache.get(1))
  print(lRUCache.get(3))
  print(lRUCache.get(4))


  ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]