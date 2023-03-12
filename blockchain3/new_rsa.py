from Crypto.PublicKey import RSA
import hashlib

def create_keys():
    for i in range(10):
        key = RSA.generate(1024)
        private_key = key.export_key()
        file_out = open(f"private-{i}.pem", "wb")
        file_out.write(private_key)
        file_out.close()

        public_key = key.publickey().export_key()
        file_out = open(f"receiver-{i}.pem", "wb")
        file_out.write(public_key)
        file_out.close()


def create_set():
    list = []
    dict = {}
    for i in range(10):
        with open(f"receiver-{i}.pem", 'rb')as f:
            x = f.readlines()
            print('xxxxxxxxxxx',len(x))
            print(x.remove(x[0]),x.remove(x[-1]))
            dict[i] = x
            list.append(x)
    print(list)       
    print(dict)
    
    print(b)
create_set()