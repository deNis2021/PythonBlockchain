from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    print("failed to connect to the Hardhat blockchain.")
else:
    print("connected to the Hardhat blockchain\n")
    latest_block = web3.eth.block_number
    print(f"latest block: {latest_block}\n")

    for block_num in range(latest_block + 1):
        block = web3.eth.get_block(block_num)
        print(f"-------- Block № {block_num} --------")
        print(f"  hash: {block.get('hash').hex() if block.get('hash') else 'N/A'}")
        print(f"  parent hash: {block.get('parentHash').hex()}")
        print(f"  timestamp: {block.get('timestamp')}")
        print(f"  transaction: {len(block.get('transactions'))}")
        print("-" * 67)