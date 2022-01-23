from collections import OrderedDict

# import binascii

# import Crypto
# import Crypto.Random
# from Crypto.Hash import SHA
# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5

import hashlib
import json
from time import time
# from urllib.parse import urlparse
# from uuid import uuid4

# import requests
# from flask import Flask, jsonify, request, render_template
# from flask_cors import CORS

MINING_SENDER = "THE BLOCKCHAIN"
MINING_REWARD = 1
MINING_DIFFICULTY = 2


# class Blockchain:

#     def __init__(self):
        
#         self.transactions = []
#         self.chain = []
#         self.nodes = set()
#         #Generate random number to be used as node_id
#         self.node_id = str(uuid4()).replace('-', '')
#         #Create genesis block
#         self.create_block(0, '00')


# def hash(self, block):
#     """
#     Create a SHA-256 hash of a block
#     """
#     # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
#     block_string = json.dumps(block, sort_keys=True).encode()
#         return hashlib.sha256(block_string).hexdigest()



def create_block(seq, nonce, previous_hash):
    """
    Add a block of transactions to the blockchain
    """
    block = {'timestamp': time(),
            'seq':seq,
            # 'transactions': self.transactions,
            'nonce': nonce,
            'previous_hash': previous_hash}

    # # Reset the current list of transactions
    # self.transactions = []

    # self.chain.append(block)
    return block


myblock = {"seq":"ACGATAGATATGAGCCCCAGT", "nonce":10}
myblock2 = create_block("ACGATAGATATGAGCCCCAGT", 10, "")
def hash(block):
    """
    Create a SHA-256 hash of a block
    """
    # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()


print('printing block1')
print(json.dumps(myblock, sort_keys=True).encode())
print(hash(myblock))
print('\nprinting block2')
print(json.dumps(myblock2, sort_keys=True).encode())
print(hash(myblock2))

