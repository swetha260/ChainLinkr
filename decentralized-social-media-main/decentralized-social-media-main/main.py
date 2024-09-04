from transaction import transaction
from wallet import wallet
from transaction_pool import transaction_pool
from block import block
import pprint
from blockchain import blockchain
from blockchain_utils import blockchain_utils
from account_model import account_model
from node import node
import sys


#from waitress import serve              
#from node_api import node_api           
#app = node_api().app                

if __name__ == "__main__":
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    api_port = int(sys.argv[3])
    
    Node = node(ip, port)
    Node.start_p2p()
    Node.start_api(api_port)         
    
    
    
    #serve(app, host="localhost" , port=5001)         
  