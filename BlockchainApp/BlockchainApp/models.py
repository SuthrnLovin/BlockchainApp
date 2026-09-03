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

