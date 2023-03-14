from numba import jit
import random 
from time import time
import hashlib
from collections import OrderedDict
import json
from rsa import generate_key_pair
from create_keys import create_keys


genesis_block = {'previous_block':'','transaction':[{'sender':'1', 'empfaenger':'1', 'geldmenge':1000000, 'gas':0},], 'transaction_hash':''}
blockchain = [genesis_block]
open_transactions = []
miner = 'localhost'

user = [
    {'public_key':1,'private_key':3},
    {'public_key':1,'private_key':3},
    {'public_key':1,'private_key':3},
    {'public_key':1,'private_key':3},
    {'public_key':1,'private_key':3}
]
transaction_model = {'sender':'', 'empfaenger':'', 'geldmenge':0, 'gas':0}


create_keys('127.0.0.1')

def add_to_open_transactions(sender, empfaenger, geldmenge, miner=miner):
    '''put the values sender empfaenger geldmenge to open transactions and calculate 3% gas from the geldmenge'''
    time_stamp = time()
    gas = int(geldmenge)/100 * 3
    ot =  OrderedDict([('sender', sender),('empfaenger',empfaenger),('geldmenge', geldmenge),('miner', miner),('gas',str(gas)),('timestamp',str(time_stamp))])
    open_transactions.append(json.dumps(ot))
    print(open_transactions)


@jit(nopython=False)
def make_hash(transaction):
    '''make a valid secure hash sha256 and add nonce to ordereddict and return it'''
   
    nonce = 0
    while True:
        hash = hashlib.sha256((str(transaction) + str(nonce)).encode()).hexdigest()
        nonce += 1
        print(hash, nonce)
        if hash[0:4] == '0000':
            break
    #transaction = OrderedDict([(transaction,transaction)])
    print('###### make_hash ###### :',transaction,hash,nonce)
    return transaction, hash, nonce



def mine_block():
    take_last_transaction, his_hash, nonce = make_hash(open_transactions[-1])
    last_block, last_block_hash, last_block_nonce = make_hash(blockchain[-1]['transaction'])
    print(take_last_transaction, his_hash, nonce)
    print(last_block, last_block_hash, last_block_nonce)
    block = {}
    blockchain.append(block)


if len(open_transactions) > 1:
    mine_block()
    







print('1 for transaction')
print('2 hash transaction')
print('3 mine block')
while True:
    x = int(input('give us your choice'))
    match x:
        case 1:
            sender = input('den versender bitte: ')
            empfaenger = input('den empfänger bitte: ')
            geldmenge = input('bitte den betrag: ')
            add_to_open_transactions(sender, empfaenger, geldmenge)
        case 2:
            mine_block()
        case 3:
            pass