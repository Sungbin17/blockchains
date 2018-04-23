from time import time
import hashlib
import json
from urllib.parse import urlparse
from uuid import uuid4
from multiprocessing import Process
from flask import Flask, jsonify, request

class BlockChain(object):
  def __init__(self):
    self.chain = []
    self.new_block(previous_hash = 1, nonce = 100)

  def new_block(self, nonce, previous_hash=None):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'nonce': nonce,
      'previous_hash': previous_hash or self.hash(self.chain[-1])
    }

    self.chain.append(block)
    return block

  def valid_chain(self, chain):
    last_block = chain[0]
    current_index = 1

    while current_index < len(chain):
      block = chain[current_index]
      last_block = block
      current_index += 1
    return True


  @property
  def last_block(self):
    return self.chain[-1]


  @staticmethod
  def hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()



  @staticmethod
  def valid_nonce(last_nonce, nonce):
    guess = f'{last_nonce}{nonce}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:5] == "00000"

  def full_chain(self):
    response = {
      'chain': self.chain,
      'length': len(self.chain)
    }
    print(response)



#------------------------------------------------------------------------------------------------------------------

blockchain1 = BlockChain()
blockchain2 = BlockChain()

blockchains = [blockchain1, blockchain2]

node1 = Node(blockchain1,1)
node2 = Node(blockchain2,2)

def run():
    for i in range(9):
        node1.mine()
        node2.mine()
        node1.resolve_conflicts()
        node2.resolve_conflicts()
        print(blockchain2.chain)



 

if __name__=='__main__':
    p1 = Process(target = run)
    p1.start()














