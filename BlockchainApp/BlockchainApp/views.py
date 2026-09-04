from django.http import JsonResponse
from .blockchain import Blockchain
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Payment
from .models import customer
import decimal
from django.db import transaction



blockchain = Blockchain()




def full_chain(request):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return JsonResponse(response)
