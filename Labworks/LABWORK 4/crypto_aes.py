

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

#Helper: Padding function (PKCS7-style)
def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

#Your message
message = b"NUR QURRATU'AINI BALQIS ,NWS23010039"

#Generate a 256-bit (32-byte) key and a 16-byte IV
key = get_random_bytes(32)  # AES-256
iv = get_random_bytes(16)   # IV must be 16 bytes

#Create cipher object with AES-256 in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

#Encrypt the padded message
ciphertext = cipher.encrypt(pad(message))

#Encode values to base64 for safe transfer
b64_cipher = base64.b64encode(ciphertext).decode()
b64_key = base64.b64encode(key).decode()
b64_iv = base64.b64encode(iv).decode()

#Print to send to your friend
print("🔐 Encrypted (Base64):", b64_cipher)
print("🔑 Key (Base64):", b64_key)
print("🧊 IV (Base64):", b64_iv)








