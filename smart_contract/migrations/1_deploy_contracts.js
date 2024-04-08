const MultiSigWallet = artifacts.require("MultiSigWallet");

module.exports = function(deployer) {
  // Manually define owner accounts
  const owners = [
    "0xE56C681b4b7F83ac2A21BAeed4F8D7caf51225bB",
  ];

  const receiver = "0xD8DAd2C29c89a160F2345f32a12d96E44B0054d9";
  const singatureCount = owners.length;
  // const singatureCount = 1

  console.log("[DEBUG] Owner accounts:", owners);
  console.log("[DEBUG] Required signature count for a transaction: ", singatureCount);
  console.log("[DEBUG] Fund receiver account:", receiver);

  // Deploy MultiSigWallet contract with constructor arguments
  deployer.deploy(MultiSigWallet, owners, singatureCount, receiver);
};