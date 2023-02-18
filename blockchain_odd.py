blockchain = [['genesisblock']]

def veryfy_chain():
    b_index = 0
    is_valid = True
    for block in blockchain:
        if block[0] == blockchain[-1]:
            is_valid = True
            print('blockchain is valid')
        else:
            is_valid = False
            print('blockchain is abbbfffffffffffffffffffuuuuuuuuuuckkkkked')
            break
        b_index +=1
        return is_valid


def get_user_choice():
    user_input = int(input('give me your choice (1 or 2 or q)'))
    
    return user_input


def get_user_input():
    a = (input('schiebs rein: '))
    if  a == '':
        a = float(0.0)
    return a

def add_value(last_trans, trans):
    blockchain.append([last_trans,trans])
    #print(blockchain)
    return blockchain

def last_eintrag():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def print_blockchain():
    for block in blockchain:
            print('geminter block')
            print(block)
        


while True:
    us = get_user_choice()
    if us == 1:
        amount = get_user_input()
        add_value(amount, last_eintrag())
    elif us == 2:
        print_blockchain()
    elif us =='q':
        continue
    elif us == 3:
        print('end-of-ether')
        break
    if us == 9:
        print("weiter im text")
    veryfy_chain()
        








