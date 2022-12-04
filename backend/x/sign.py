import json

from dotenv import load_dotenv
from web3 import Web3, Account, HTTPProvider

# web3.py instance
w3 = Web3(HTTPProvider("https://eth-goerli.alchemyapi.io/v2/IAbVvHTk8FLyqNi44LSKH69_vEJiCtLU")) #modify
print(w3.isConnected())
contract_address = Web3.toChecksumAddress("<Deployed Contract Address here>") #modify
key="<Private key with 0x prefix here>" #modify
acct = w3.eth.account.privateKeyToAccount(key)
account_address= acct.address

tx = contract_instance.functions.greet("Hello all  my goody people").buildTransaction(
    {'nonce': w3.eth.getTransactionCount(account_address)})
# Get tx receipt to get contract address
signed_tx = w3.eth.account.signTransaction(tx, key)
#tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(hash.hex())
