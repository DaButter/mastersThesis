# Master Thesis: Multi Signature Wallet Smart Contract Performance Measurements

This repository contains the source code and measurement results for my master's thesis on evaluating the performance of a multi-signature wallet smart contract on the Ganache Ethereum blockchain. The focus of the study is on gas usage during various operations, such as deposit creation, signature verification, and contract deployment.

## Directory Structure

The repository is organized into the following directories:

### `communication_with_blockchain`

This directory contains Python scripts used to interact with the Ethereum blockchain via the Web3 library. These scripts are responsible for executing test scenarios, such as creating deposits, obtaining signatures, and recording gas costs for transactions. Additionally, helper scripts are included for tasks such as fetching a list of all accounts in Ganache. The main script I used for measurements is ```smart_contract_test_scenarios.py``` to whom I changed the deposit/signer count as needed for measurements. The contract address and account addresses are hardcoded, was too lazy to automate this, but that is why helper scripts exist to fetch the needed data to be pasted.

### `gas_cost_measurements`

In this directory, MATLAB scripts are provided for analyzing and visualizing gas cost measurements. The scripts generate graphs illustrating the relationship between gas costs and various factors, such as signature count, deposit count, and contract owner count. The measurements provide insights into the efficiency and scalability of the multi-signature wallet smart contract.

### `smart_contract`

The `smart_contract` directory contains the complete Truffle project for the multi-signature wallet smart contract. It includes the following files:

- `truffle-config.js`: Configuration file for Truffle project settings.
- `MultiSigWallet.sol`: Source code for the multi-signature wallet smart contract.
- `1_deploy_contracts.js`: Deployment script for deploying the smart contract to the Ethereum blockchain.
- `MultiSigWallet.json`: ABI (Application Binary Interface) JSON file containing the contract's interface definition.

## Usage

To replicate the experiments and analyze the performance of the multi-signature wallet smart contract, follow the instructions provided in each directory's respective README file.

## Contributors

- [Austris Eglitis]
