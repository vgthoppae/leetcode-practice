from collections import  deque
class RecentCounter:
  def __init__(self):
    self.req_queue = deque()

  def ping(self, t:int)->int:
    self.req_queue.append(t)
    while self.req_queue[0] < t-3000:
      self.req_queue.popleft();

    return len(self.req_queue)


if __name__ == "__main__":
  rc = RecentCounter()
  print(rc.ping(1))#-2999,
  print(rc.ping(100))#-2900, 100
  print(rc.ping(3001))#1, 3001
  print(rc.ping(3002))#2, 3002
  print(rc.ping(4000))#1000, 4000
  # print(rc.ping(5000))  # 2000, 5000
  # print(rc.ping(6000))  # 3000, 6000
  print(rc.ping(7000))  # 4000, 7000