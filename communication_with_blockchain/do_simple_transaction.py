from web3 import Web3

# Ganache RPC server endpoint
ganache_url = "http://127.0.0.1:8888"

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Sender and receiver account addresses
sender_address = "0x77ed873989C5452154D11e1e2C9F58fEA30A21Ef"
receiver_address = "0x95477df6DA92E8e27d5b40679B751c44c2Bd507E"

# Get the nonce
nonce = web3.eth.get_transaction_count(sender_address)

# Build the transaction
transaction = {
    'from': sender_address,
    'to': receiver_address,
    'value': web3.to_wei(10, 'ether'),       # ETH amount to be sent
    'gas': 2000000,                         # Gas limit
    'gasPrice': web3.to_wei('50', 'gwei'),  # Gas price in Gwei
    'nonce': nonce,                         # Nonce value
}

# Sender's account private key:
private_key = "0x22713404266b3c8105600d2676d071e16b5010b702c49be3d804d2dc8d80bb22"

# Sign the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Wait for the transaction to be mined
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction receipt: {tx_receipt}")
if tx_receipt.status == 1:
    print("Transaction successful!")
else:
    print(f"Transaction failed with status code: {tx_receipt.status}")
