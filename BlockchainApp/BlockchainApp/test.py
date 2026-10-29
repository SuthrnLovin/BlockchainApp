from django.test import SimpleTestCase
from .blockchain import Blockchain
from django.test import TestCase

class BlockchainValidationTests(SimpleTestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_valid_genesis_block(self):
        self.assertTrue(
            self.blockchain.is_chain_valid()
        )

    def test_invalid_genesis_index(self):
        self.blockchain.chain[0]["index"] = 99

        self.assertFalse(
            self.blockchain.is_chain_valid()
        )

    def test_invalid_genesis_previous_hash(self):
        self.blockchain.chain[0]["previous_hash"] = "invalid"

        self.assertFalse(
            self.blockchain.is_chain_valid()
        )

    def test_empty_chain_is_invalid(self):
        self.blockchain.chain = []

        self.assertFalse(
            self.blockchain.is_chain_valid()
        )