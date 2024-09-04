from transaction import transaction
from flask_classful import FlaskView, route
from flask import Flask, jsonify, request
from blockchain_utils import blockchain_utils

node = None

class node_api(FlaskView):
    
    def __init__(self):
        self.app = Flask(__name__)
        
    def start(self, api_port):
        node_api.register(self.app, route_base="/")
        self.app.run(host="localhost", port=api_port)
        
    def inject_node(self, injected_node):
        global node
        node = injected_node
        
    @route("/info", methods=["GET"])
    def info(self):
        return "This is a communication interface to a nodes blockchain", 200
    
    @route("/blockchain", methods=["GET"])
    def blockchain(self):
        return node.Blockchain.toJson(), 200
    
    @route("/transaction_pool", methods=["GET"])
    def transaction_pool(self):
        transactions = {}
        for ctr, transaction in enumerate(node.Transaction_pool.transactions):
            transactions[ctr] = transaction.toJson()
        return jsonify(transactions), 200
    
    @route("/transaction", methods=["POST"])
    def transaction(self):
        values = request.get_json()
        if not "sender" in values or not "receiver" in values or not "amount" in values:
            return "Missing transaction value", 400
        sender = values["sender"]
        receiver = values["receiver"]
        amount = values["amount"]
        Transaction = transaction(sender, receiver, amount,"Transfer")
        node.handle_transaction(Transaction)
        response = {"message": "Received transaction"}
        return jsonify(response), 201