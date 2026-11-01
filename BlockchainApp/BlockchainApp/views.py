from django.http import JsonResponse
import random
from django.shortcuts import render
from .blockchain import Blockchain
from time import time
import json
import hashlib
blockchain = Blockchain()

def dashboard(request):
    return render(request, dashboard.html)

# blockchain.pending_transactions.append({
#     "sender": "Alice",
#     "recipient": "Bob",
#     "amount": 10
# })

# # Create the second block
# blockchain.new_block(proof=200)

# # Print the entire blockchain
# print(json.dumps(blockchain.chain, indent=4))

# # Print the latest block
# print(blockchain.last_block())

# # Print the hash of the latest block
# #rint(blockchain.hash(blockchain.last_block()))


price = 100.00
cash = 1000.00
shares = 0

def dashboard(request):
    return render(request, "dashboard.html")

def stock_price(request):
    global price

    price += random.uniform(-2, 2)
    price = max(price, 1)

    return JsonResponse({
        "price": round(price, 2),
        "cash": round(cash, 2),
        "shares": shares,
        "value": round(cash + shares * price, 2)
    })


def buy(request):
    global cash, shares

    amount = int(request.GET.get("amount", 0))
    cost = amount * price

    if amount > 0 and cost <= cash:
        cash -= cost
        shares += amount

    return JsonResponse({
        "cash": round(cash, 2),
        "shares": shares
    })


def sell(request):
    global cash, shares

    amount = int(request.GET.get("amount", 0))

    if amount > 0 and amount <= shares:
        cash += amount * price
        shares -= amount

    return JsonResponse({
        "cash": round(cash, 2),
        "shares": shares
    })

def full_chain(request):
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return JsonResponse(response)
