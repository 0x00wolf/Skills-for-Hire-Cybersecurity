from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
from Crypto import Random
from Crypto.Hash import SHA256
import base64

class CryptoRSA:
    PRIVATE_KEY_FILE = "privatekey.pem"
    PUBLIC_KEY_FILE = "publickey.pem"

    def __init__(self):
        return
    
    def __save_file(self, contents, file_name):
        f = open(file_name, 'wb')
        f.write(contents)
        f.close()

    def __read_file(self, file_name):
        f = open(file_name, 'r')
        contents = f.read()
        f.close()
        return contents
    
    def __generate_random(self):
        return Random.new().read()
    
    def __sha256(self, input):
        sha256 = SHA256.new()
        sha256.update(input.encode())
        return sha256
    
    def generate_keys(self):
        keys = RSA.generate(4096)
        private_key = keys.exportKey("PEM")
        public_key = keys.publickey().exportKey("PEM")
        self.__save_file(private_key, self.PRIVATE_KEY_FILE)
        self.__save_file(public_key, self.PUBLIC_KEY_FILE)
        print("Public & Private Keys: generated and saved successfully")

    def encrypt(self, cleartext, public_keypath=None):
        if (public_keypath == None):
            public_keypath = self.PUBLIC_KEY_FILE

        public_key = RSA.importKey(self.__read_file(public_keypath))
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(cleartext.encode())
        return base64.b64encode(encrypted_data)

    def decrypt(self, cipher_text, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE

        cipher_text = base64.b64decode(cipher_text)
        private_key = RSA.importKey(self.__read_file(private_key_path))
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(cipher_text)
    
    def sign(self, textmessage, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE

        private_key = RSA.importKey(self.__read_file(private_key_path))
        signature = PKCS1_PSS.new(private_key)
        return signature.sign(self.__sha256(textmessage))
    
    def verify(self, signed_signature, textmessage, public_key_path=None):
            if public_key_path == None:
                public_key_path = self.PUBLIC_KEY_FILE

            public_key = RSA.importKey(self.__read_file(public_key_path))
            verifier = PKCS1_PSS.new(public_key)
            verification = verifier.verify(self.__sha256(textmessage), signed_signature)
            print(verification)

bobcat = CryptoRSA()
bobcat.generate_keys()
encrypted_data =  bobcat.encrypt("Hello World")
print(encrypted_data)
decrypted_data = bobcat.decrypt(encrypted_data)
print(decrypted_data)

signed_signature = bobcat.sign("Hello World")
bobcat.verify(signed_signature, "Hello World")
