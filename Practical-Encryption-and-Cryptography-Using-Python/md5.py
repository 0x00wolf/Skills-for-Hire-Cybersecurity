# You need to install the pycryptodome package for this program to work.
# pip install pycryptodome
# read the docs: https://pycryptodome.readthedocs.io/

from Crypto.Hash import MD5
# In Python3 you must encode the string into a byte array or the program will fail.
message = 'Hello World'.encode('utf-8')
h = MD5.new()
h.update(message)
print(h.hexdigest())

