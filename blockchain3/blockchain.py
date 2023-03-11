import random 
from time import time
from collections import OrderedDict
from rsa import generate_key_pair
from create_keys import create_keys

blockchain =[]
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

def add_to_open_transactions(sender, empfaenger, geldmenge, miner):
    time_stamp = time.time()
    gas = geldmenge/100 * 3
    OrderedDict([('sender', sender),('empfaenger',empfaenger),('geldmenge', geldmenge),('miner', miner),('gas',gas),('timestamp',time_stamp)])

