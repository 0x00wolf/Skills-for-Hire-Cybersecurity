from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import base64

class AESCrypto:

    def md5_hash(self, text):
        h = MD5.new()
        h.update(text.encode())
        return h.hexdigest()
    
    def __init__(self, key):
        self.key = self.md5_hash(key)

    def encrypt(self, cleartext):
        Block_Size = AES.block_size
        pad = lambda s: s + (Block_Size - len(s) % Block_Size) * chr(Block_Size - len(s) % Block_Size)
        cleartext_blocks = pad(cleartext)

        # create a random IV
        iv = Random.new().read(Block_Size)
        crypto = AES.new(self.key.encode(), AES.MODE_CBC, iv)
        return base64.b64encode(iv + crypto.encrypt(cleartext_blocks.encode()))
    
    def decrypt(self, enctext):
        enctext = base64.b64decode(enctext)
        iv = enctext[:16]
        crypto = AES.new(self.key.encode(), AES.MODE_CBC, iv)
        unpad = lambda s : s[:-ord(s[-1:])]
        return unpad(crypto.decrypt(enctext[16:]))
    
aes = AESCrypto('password123')
encrypted = aes.encrypt('Hello World')
print(encrypted)
decrypted = aes.decrypt(encrypted)
print(decrypted)
