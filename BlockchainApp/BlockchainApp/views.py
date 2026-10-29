from django.http import JsonResponse
from .blockchain import Blockchain
from time import time
import json
import hashlib
blockchain = Blockchain()

#blockchain.pending_transactions.append({
    #"sender": "Alice",
    #"recipient": "Bob",
    #"amount": 10
#})

# Create the second block
#blockchain.new_block(proof=200)

# Print the entire blockchain
#print(json.dumps(blockchain.chain, indent=4))

# Print the latest block
#print(blockchain.last_block())

# Print the hash of the latest block
#print(blockchain.hash(blockchain.last_block()))



def full_chain(request):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return JsonResponse(response)
