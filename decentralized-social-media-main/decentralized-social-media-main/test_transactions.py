from Crypto.PublicKey import RSA
from wallet import wallet
from blockchain_utils import blockchain_utils
import requests

if __name__ == "__main__":
    bob = wallet()
    alice = wallet()
    exchange = wallet()
    
    transaction = exchange.create_transaction(alice.public_key_string(), 10, "EXCHANGE")
    
    url = "http://localhost:5000/add_transaction"
  
    package = {
        "sender": transaction.sender_public_key,  # Use sender_public_key attribute
        "receiver": transaction.receiver_public_key,  # Use receiver_public_key attribute
        "amount": transaction.amount
    }
    
    
    request = requests.post(url, json=package)
    print(request.text)
    
