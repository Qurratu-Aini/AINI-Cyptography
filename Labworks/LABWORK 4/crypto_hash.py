import hashlib

#File to hash (same directory)
filename = "example.txt"

#Read file in binary mode
with open(filename, "rb") as f:
    file_data = f.read()

#Generate hash
hash_object = hashlib.sha256(file_data)
hex_dig = hash_object.hexdigest()

print("📄 File:", filename)
print("🔐 SHA-256 Hash:", hex_dig)
