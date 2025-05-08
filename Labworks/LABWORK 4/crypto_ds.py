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
