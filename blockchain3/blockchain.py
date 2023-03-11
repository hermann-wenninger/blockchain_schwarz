import random 
from rsa import generate_key_pair

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

primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

keys = []

for i in range(len(primes)):
    x = random.choice(primes)
    y = random.choice(primes)
    if x == y:
        continue
    x,y = generate_key_pair(x,y)
    keys.append((x,y))
#print(keys)

for i in range(len(keys)):
    with open('./wallets/wallet-{}.txt'.format(i), mode='w') as f:
        f.write(str(keys[i]))
        