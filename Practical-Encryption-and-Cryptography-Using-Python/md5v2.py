from Crypto.Hash import MD5
import sys

if len(sys.argv) == 2:
    message = sys.argv[1].encode('utf-8')
    h = MD5.new()
    h.update(message)
    print(h.hexdigest())
else:
    print('\n'*40 + "Usage:\nmd5v2.py 'Message to encrypt'")
    print("Message must be encapsulated in ''")
