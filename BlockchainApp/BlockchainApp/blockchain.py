import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def last_block(self):
        return self.chain[-1]


    def is_chain_valid(self):
        if not self.chain:
            return False

        # Check the genesis block
        if self.chain[0]['index'] != 1:
            return False

        if self.chain[0]['previous_hash'] != '1':
            return False

        # Check every block after the genesis block
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check that the block points to the correct previous block
            if current_block['previous_hash'] != self.hash(previous_block):
                return False

            # Check that block indexes are sequential
            if current_block['index'] != previous_block['index'] + 1:
                return False

        return True


