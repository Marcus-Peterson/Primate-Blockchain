import hashlib
import time
import random
import math

class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.jernmalm = 0
        self.riksdaler = 0

class Delegate(Node):
    def __init__(self, identifier):
        super().__init__(identifier)
        self.total_flow_value = 0

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def compute_hash(block):
    block_data = str(block.index) + str(block.previous_hash) + str(block.timestamp) + str(block.data)
    return hashlib.sha256(block_data.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", "0")

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis_block()]
        self.pending_transactions = []
        self.delegates = []
        self.common_staking_pool = []
        self.rotation_count = 0

    def add_block(self, new_block):
        if len(self.chain) > 0:
            new_block.previous_hash = self.chain[len(self.chain)-1].hash
        else:
            new_block.previous_hash = "0"
        
        new_block.hash = compute_hash(new_block)
        self.chain.append(new_block)

    def add_delegate(self, delegate):
        if len(self.delegates) < 256:
            self.delegates.append(delegate)

    def new_transaction(self, sender, recipient, amount, is_jernmalm):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'is_jernmalm': is_jernmalm
        }
        self.pending_transactions.append(transaction)
        return self.get_last_block()['index'] + 1

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_stake(self):
        selected_delegate = random.choice(self.delegates)
        return selected_delegate

    def mine(self, node_identifier):
        last_block = self.get_last_block()
        last_proof = last_block['proof']
        delegate = self.proof_of_stake()

        if delegate == node_identifier:
            block = Block(len(self.chain), last_block.hash, time.time(), self.pending_transactions, "0")
            self.add_block(block)
            self.pending_transactions = []
            return True
        else:
            return False
    def perform_stake_rotation(self):
        if self.rotation_count >= 256:
            self.update_delegates()
            self.destroy_coins()
            
            for delegate in self.delegates:
                reward = self.calculate_individual_reward(delegate)
                delegate.jernmalm += reward * delegate.jernmalm
                delegate.riksdaler += reward * delegate.riksdaler
                
            self.rotation_count = 0

    def stake(self, node, amount, is_jernmalm):
        if node is None or amount <= 0:
            raise ValueError("Invalid node or stake amount")
        if is_jernmalm:
            node.jernmalm += amount
        else:
            node.riksdaler += amount
        self.perform_stake_rotation()

    def calculate_common_staking_pool(self):
        a = sum([node.jernmalm for node in self.delegates])
        b = sum([node.riksdaler for node in self.delegates])
        c = (a - b * math.cos(1))**2 + (0 - b * math.sin(1))**2
        return c

    def calculate_individual_reward(self, node):
        c = self.calculate_common_staking_pool()
        sN = node.total_flow_value
        s = (c - 256) * (-sN)
        profit = s / c
        return profit

    def register_swe_stock(self, organization_number, company_name, owner):
        token = f"SWE-{organization_number}-{company_name}"
        self.add_delegate(Delegate(owner))
        return token
    
    def calculate_individual_reward(self, node):
        c = self.calculate_common_staking_pool()
        sN = node.total_flow_value
        s = (c - 256) * (-sN)
        profit = s / c
        return profit

    def register_swe_stock(self, organization_number, company_name, owner):
        token = f"SWE-{organization_number}-{company_name}"
        self.add_delegate(Delegate(owner))
        return token

# Example usage of the modified Blockchain class
blockchain = Blockchain()
genesis_node = Node("genesis")
blockchain.stake(genesis_node, 256, True)
blockchain.register_swe_stock("1234567890", "TestCompany", "test_owner")


# Example usage of the modified Blockchain class
blockchain = Blockchain()
genesis_node = Node("genesis")
blockchain.stake(genesis_node, 256, True)
blockchain.register_swe_stock("1234567890", "TestCompany", "test_owner")

