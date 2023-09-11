

from transactions import Transactions
from verify_blockchain import Verify_Blockchain
from save_data import save_all_data
from blockchain import Blockchain
from wallet import Wallet


class Node(Transactions, Verify_Blockchain):

    def __init__(self):
        self.wallet = Wallet()
        self.blockchain = Blockchain(self.wallet.public_key)

     # returns to choose option for user

    def choose_option(self):
        user_choice = input(
            '\n--------please choose valid option-------- \n a. Add transaction \n b. Mine a new Block \n c. Create keys \n d. Quit transaction \n Your choice is :  ')
        return user_choice

    """ front screen to user """

    def front_screen(self):

        while True:
            user_choice = self.choose_option()
            if user_choice == 'a' and self.blockchain.hosting_node != None:

                receipent_address, tx_amount = Blockchain.get_transaction_details(
                    self)  # type: ignore
                if tx_amount > 0:

                    Transactions.add_transaction(
                        self, receipent_address, tx_amount, self.blockchain.open_transaction)

                    print(
                        f'\n adding transaction and printing transactions : {self.blockchain.open_transaction}')

            elif user_choice == 'b':

                if len(self.blockchain.open_transaction) >= 1 and len(self.blockchain.blockchain) >= 1:
                    # Blockchain.mine_new_block()
                    self.blockchain.mine_new_block()
                    print(
                        f'\n mining new block and printing mined block : {self.blockchain.blockchain[-1]}')

                    print('\n--------validating blockchain--------')
                    is_valid = Verify_Blockchain.validate_blockchain(
                        self.blockchain.blockchain)
                    if (is_valid != True):
                        break
                    else:
                        print('\n--------blockchain is valid !!!--------')
                        print('\n saving blockchain data')
                        save_all_data(
                            self.blockchain.blockchain, self.blockchain.open_transaction)

                        print(
                            f'\n complete blockchain : {self.blockchain.blockchain}')
                        self.blockchain.open_transaction = []
                        print(
                            f'\n cleared open transaction {self.blockchain.open_transaction}')

                    # print(f'\n adding transaction and printing block : {self.blockchain[len(self.blockchain)-1]}'
                    #       )

                    print('_'*100)

                else:
                    print('\n no transactions found in open transactions')
                    continue

            elif user_choice == 'c':
                private_key, public_key = Wallet.create_keys(
                    self)  # type: ignore
                self.blockchain.hosting_node = public_key
                Transactions.owner_address = public_key
                print(
                    f'\n private key : {str(private_key)} public key : {str(public_key)}')

            elif user_choice == 'd':

                print('\n--------application quited successfully--------')

                break

            else:
                print(
                    '\nInvalid Input !!! please choose valid option or Create public keys to add transaction')

                continue


node = Node()
node.front_screen()
