from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Load private key
private_key = RSA.import_key(open("private.pem").read())

# Read encrypted message
with open("encrypted_rsa.txt", "r") as f:
    b64_cipher = f.read()

# Decode from Base64
ciphertext = base64.b64decode(b64_cipher)

# Decrypt
cipher_rsa = PKCS1_OAEP.new(private_key)
message = cipher_rsa.decrypt(ciphertext)

print("🔓 Decrypted message:", message.decode())