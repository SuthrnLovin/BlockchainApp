import django
from .models import Unit
from django.test import TestCase


class UnitTest(TestCase):
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
