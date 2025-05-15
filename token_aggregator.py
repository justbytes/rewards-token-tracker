import solana
import asyncio
import os
from solana.rpc.api import Client
from solders.pubkey import Pubkey



def aggregate(distributing_address, token_address, wallet_address):
    # Create a connection to Solana mainnet. Uses default rpc url if none is provided
    connection = Client(os.getenv('RPC_URL', "https://api.mainnet-beta.solana.com"))

    # Convert the strings to a Pubkeys
    distributing_address = Pubkey.from_string(distributing_address)
    token_address =  Pubkey.from_string(token_address)
    target_wallet = Pubkey.from_string(wallet_address)

    print(distributing_address, token_address, target_wallet)
