import sha256
print('sha256',sha256.generate_hash("Hello World").hex())

genesis_block = {'previous_block':'', 'index':0, 'transactions':[]}
blockchain = [genesis_block]
open_transactions = []
owner = 'hmannx'
participants = {}
participants =  set(participants)

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain or None if the blockchain is empty"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(reciver, sender = owner ,amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain
    Arguments:
       :sender - the coinsender
       :recipient - the coinempfänger
       :amount - how much coins
     """
    transaction = {'sender':sender, 'reciver':reciver, 'amount':amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(reciver)


def mine_block():
    last_block = blockchain[-1] 
    hashed_block = hash_block(last_block)
    #for key in last_block:
    #    value = last_block[key]
    #    hashed_block = hashed_block + str(value)
    print('########',hashed_block)
    block= {'previous_hash':hashed_block,
            'index':len(blockchain),
            'transactions': open_transactions }
    blockchain.append(block)

def hash_block(block):
    return '-'.join([str(block[key])for key in block])



def get_transaction_value():
    
    """ Returns the input of the user (a new transaction amount) as a float 
         and the recipient of the coins you send                            """
    
    tx_recipient = input('enter the reciver of your transaction: ')
    tx_amount = float(input('Your transaction amount: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print('-|'*33)


def verify_chain():
    for (index,block)in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False 
    return True
    # block_index = 0
    # is_valid = True
    # for block_index in range(len(blockchain)):
    #     if block_index == 0:
    #         continue
    #     elif blockchain[block_index][0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index += 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    


waiting_for_input = True
while waiting_for_input:
    print('Please wähle: ')
    print('1. Add a new value to the blockchain')
    print('2. Mine new block')
    print('3. Output the blockchain blocks')
    print('h. Manipulate the chain')
    print('q. Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        reciver, amount = tx_data
        add_transaction(reciver, amount=amount)
        print('open transactions: ', open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain)>=1:
            blockchain[0] = {'previous_block':'', 'index':0, 'transactions':[{'sender':'Limbus','reciver':'Manu','amount':0.1}]}
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list')
    if not verify_chain():
        print_blockchain_elements()
        print('WARNING: Invalid blockchain')
        break
        #waiting_for_input =  False


print('Done!')
