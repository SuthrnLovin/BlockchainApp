from django.http import JsonResponse
from .blockchain import Blockchain
blockchain = Blockchain()




def full_chain(request):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return JsonResponse(response)
