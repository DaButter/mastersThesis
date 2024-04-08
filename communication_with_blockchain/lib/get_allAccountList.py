from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:8888"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Get the list of account addresses
accounts = web3.eth.accounts

# Print the list of account addresses
print("List of account addresses:")
for account in accounts:
    print(account)
