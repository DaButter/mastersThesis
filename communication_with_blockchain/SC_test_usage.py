from web3 import Web3
import json

def sign_transaction(tx, private_key):
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    return signed_tx.rawTransaction

def send_transaction(signed_tx):
    tx_hash = web3.eth.send_raw_transaction(signed_tx)
    return tx_hash

def deposit_funds(sender_addr, sender_priv_key, amount, contract_addr):
    nonce = web3.eth.get_transaction_count(sender_addr)
    tx = {
        'from': sender_addr,
        'to': contract_addr,
        'value': amount,                        # ETH amount to be sent
        'gas': 2000000,                         # Gas limit
        'gasPrice': web3.to_wei('50', 'gwei'),  # Gas price in Gwei
        'nonce': nonce,                         # Nonce value
    }
    signed_tx = sign_transaction(tx, sender_priv_key)
    tx_hash = send_transaction(signed_tx)
    return tx_hash

def confirm_deposit(deposit_id, depositor_address, depositor_private_key):
    nonce = web3.eth.get_transaction_count(depositor_address)
    tx = contract.functions.confirmDeposit(deposit_id).build_transaction({
        'from': depositor_address,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })
    signed_tx = sign_transaction(tx, depositor_private_key)
    tx_hash = send_transaction(signed_tx)
    return tx_hash

def get_trx_gas_usage(tx_hash):
    tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
    return tx_receipt['gasUsed']


if __name__ == "__main__":
    # Connection to blockchain
    ganache_url = "http://127.0.0.1:8888"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    # Contract data
    contract_address = "0x29aE08713eaf4dfBf4066e57abCCeFC450339c5f"
    with open('lib/MultiSigWallet.json', 'r') as file:
        abi_data = json.load(file)
    contract_abi = abi_data['abi']

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Account addresses and private keys fro Ganache
    accnt_addr = [
        "0x44d4Ccfb712777CeDE08192b794EDfb5cCf10B8D",
        "0x77ed873989C5452154D11e1e2C9F58fEA30A21Ef",
        "0x7051ee651261fc53c4d74149a07973fcbBE7Fb8F",
        "0x95477df6DA92E8e27d5b40679B751c44c2Bd507E",
        "0x16bf0981504759deac3e5bF6E54106C3B209e72c",
        "0xb89285EF7e68bfA2b3d4AF08e3E0EF7Dcd6629dF"
    ]

    accnt_priv_key = [
        "0xae5c1d56f70bb07e01feae5d8cdc0084a874732e714f79d7f6bbb69e0276dc1f",
        "0x22713404266b3c8105600d2676d071e16b5010b702c49be3d804d2dc8d80bb22",
        "0x8eb0f8370ff89ada83910eeff0078d7e775be1bd289d4f23e3868d173a609bb2",
        "0x62eac73ca37c21890d1a2f15f77354d629ca18d69e897e9414e1c4f0d1f8064f",
        "0x110738edd3c3ee09b220103d702cea79d3cd3060b4b3680d6f912123cab208bb",
        "0xcda01c2ac1d8fe9f591005e33513d571f8f06ef45ba8cd15089b8916b19a183a"
    ]

    # For other exp
    # accnt_addr = ["0x6C0CfBD369A96ecAfE9955c7c1721Ee3C6a83165"]
    # accnt_priv_key = ["0x5b5e33d6701f50997c3a95b2f19e9d6cb1d5b5f622c1371b32a10a30fb718cb5"]

    # Transfer funds to the smart contract
    deposit_count = 9
    gas_usage = []
    for i in range(deposit_count):
        amount = web3.to_wei(1, 'ether')
        tx_hash = deposit_funds(accnt_addr[0], accnt_priv_key[0], amount, contract_address)
        print(f"Funds deposited by [{accnt_addr[0]}] to smart contract, transaction hash: {tx_hash.hex()}")
        trx_gas_usage = get_trx_gas_usage(tx_hash)
        gas_usage.append(trx_gas_usage)
        print(f"Gas used for deposit transaction: {trx_gas_usage}")

    print(f"Total gas usage for all deposit transactions: {sum(gas_usage)}")

    accnt_addr = ["0xE56C681b4b7F83ac2A21BAeed4F8D7caf51225bB"]
    accnt_priv_key = ["0x11c063b2facbedeb8d1bd40f8b8bf111952a77d61e9901aa23472a7f052677e1"]

    # Confirm all deposits with the needed signature count
    signer_count = 1
    gas_usage = []
    for signer_id in range(signer_count):
        for deposit_id in range(deposit_count):
            tx_hash = confirm_deposit(deposit_id, accnt_addr[signer_id], accnt_priv_key[signer_id])
            print(f"Deposit ID [{deposit_id}] confirmed by contract owner [{accnt_addr[signer_id]}], transaction hash: {tx_hash.hex()}")
            trx_gas_usage = get_trx_gas_usage(tx_hash)
            gas_usage.append(trx_gas_usage)
            print(f"Gas used for signature transaction: {trx_gas_usage}")

    print(f"Total gas usage for all signature transactions: {sum(gas_usage)}")
