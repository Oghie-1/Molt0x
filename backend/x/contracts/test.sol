const { deployments, ethers } = require("hardhat");
const { expect } = require("chai");
const { solidity } = require("ethereum-waffle");

const Bank = require("../build/Bank");

describe("Bank", () => {
  let bank;
  let userAccount;

  beforeEach(async () => {
    // Deploy the Bank contract
    bank = await deployments.deploy(Bank);

    // Create a user account
    userAccount = (await ethers.getSigners())[0];
    await bank.createAcc({ value: ethers.utils.parseEther("1.0") });
  });

  it("should create an account", async () => {
    expect(await bank.accountExist()).to.be.true;
  });

  it("should deposit funds", async () => {
    const initialBalance = await bank.userAccountBalance();

    await bank.deposit({ value: ethers.utils.parseEther("1.0") });

    expect(await bank.userAccountBalance()).to.equal(initialBalance.add(ethers.utils.parseEther("1.0")));
  });

  it("should withdraw funds", async () => {
    const initialBalance = await bank.userAccountBalance();

    await bank.withdraw(ethers.utils.parseEther("1.0"));

    expect(await bank.userAccountBalance()).to.equal(initialBalance.sub(ethers.utils.parseEther("1.0")));
  });

  it("should transfer funds", async () => {
    const initialSenderBalance = await bank.userAccountBalance();
    const recipient = (await ether)
