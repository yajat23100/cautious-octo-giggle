from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98&sa=D&source=editors&ust=1705739185400871&usg=AOvVaw1rqreiexMNMj3zZ1fa31Pi'
web3 = Web3(Web3.HTTPProvider(API_url))

Block_data = web3.eth.getBlock(19046573)
print('Block_data:', Block_data)

print('gasUsed:', Block_data ['gasUsed'])
print('Total difficulty:', Block_data ['difficulty'])

print('transaction data :', Block_data ['transactions'])
transaction = web3.eth.get_transaction('0x2ce85b9aabddbf910f44c41b47be60d126d3065c19f2cd3fb5c8aba8ff478f04')
print('data', transaction)