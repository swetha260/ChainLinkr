from Crypto.Hash import SHA256
import json

class blockchain_utils():
    
    @staticmethod
    def hash(data):
        data_string = json.dumps(data,sort_keys=True)
        data_bytes = data_string.encode("utf-8")
        data_hash = SHA256.new(data_bytes)
        return data_hash
