import hashlib

# Input message
message = "we"

# Encode and hash
hash_object = hashlib.sha256(message.encode())
hex_dig = hash_object.hexdigest()

print("✅ Message:", message)
print("🔐 SHA-256 Hash:", hex_dig)
