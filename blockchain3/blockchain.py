import random 
from time import time
import hashlib
from collections import OrderedDict
import json
from rsa import generate_key_pair
from create_keys import create_keys

blockchain = []
open_transactions = []
miner = 'localhost'
genesis_block = {'previous_block':'','transaction':[],'proof':0}
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



def make_hash(open_transactions):
    '''make a valid secure hash sha256 and add nonce to ordereddict and return it'''
    transaction = open_transactions[-1]
    nonce = 0
    while True:
        x = hashlib.sha256((transaction + str(nonce)).encode()).hexdigest()
        nonce += 1
        print(x, nonce)
        if x[0:2] == '0000':
            break
    transaction = OrderedDict([(transaction,transaction),('nonce',nonce)])
    print('###### make_hash ###### :',transaction)
    return transaction











print('1 for transaction')
print('2 for mining')
print('3 for test the rest')
while True:
    x = int(input('give us your choice'))
    match x:
        case 1:
            sender = input('den versender bitte: ')
            empfaenger = input('den empfänger bitte: ')
            geldmenge = input('bitte den betrag: ')
            add_to_open_transactions(sender, empfaenger, geldmenge)
        case 2:
            make_hash(open_transactions)