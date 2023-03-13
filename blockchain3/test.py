from hashlib import blake2b
h = blake2b()
h.update(b'a aa ')
print(h.hexdigest())