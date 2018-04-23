from multiprocessing import Process
import urllib.request
import time

node1_mine = 'http://localhost:5000/mine_block'
node1_replace = 'http://localhost:5000/replace_chain'

node2_mine = 'http://localhost:5001/mine_block'
node2_replace = 'http://localhost:5001/replace_chain'




def node1():
  urllib.request.urlopen(node1_mine).read()
  time.sleep(2)
  urllib.request.urlopen(node1_replace).read()


def node2():
  urllib.request.urlopen(node2_mine).read()
  urllib.request.urlopen(node2_replace).read()

if __name__ == '__main__':
  p1 = Process(target=node1)
  p1.start()
  p2 = Process(target=node2)
  p2.start()
