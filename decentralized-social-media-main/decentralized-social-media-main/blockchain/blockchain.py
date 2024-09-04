from block import block
from blockchain_utils import blockchain_utils
from account_model import account_model

class blockchain():
    
    def __init__(self):
        self.blocks = [block.genesis()]
        self.account_model = account_model()
    
    def add_block(self, block):
        self.execute_transactions(block.transactions)
        self.blocks.append(block)
    
    def toJson(self):
        data = {}
        json_blocks = []
        for Block in self.blocks:
            json_blocks.append(Block.toJson())
        data["blocks"] = json_blocks
        return data
    
    def block_count_valid(self, block):
        if self.blocks[-1].block_count == block.block_count -1:
            return True
        else:
            return False
        
    def last_block_hash_valid(self, block):
        latest_blockchain_block_hash = blockchain_utils.hash(self.blocks[-1].payload()).hexdigest()
        if latest_blockchain_block_hash == block.last_hash:
            return True
        else:
            return False
        
    def get_covered_transaction_set(self, transactions):
        covered_transactions = []
        for transaction in transactions:
            if self.transaction_covered(transaction):
                covered_transactions.append(transaction)
            else:
                print("transaction is not covered by sender")
        return covered_transactions
    
    def transaction_covered(self, transaction):
        if transaction.type == "EXCHANGE" :
            return True
        sender_balance = self.account_model.get_balance(transaction.sender_public_key)
        if sender_balance >= transaction.amount:
            return True
        else:
            return False
    
    def execute_transactions(self, transactions):
        for transaction in transactions:
            self.execute_transaction(transaction)
        
    def execute_transaction(self, transaction):
        sender = transaction.sender_public_key
        receiver = transaction.receiver_public_key
        amount = transaction.amount
        self.account_model.update_balance(sender, -amount)
        self.account_model.update_balance(receiver, amount)
