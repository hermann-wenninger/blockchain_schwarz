from blockchain import blockchain, open_transactions

def save_data():
    with open('daten/blockchain.txt', 'w')as file:
        file.write(str(blockchain))
        file.write('\n')
        file.write(open_transactions)