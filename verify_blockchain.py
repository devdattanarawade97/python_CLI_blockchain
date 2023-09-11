

class Verify_Blockchain:

        def validate_blockchain(blockchain):
        # last_block = self.blockchain[len(self.blockchain)-2]
        # current_block = (self.blockchain[(len(self.blockchain)-1)])[0]

        # print(f'last block={self.blockchain[len(self.blockchain)-2]}',
        #       f'current block ={(self.blockchain[(len(self.blockchain)-1)])[0]}')
            is_valid = False
            block_index = 0
            while block_index < len(blockchain)-1:
                print(f'\n block index {block_index}')
                last_block = blockchain[block_index]
                current_block = blockchain[block_index+1]
                print(f'\n last block ={last_block}',
                    f'\n current block = {current_block}')
                previous_hash = last_block[0]['current_hash']
                current_hash = current_block[0]['previous_hash']
                print(f'\n current hash of previous block ={previous_hash}',
                    f'\n previous hash of current block = {current_hash}')
                if (previous_hash == current_hash):

                    block_index += 1
                    is_valid = True

                else:
                    print('\n Invalid blockchain !!!')
                    return False

            return is_valid