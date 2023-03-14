from Crypto.PublicKey import RSA


def create_keys():
    participants = set()
    for i in range(10):
        key = RSA.generate(1024)
        private_key = key.export_key()
        file_out = open(f"wallets/private-{i}.pem", "wb")
        file_out.write(private_key)
        file_out.close()

        public_key = key.publickey().export_key()
        
        file_out = open(f"wallets/receiver-{i}.pem", "wb")
        file_out.write(public_key)
        file_out.close()
        
    
create_keys()

def create_set():
    list = []
    dict = {}
    for i in range(10):
        with open(f"wallets/receiver-{i}.pem", 'rb')as f:
            x = f.readlines()
            #print('xxxxxxxxxxx',len(x))
            print(x.remove(x[0]),x.remove(x[-1]))
            dict[i] = x
            #list.append(x)
    #print(list)       
    #print(dict)
    #print('###########################',b"".join(dict[0]))

    for i in range(len(dict)):
        #print(dict[i][0:-1])
        for j in dict[i]:
            print(j[0:-1])
            dict[i]=join(j[0:-1])
            #print(j,"".join(str(j[0:-1])))
    # for kw in dict:
    #     print(kw, "::", dict[kw][0:-1])
create_set()