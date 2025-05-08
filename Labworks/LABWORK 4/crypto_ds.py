from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64

# Load/generate private key
private_key = RSA.import_key(open("private.pem").read())

# Message to sign
message = b"Digital signature test from Aini, CB123456"

# Hash the message
hash_obj = SHA256.new(message)

# Sign the hash with private key
signature = pkcs1_15.new(private_key).sign(hash_obj)

# Base64 encode the signature to send
b64_signature = base64.b64encode(signature).decode()

# Save message and signature to file
with open("signed_message.txt", "wb") as f:
    f.write(message)

with open("signature.txt", "w") as f:
    f.write(b64_signature)

print("✅ Message signed!")
print("✉️ Signature (Base64):", b64_signature)
