# You need to install the pycryptodome package for this program to work.
# pip install pycryptodome
# read the docs: https://pycryptodome.readthedocs.io/

from Crypto.Hash import SHA256
message = 'Hello World'.encode('utf-8')
h = SHA256.new()
h.update(message)
print(h.hexdigest())