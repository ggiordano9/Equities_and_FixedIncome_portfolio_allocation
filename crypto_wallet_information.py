# Will be used if the investor is recommended to invest in crypto based on their tax files
# and allows the user to have a brief summary of their crypto financial account information for easy access.

# Imports
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3 import middleware
from web3.auto.infura.kovan import w3
from web3 import Account
from bip44 import Wallet
import os
import requests
from dotenv import load_dotenv
load_dotenv()

# Wallet functionality

# Create a digital wallet and Ethereum account from a mnemonic seed phrase.
def generate_crypto_account(private):
    # Fetch mnemonic 
    if not private:
        mnemonic = os.getenv("MNEMONIC")

    # Wallet Object
        wallet = Wallet(mnemonic)

    # Obtain Ethereum Private Key
        private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)
    
    return account

# Using an Ethereum account address to access the account's balance in Ether
def get_balance(address):
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Converting Wei to ether
    ether = w3.fromWei(wei_balance, "ether")

    # Return the value in ether
    return ether
