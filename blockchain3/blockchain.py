import random 
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
transaction_model = {'sender':'', 'empfaenger':'', 'menge':0, 'gas':0}


create_keys()

