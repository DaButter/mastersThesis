// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiSigWallet {
    address[] public owners;
    address public finalFundReceiver;
    mapping(address => bool) public isOwner;
    uint public requiredConfirmationCount;

    uint public depositCount;
    struct Deposit {
        address depositor;
        uint amount;
        uint confirmationCount;
    }

    Deposit[] public deposits;

    event DepositMade(address indexed depositor, uint amount, uint confirmationCount);
    event Confirmation(address indexed owner, uint indexed depositId);
    event Execution(uint totalAmount);

    modifier checkOwner() {
        require(isOwner[msg.sender], "Not an owner!");
        _;
    }

    modifier checkDeposit(uint _depositId) {
        require(_depositId < deposits.length, "Deposit ID does not exist!");
        _;
    }

    modifier notConfirmed(uint _depositId) {
        require(deposits[_depositId].confirmationCount < requiredConfirmationCount, "Deposit is already confirmed!");
        _;
    }

    constructor(address[] memory _owners, uint _requiredConfirmationCount, address _finalFundReceiver) {
        require(_owners.length > 0, "Owners required");
        require(_requiredConfirmationCount > 0 && _requiredConfirmationCount <= _owners.length, "Invalid number of confirmations");
        require(_finalFundReceiver != address(0), "Invalid destination account!");

        for (uint i = 0; i < _owners.length; i++) {
            address owner = _owners[i];
            require(owner != address(0), "Invalid owner!");
            require(!isOwner[owner], "Duplicate owner!");
            isOwner[owner] = true;
            owners.push(owner);
        }

        requiredConfirmationCount = _requiredConfirmationCount;
        finalFundReceiver = _finalFundReceiver;
    }

    receive() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0!");
        depositCount += msg.value;
        deposits.push(Deposit(msg.sender, msg.value, 0));
        emit DepositMade(msg.sender, msg.value, 0);
    }

    function confirmDeposit(uint _depositId) public checkOwner checkDeposit(_depositId) notConfirmed(_depositId) {
        deposits[_depositId].confirmationCount += 1;
        emit Confirmation(msg.sender, _depositId);
        if (isAllDepositsConfirmed()) {
            transferFunds();
        }
    }

    function isAllDepositsConfirmed() internal view returns (bool) {
        for (uint i = 0; i < deposits.length; i++) {
            if (deposits[i].confirmationCount != requiredConfirmationCount) {
                return false;
            }
        }
        return true;
    }

    function transferFunds() internal {
        require(depositCount > 0, "No deposits to execute");
        (bool success, ) = finalFundReceiver.call{value: depositCount}("");
        require(success, "Failed to transfer funds");
        emit Execution(depositCount);
        depositCount = 0;
    }

    // function getGreeting() public pure returns (string memory) {
        // return "Hello Austris :) This function is for test purposes and just a sanity check";
    // }
}
