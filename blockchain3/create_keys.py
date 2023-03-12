import random 
import os
from rsa import generate_key_pair



def create_keys(ip_adress):
    if not os.path.exists("./wallets/wallet-9.txt"):
        primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

        keys = []

        for i in range(len(primes)+1):
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
                f.write('\n')
                f.write(str({'amount': 100}))
                f.write('\n')
                f.write(ip_adress)