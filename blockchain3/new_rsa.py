from Crypto.PublicKey import RSA
import re
from binascii import a2b_base64, unhexlify
from Crypto.Util.py3compat import tobytes
from Crypto.Util.Padding import unpad
from Crypto.Cipher import DES, DES3, AES


def _EVP_BytesToKey(data, salt, key_len):
    d = [ b'' ]
    m = (key_len + 15 ) // 16
    for _ in range(m):
        nd = MD5.new(d[-1] + data + salt).digest()
        d.append(nd)
    return b"".join(d)[:key_len]



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

def decode(pem_data, passphrase=None):
    """Decode a PEM block into binary.
    Args:
      pem_data (string):
        The PEM block.
      passphrase (byte string):
        If given and the PEM block is encrypted,
        the key will be derived from the passphrase.
    Returns:
      A tuple with the binary data, the marker string, and a boolean to
      indicate if decryption was performed.
    Raises:
      ValueError: if decoding fails, if the PEM file is encrypted and no passphrase has
                  been provided or if the passphrase is incorrect.
    """

    # Verify Pre-Encapsulation Boundary
    r = re.compile(r"\s*-----BEGIN (.*)-----\s+")
    m = r.match(pem_data)
    if not m:
        raise ValueError("Not a valid PEM pre boundary")
    marker = m.group(1)

    # Verify Post-Encapsulation Boundary
    r = re.compile(r"-----END (.*)-----\s*$")
    m = r.search(pem_data)
    if not m or m.group(1) != marker:
        raise ValueError("Not a valid PEM post boundary")

    # Removes spaces and slit on lines
    lines = pem_data.replace(" ", '').split()

    # Decrypts, if necessary
    if lines[1].startswith('Proc-Type:4,ENCRYPTED'):
        if not passphrase:
            raise ValueError("PEM is encrypted, but no passphrase available")
        DEK = lines[2].split(':')
        if len(DEK) != 2 or DEK[0] != 'DEK-Info':
            raise ValueError("PEM encryption format not supported.")
        algo, salt = DEK[1].split(',')
        salt = unhexlify(tobytes(salt))

        padding = True

        if algo == "DES-CBC":
            key = _EVP_BytesToKey(passphrase, salt, 8)
            objdec = DES.new(key, DES.MODE_CBC, salt)
        elif algo == "DES-EDE3-CBC":
            key = _EVP_BytesToKey(passphrase, salt, 24)
            objdec = DES3.new(key, DES3.MODE_CBC, salt)
        elif algo == "AES-128-CBC":
            key = _EVP_BytesToKey(passphrase, salt[:8], 16)
            objdec = AES.new(key, AES.MODE_CBC, salt)
        elif algo == "AES-192-CBC":
            key = _EVP_BytesToKey(passphrase, salt[:8], 24)
            objdec = AES.new(key, AES.MODE_CBC, salt)
        elif algo == "AES-256-CBC":
            key = _EVP_BytesToKey(passphrase, salt[:8], 32)
            objdec = AES.new(key, AES.MODE_CBC, salt)
        elif algo.lower() == "id-aes256-gcm":
            key = _EVP_BytesToKey(passphrase, salt[:8], 32)
            objdec = AES.new(key, AES.MODE_GCM, nonce=salt)
            padding = False
        else:
            raise ValueError("Unsupport PEM encryption algorithm (%s)." % algo)
        lines = lines[2:]
    else:
        objdec = None

    # Decode body
    data = a2b_base64(''.join(lines[1:-1]))
    enc_flag = False
    if objdec:
        if padding:
            data = unpad(objdec.decrypt(data), objdec.block_size)
        else:
            # There is no tag, so we don't use decrypt_and_verify
            data = objdec.decrypt(data)
        enc_flag = True

    return (data, marker, enc_flag)