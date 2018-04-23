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



class Node(object):
  def __init__(self, blockchain, node_number):
    self.blockchain = blockchain
    self.nodes = set()
    self.node_number = node_number


  def proof_of_work(self, last_nonce):
    if self.node_number ==1:
      nonce = 0
      while self.blockchain.valid_nonce(last_nonce, nonce) is False:
        nonce += 1
    elif self.node_number ==2:
      nonce = 10000
      while self.blockchain.valid_nonce(last_nonce, nonce) is False:
        nonce -= 1
    return nonce

  def resolve_conflicts(self):
    length = len(self.blockchain.chain)
    
    for blockchain in blockchains:
      chain = blockchain.chain
      if blockchain.valid_chain(chain) and len(blockchain.chain) > length:
        self.blockchain.chain = blockchain.chain
        print('chain replaced!')
      else:
        print('chain not replaced!')

  def mine(self):
    last_block = self.blockchain.last_block
    last_nonce = last_block['nonce']
    nonce = self.proof_of_work(last_nonce)
    previous_hash = self.blockchain.hash(last_block)
    block = self.blockchain.new_block(nonce, previous_hash)

    response = {
      'message': "new block built",
      'index': block['index'],
      'nonce': block['nonce'],
      'previous_hash': block['previous_hash']
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














