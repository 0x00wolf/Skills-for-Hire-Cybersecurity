from Crypto.Hash import SHA512
message = 'Hello World'.encode('utf-8')
h = SHA512.new()
h.update(message)
print(h.hexdigest())