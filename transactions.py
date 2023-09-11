

class Transactions:

    
    owner_address = 'vikki'

    # appends new transaction to open transactions when user send amount
    def add_transaction(self, receipent_address, tx_amount, open_transaction):

        transaction = {
            'sender': self.owner_address,
            'receipent': receipent_address,
            'amount': tx_amount


        }
        
        open_transaction.append(transaction)

        return (open_transaction)
