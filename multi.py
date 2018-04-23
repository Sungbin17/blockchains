from multiprocessing import Process
import urllib.request


node1 = "http://localhost:5000/"

node2 = "http://localhost:5000/"

urllib.request.urlopen("http://example.com/foo/bar").read()



def node1():
  urllib.request.urlopen(node1 + 'mine_block').read()
  urllib.request.urlopen(node1 + 'replace_chain').read()


def node2():
  urllib.request.urlopen(node2 + 'mine_block').read()
  urllib.request.urlopen(node2 + 'replace_chain').read()

if __name__ == '__main__':
  p1 = Process(target=node1)
  p1.start()
  p2 = Process(target=node2)
  p2.start()
