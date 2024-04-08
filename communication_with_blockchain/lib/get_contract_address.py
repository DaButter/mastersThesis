from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:8888"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Get the latest block number
latest_block = web3.eth.block_number

# List to store contract addresses
contract_addresses = []

# Iterate through blocks to get contract addresses
for block_number in range(1, latest_block + 1):
    block = web3.eth.get_block(block_number)
    transactions = block['transactions']
    for tx_hash in transactions:
        tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
        if tx_receipt.contractAddress:
            contract_addresses.append(tx_receipt.contractAddress)

# Print the list of contract addresses
print("Contract Addresses:")
for address in contract_addresses:
    print(address)
