import pickle

# this method saves all blockchain data to pickle


def save_all_data(blockchain, open_transaction):
    try:
        with open('blockchain.p', mode='wb') as file:
            save_data = {

                'chain': blockchain,
                'ot': open_transaction

            }

            file.write(pickle.dumps(save_data))
    except (IOError):
        print('writing file error')


# this method retrives all blockchain data from pickle
def read_all_data(blockchain, open_transaction):

    try:
        with open('blockchain.p', mode='rb') as file:
            file_content = pickle.loads(file.read())
            blockchain = file_content['chain']
            open_transaction = file_content['ot']
            print(file_content)

            return (blockchain, open_transaction)
    except (IOError):
        print('file not found')
