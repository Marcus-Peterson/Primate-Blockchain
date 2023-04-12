from flask import Flask, jsonify, request
from blockchainv1 import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

# Get the full blockchain
@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain': [block.__dict__ for block in blockchain.chain],
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

# Add a new delegate
@app.route('/delegate', methods=['POST'])
def add_delegate():
    delegate_id = request.form['id']
    blockchain.add_delegate(delegate_id)
    return f"Delegate {delegate_id} added", 201

# Perform staking
@app.route('/stake', methods=['POST'])
def stake():
    delegate_id = request.form['id']
    amount = float(request.form['amount'])
    is_jernmalm = request.form['is_jernmalm'].lower() == 'true'
    delegate = next((d for d in blockchain.delegates if d.delegate_id == delegate_id), None)
    
    if delegate is None:
        return "Delegate not found", 404
    
    blockchain.stake(delegate, amount, is_jernmalm)
    return "Staking successful", 200

# Vote for a delegate
@app.route('/vote', methods=['POST'])
def vote():
    voter_id = request.form['voter_id']
    delegate_id = request.form['delegate_id']
    delegate = next((d for d in blockchain.delegates if d.delegate_id == delegate_id), None)
    
    if delegate is None:
        return "Delegate not found", 404
    
    blockchain.vote_for_delegate(voter_id, delegate)
    return "Vote successful", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
