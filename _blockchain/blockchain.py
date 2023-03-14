import sha256
from functools import reduce
import hashlib
import json
from collections import OrderedDict

from hash_util import  hash_block
#import save_data



print('sha256: ',sha256.generate_hash("Hello World").hex())

MIN_GAS = 0.001
genesis_block = {'previous_block':'', 'index':0, 'transactions':[],'proof':100}
blockchain = [genesis_block]
open_transactions = []
owner = 'hmannx'
participants =  set()



def load_data():
    with open('blockchain.txt', 'r')as file:
        content = file.readlines()
        global blockchain
        global open_transactions
        blockchain = json.loads(content[0][:-1])
        updated_blockchain =[]
        for block in blockchain:
            updated_block =  {
                            'previous_hash': block['previous_hash'],
                            'index': block['index'],
                            'proof': block['proof'],
                            'transactions':[OrderedDict(
                            [('sender', tx['sender']),
                            ('reciver',tx['reciver']),
                            ('amount', tx['amount'])])for tx in block['transactions']]} 
            updated_blockchain.append(updated_block)  
        blockchain = updated_blockchain              
        open_transactions = json.loads(content[1])
        updated_transactions = []
        for tx in open_transactions:
            updated_transaction = {
                [OrderedDict(
                            [('sender', tx['sender']),
                            ('reciver',tx['reciver']),
                            ('amount', tx['amount'])])]
            }
            updated_transactions.append(updated_transaction)
        open_transactions = updated_transactions
        print('######################################',blockchain)
        print('######################################', open_transactions)
        
load_data()




def save_data():
    with open('blockchain.txt', 'w')as file:
        file.write(json.dumps(blockchain))
        file.write('\n')
        file.write(json.dumps(open_transactions))


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print('function: -> valid_proof:',guess_hash)
   
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof



def get_last_blockchain_value():
    """ Returns the last value of the current blockchain or None if the blockchain is empty"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_balance(participant):
    ''' get the balance of sender and reciver'''
    amount_sent = 0
    amount_recived = 0
    
    open_tx_sender = [[tx['amount'] for tx in open_transactions if tx['sender'] == participant]]
    tx_sender = [[tx['amount'] for tx in block['transactions']if tx['sender']==participant]for block in blockchain]
    amount_sent = reduce(lambda tx_sum, tx_amt:tx_sum + sum(tx_amt) if len(tx_amt)>0 else tx_sum + 0,tx_sender,0 )
    #amount_recived = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt)>0)
    for coin in tx_sender:
         if len(coin)>0:
             amount_sent += coin[0]

    tx_sender.append(open_tx_sender)
    tx_reciver = [[tx['amount'] for tx in block['transactions']if tx['reciver']==participant]for block in blockchain]

    print('open_tx_sender',participant,open_tx_sender)
    print('tx_sender', tx_sender)
    print('tx_reciver', tx_reciver)
    amount_open_tx_sender = 0
    for coin in open_tx_sender:
        if len(coin)>0:
            amount_open_tx_sender+= coin[0]
    print('#### amount_open_tx_sender', amount_open_tx_sender)
    # tx_sender.append(open_tx_sender)

    

   
    
    for coin in tx_reciver:
         if len(coin)>0:
             amount_recived += coin[0]

    total = amount_recived - amount_sent
    return total


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']
        


def verify_transactions():
    return all([verify_transaction[tx]for tx in open_transactions])




def add_transaction(reciver, sender = owner ,amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain
    Arguments:
       :sender - the coinsender
       :recipient - the coinempfänger
       :amount - how much coins
     """
    #transaction = {'sender':sender, 'reciver':reciver, 'amount':amount}
    transaction = OrderedDict([('sender', sender),('reciver',reciver),('amount', amount)])
    if  verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(reciver)
        save_data()
        return True
    return False


def mine_block():
    last_block = blockchain[-1] 
    hashed_block = hash_block(last_block)
<<<<<<< HEAD:blockchain_left.py
    reward_transaction = {
        'sender': 'MINING',
        'reciver':owner, 
        'amount': MIN_GAS}
    copied_transactions = open_transactions[:]
    open_transactions.append(reward_transaction)
    print('########',hashed_block)
    block= {'previous_hash':hashed_block,
=======
    proof = proof_of_work()
    reward_transaction = {'sender': 'MINING','reciver':owner, 'amount': MIN_GAS}

    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    print('######## : ',hashed_block)
    block= {
            'previous_hash':hashed_block,
>>>>>>> 33e6de9bb563358757bc6b076c8fef0ce8e2aa0a:blockchain.py
            'index':len(blockchain),
            'transactions': copied_transactions,
            'proof': proof 
            }
    blockchain.append(block)
    save_data()
    return True





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
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
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
    print('4. print participants')
    print('5. verify transactions')
    print('h. Manipulate the chain')
    print('q. Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        reciver, amount = tx_data
        if add_transaction(reciver, amount=amount):
            print('added transaction succesfull')
        else:
            print('transaction verweigert!!!!!!!!')
        print('open transactions: ', open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('all transactions are ok')
        else:
            print('transactions are invalid')
    elif user_choice == 'h':
        if len(blockchain)>=1:
            blockchain[0] = {'previous_block':'', 'index':0, 'transactions':[{'sender':'Limbus','reciver':'Manu','amount':0.1}]}
    elif user_choice == 'q':
        waiting_for_input = False
        break
    else:
        print('Input was invalid, please pick a value from the list')
    if not verify_chain():
        print_blockchain_elements()
        print('WARNING: Invalid blockchain')
        break
    print(get_balance('hmannx'))
    print('the balance of {owner} is {number}'.format(owner = owner, number = get_balance(owner)))
else:
    print('user is not in our system')
        #waiting_for_input =  False


print('Done!')
