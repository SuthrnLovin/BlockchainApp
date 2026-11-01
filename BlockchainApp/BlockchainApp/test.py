from django.test import SimpleTestCase
from .blockchain import Blockchain


class BlockchainTests(SimpleTestCase):
    #This all works
    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block_created(self):
        self.assertEqual(len(self.blockchain.chain), 1)

        genesis = self.blockchain.chain[0]

        self.assertEqual(genesis["index"], 1)
        self.assertEqual(genesis["previous_hash"], "1")
        self.assertEqual(genesis["proof"], 100)

    def test_valid_chain(self):
        previous_block = self.blockchain.last_block()

        self.blockchain.new_block(
            proof=200,
            previous_hash=self.blockchain.hash(previous_block),
        )

        self.assertTrue(self.blockchain.is_chain_valid())

    def test_empty_chain_is_invalid(self):
        self.blockchain.chain = []

        self.assertFalse(self.blockchain.is_chain_valid())

    def test_invalid_genesis_index(self):
        self.blockchain.chain[0]["index"] = 99

        self.assertFalse(self.blockchain.is_chain_valid())

    def test_invalid_genesis_previous_hash(self):
        self.blockchain.chain[0]["previous_hash"] = "invalid"

        self.assertFalse(self.blockchain.is_chain_valid())

    def test_invalid_previous_hash(self):
        previous_block = self.blockchain.last_block()

        self.blockchain.new_block(
            proof=200,
            previous_hash=self.blockchain.hash(previous_block),
        )

        self.blockchain.chain[1]["previous_hash"] = "invalid"

        self.assertFalse(self.blockchain.is_chain_valid())

    def test_non_sequential_index(self):
        previous_block = self.blockchain.last_block()

        self.blockchain.new_block(
            proof=200,
            previous_hash=self.blockchain.hash(previous_block),
        )

        self.blockchain.chain[1]["index"] = 5

        self.assertFalse(self.blockchain.is_chain_valid())

    def test_modifying_previous_block_invalidates_link(self):
        previous_block = self.blockchain.last_block()

        self.blockchain.new_block(
            proof=200,
            previous_hash=self.blockchain.hash(previous_block),
        )

        self.blockchain.chain[0]["proof"] = 999

        self.assertFalse(self.blockchain.is_chain_valid())

        #This does not work, need better validator
    def test_tampered_last_block_is_invalid(self):
        previous_block = self.blockchain.last_block()

        self.blockchain.new_block(
            proof=200,
            previous_hash=self.blockchain.hash(previous_block),
        )

        # Tamper with the last block
        self.blockchain.chain[-1]["proof"] = 999

        self.assertFalse(self.blockchain.is_chain_valid())