## ENDER (AINI)(GENERATE PUBLIC AND PRIVATE KEY)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

#Generate RSA key pair (2048 bits)
key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

#Save keys to files
with open("private.pem", "wb") as f:
    f.write(private_key)

with open("public.pem", "wb") as f:
    f.write(public_key)

#Message to encrypt
message = b"Hello from Aini, CB123456 - Cryptography Lab!"

#Encrypt message with public key
recipient_key = RSA.import_key(open("public.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
ciphertext = cipher_rsa.encrypt(message)

#Base64 encode ciphertext to send
b64_cipher = base64.b64encode(ciphertext).decode()

#Save to file or share via WhatsApp
with open("encrypted_rsa.txt", "w") as f:
    f.write(b64_cipher)

print("✅ Encrypted message (Base64):", b64_cipher)


## RECEIVER (AKMAL)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

#Load private key
private_key = RSA.import_key(open("private.pem").read())

#Read encrypted message
with open("encrypted_rsa.txt", "r") as f:
    b64_cipher = f.read()

#Decode from Base64
ciphertext = base64.b64decode(b64_cipher)

#Decrypt
cipher_rsa = PKCS1_OAEP.new(private_key)
message = cipher_rsa.decrypt(ciphertext)

print("🔓 Decrypted message:", message.decode())

