from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64

# Load private key (i've already generated it)
private_key = RSA.import_key(open("private.pem").read())

# Message to sign
message = b"Digital signature test from Aini, CB123456"

# Hash the message first
hash_obj = SHA256.new(message)

# Sign the hash with your private key
signature = pkcs1_15.new(private_key).sign(hash_obj)

# Encode signature in base64 for transmission (optional)
b64_signature = base64.b64encode(signature).decode()

# Save signed message and signature
with open("signed_message.txt", "wb") as f:
    f.write(message)

with open("signature.txt", "w") as f:
    f.write(b64_signature)

# Output signature for debugging or to send
print("✅ Message signed!")
print("✉️ Signature (Base64):", b64_signature)

---

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