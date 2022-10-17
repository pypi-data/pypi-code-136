from web3client.Web3Client import Web3Client
from getpass import getpass

node_uri = "https://eth-mainnet.gateway.pokt.network/v1/5f3453978e354ab992c4da79"
private_key = getpass()

if len(private_key) != 64:
    raise Exception("Please provide a valid private key")

client = Web3Client(
    nodeUri=node_uri,
    privateKey=private_key,
)

nonce = client.getNonce()

print(">>> NONCE")
print(nonce)
