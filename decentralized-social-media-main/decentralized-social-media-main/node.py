from transaction_pool import transaction_pool
from wallet import wallet
from blockchain import blockchain
from socket_communication import socket_communication
from node_api import node_api
from message import message
from blockchain_utils import blockchain_utils

class node():
    
    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.Transaction_pool = transaction_pool()
        self.Wallet = wallet()
        self.Blockchain = blockchain()
        
    def start_p2p(self):
        self.p2p = socket_communication(self.ip, self.port)
        self.p2p.start_socket_communication(self)
        
    def start_api(self, api_port):
        self.api = node_api()
        self.api.inject_node(self)
        self.api.start(api_port)
        
    def handle_transaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signer_public_key = transaction.sender_public_key
        signature_valid = wallet.signature_valid(data, signature, signer_public_key)
        transaction_exists = self.Transaction_pool.transaction_exists(transaction)
        if not transaction_exists and signature_valid:
            self.Transaction_pool.add_transaction(transaction)
            Message = message(self.p2p.Socket_connector, "TRANSACTION", transaction)
            encoded_message = blockchain_utils.encode(Message)
            self.p2p.broadcast(encoded_message)