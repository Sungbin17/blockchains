from blockchain import *


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
