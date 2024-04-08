To create truffle project template, run ```truffle init``` in the directory where project should be located.

To deploy a smart contract:
1. Create ```.sol``` contract file in ```/contracts```.
3. Create a migrate script in ```/migrations```. If input arguments for contract ```constructor()``` are needed, then parse them in the deployment script.
4. Configure ```truffle-config.js``` with the network settings to match _Ganache_ and the correct SOLC compiler version.
5. Run ```truffle deploy```. (compiles and deploys the smart contract to network)
6. Check _Ganache_ if the smart contract is deployed.