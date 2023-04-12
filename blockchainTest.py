from blockchain import *
def test_blockchain():
    # Create a new blockchain instance
    blockchain = Blockchain()

    # Test genesis block creation
    assert len(blockchain.chain) == 1, "Genesis block not created"

    # Test adding delegates
    blockchain.add_delegate("Delegate 1")
    blockchain.add_delegate("Delegate 2")
    assert len(blockchain.delegates) == 2, "Delegates not added correctly"

    # Test stake functionality
    blockchain.stake(blockchain.delegates[0], 100, True)
    assert blockchain.delegates[0].jernmalm == 356, "Staking Jernmalm failed"
    blockchain.stake(blockchain.delegates[1], 50, False)
    assert blockchain.delegates[1].riksdaler == 50, "Staking Riksdaler failed"

    # Test rotation count and stake rotation
    for _ in range(255):
        blockchain.stake(blockchain.delegates[0], 100, True)
    assert blockchain.rotation_count == 256, "Rotation count not updated correctly"
    assert len(blockchain.common_staking_pool) == 0, "Stake rotation not performed correctly"

    # Test destroy coins functionality
    blockchain.stake(blockchain.delegates[0], 100, True)
    assert blockchain.rotation_count == 1, "Rotation count not reset after stake rotation"
    assert blockchain.delegates[0].jernmalm < 356, "Destroy coins failed"
    assert blockchain.delegates[1].riksdaler < 50, "Destroy coins failed"

    print("All tests passed!")


if __name__ == "__main__":
    test_blockchain()
