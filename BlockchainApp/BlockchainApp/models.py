from django.db import models
import hashlib
import json
from time import time


class Block(models.Model):
    index = models.IntegerField()
    timestamp = models.FloatField()
    transactions = models.TextField()
    proof = models.IntegerField()
    previous_hash = models.CharField(max_length=64)
    
    @property
    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class customer(models.Model):
    name = models.CharField(max_legnth=50)
    balance = models.DecimalFeild(max_digits=5, decimal_places=2)
    created = models.DateTimeFied(auto_now_add=True)
    updated = models.DateTmeField(auto_now=True)

    def __str__(self):
        return self.name