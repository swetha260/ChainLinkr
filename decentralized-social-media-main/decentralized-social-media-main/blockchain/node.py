
from Crypto.PublicKey import RSA
from transaction_pool import transaction_pool
from wallet import wallet
from blockchain import blockchain

class node():
    
    def __init__(self):
        self.Transaction_pool = transaction_pool()
        self.Wallet = wallet()
        self.Blockchain = blockchain()

