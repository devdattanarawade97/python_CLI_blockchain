
import datetime
import hashlib
import json
from transactions import Transactions
from verify_blockchain import Verify_Blockchain


# own files
import utility.valid_hashing as valid_hashing
import save_data


class Blockchain():
    print(__name__)
    MINING_REWARD = 10
    owner_address = 'sam'
    __nonce = 1
    __GENESIS_BLOCK = {
        'index': 0,
        'previous_hash': 0,
        'current_hash': 0,
        'nonce': 1,
        'timestamp': str(datetime.datetime.now()),
        'transactions': 0
    }
    __participants = set()
    # intializes genesis block

    def __init__(self, hosting_node, __blockchain=[[__GENESIS_BLOCK]], __open_transaction=[]):
        self.blockchain = __blockchain
        self.open_transaction = __open_transaction
        print('\n--------intialized genesis block successfully!!!--------')
        save_data.read_all_data(self.blockchain, self.open_transaction)
        print('\n--------loaded blockchain successfully!!!--------')

        self.hosting_node = hosting_node

        print(f'hosting node : {self.hosting_node}')

    # returns last block of blockchain

    def get_last_block(self):
        return self.blockchain[-1]

    # returns user entered transaction amount
    def get_transaction_details(self):
        reciepent_address = input('\n please enter receipent address : ')
        tx_amount = float(input('\n please enter valid transaction amount : '))
        return (reciepent_address, tx_amount)

   # returns to choose option for user
    def choose_option(self):
        user_choice = input(
            '\n--------please choose valid option-------- \n a. Add transaction \n b. Mine a new Block \n c. Check all participants \n d. Quit transaction \n Your choice is :  ')
        return user_choice

   # returns current block details
    def get_current_transaction_block(self):
        current_block = self.blockchain[len(self.blockchain)-1]
        return current_block

    #     return is_valid

    def find_current_hash(self):
        encoded_block = json.dumps(
            self.open_transaction, sort_keys=True).encode()
        current_hash = hashlib.sha256(encoded_block).hexdigest()
        return current_hash

    # consensus algorithm uses proof of work to find nonce and valid hash . this function returns valid nonce number and hash

    def proof_of_work(self, nonce):

        valid_proof = False
        last_block = self.get_last_block()
        previous_nonce = last_block[0]['nonce']

        while valid_proof is False:
            valid_hash = valid_hashing.find_valid_hash(nonce, previous_nonce)

            if valid_hash[0:4] == '0000':
                valid_proof = True
                return (nonce)
            else:
                nonce += 1

    # # miner mines new block by using consensus algorithm . consensus algorithm uses proof of work to find nonce and valid hash

    def mine_new_block(self):
        last_block = self.get_last_block()

        previous_hash = last_block[0]['current_hash']

        print(f"\n previous hash : {previous_hash}")

        nonce = self.proof_of_work(self.__nonce)
        self.__nonce = nonce
        current_hash = self.find_current_hash()
        print(f'nonce  : {nonce} and current hash : {current_hash}')
        block = {
            # 'previous_hash': last_block['previous_hash'],
            'index': len(self.blockchain)+1,
            'previous_hash': previous_hash,
            'current_hash': current_hash,
            'nonce': nonce,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.open_transaction
        }

        self.blockchain.append([block])
        print(f'hosting node : {self.hosting_node}')


# blockchain = Blockchain("cddd")  # type: ignore
# blockchain.front_screen()
