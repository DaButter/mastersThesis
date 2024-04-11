from web3 import Web3
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:8888"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Get transaction receipt by transaction hash
tx_hash = "0x7ec481e51b309e6c884fd52a9dcb8b881966116aeacacc89e61e31772a9807b8"
tx_receipt = web3.eth.get_transaction_receipt(tx_hash)

# Print transaction receipt
print("Receipt data: ", tx_receipt)
