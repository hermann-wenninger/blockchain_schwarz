import random 
from time import time
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
    gas = geldmenge/100 * 3
    ot =  OrderedDict([('sender', sender),('empfaenger',empfaenger),('geldmenge', geldmenge),('miner', miner),('gas',gas),('timestamp',time_stamp)])
    open_transactions.append(json.dumps(ot))
    print(open_transactions)










add_to_open_transactions('hans22', 'peter555',123)
add_to_open_transactions('hans33', 'peter6666',123)
add_to_open_transactions('hans44', 'peter7777777777777',123)

print('###########################################',open_transactions)


print('1 for transaction')
print('2 for mining')
print('3 for test the rest')
x = int(input('give us your choice'))
match x:
    case 1:
       sender = input('den versender bitte: ')
       empfaenger = input('den empfänger bitte: ')
       geldmenge = input('bitte den betrag: ')
    case 2:
        print('3333')