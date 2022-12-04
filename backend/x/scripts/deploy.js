async function main() {
   const Bank = await ethers.getContractFactory("Bank");

   // Start deployment, returning a promise that resolves to a contract object
   const bank = await Bank.deploy();
   console.log("Contract deployed to address:", bank.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });