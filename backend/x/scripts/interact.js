// interact.js

const API_KEY = process.env.API_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;


const contract = require("../artifacts/contracts/bank.sol/Bank.json");

console.log(JSON.stringify(contract.abi));
    

// Provider
const alchemyProvider = new ethers.providers.AlchemyProvider(network="goerli", API_KEY);

// Signer
const signer = new ethers.Wallet(PRIVATE_KEY, alchemyProvider);

// Contract
const bankContract = new ethers.Contract(CONTRACT_ADDRESS, contract.abi, signer);

// ...

async function main() {
  const message = await bank.message();
  console.log("The message is: " + message);
}
main();