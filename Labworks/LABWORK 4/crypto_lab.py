from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = cipher.iv
    return iv, ct_bytes

def aes_decrypt(iv, ct_bytes, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt.decode()

# Example usage
key = get_random_bytes(16)  # 128-bit key
message = "Cryptography Lab by NUR QURRATU'AINI BALQIS,NWS23010039!"

iv, ciphertext = aes_encrypt(message, key)
print("Encrypted:", ciphertext.hex())

plaintext = aes_decrypt(iv, ciphertext, key)
print("Decrypted:", plaintext)