from web3 import Web3, Account
import time

# Create by Espresso "https://twitter.com/zicza10"
# Path to the file containing the RPC endpoint URL
rpc_endpoint_file = './rpc_endpoint.txt'

# Path to the file containing wallet private key
private_key_file = './private_key.txt'

# Connect to Ethereum node
def connect_to_rpc_endpoint(file_path):
    try:
        with open(file_path, 'r') as file:
            rpc_endpoint = file.read().strip()
        return rpc_endpoint
    except Exception as e:
        print("Error reading RPC endpoint from file:", e)
        return None

# Wallet connection status
wallet_connected = False

def read_private_key_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            private_key = file.read().strip()
        return private_key
    except Exception as e:
        print("Error reading private key from file:", e)
        return None

def toggle_wallet_connection(private_key):
    global wallet_connected
    try:
        if not wallet_connected:
            account = Account.from_key(private_key)
            web3.eth.defaultAccount = account.address
            wallet_connected = True
            print("Wallet connected successfully.")
        else:
            web3.eth.defaultAccount = None
            wallet_connected = False
            print("Wallet disconnected.")
    except Exception as e:
        print("Error toggling wallet connection:", e)

def check_rpc_status():
    try:
        # Get syncing status
        syncing = web3.eth.syncing

        if syncing:
            print("Node is syncing...")
            print("Current block:", syncing['currentBlock'])
            print("Highest block:", syncing['highestBlock'])
        else:
            print("Node is up to date.")
    except Exception as e:
        print("Error while checking node status:", e)

def check_wallet_balance():
    try:
        if wallet_connected:
            balance_wei = web3.eth.get_balance(web3.eth.defaultAccount)
            balance_eth = balance_wei / 10**18  # Convert Wei to Ether
            print(f"Wallet balance: {balance_eth} ETH")
        else:
            print("Wallet Disconnected. Cannot check balance.")
    except Exception as e:
        print("Error while checking wallet balance:", e)

# Main loop
while True:
    rpc_endpoint = connect_to_rpc_endpoint(rpc_endpoint_file)
    private_key = read_private_key_from_file(private_key_file)
    
    if rpc_endpoint and private_key:
        web3 = Web3(Web3.HTTPProvider(rpc_endpoint))
        toggle_wallet_connection(private_key)  # Connect or disconnect wallet
        check_rpc_status()  # Check RPC node status
        check_wallet_balance()  # Check wallet balance
    
    time.sleep(10)  # Wait for 10 seconds
