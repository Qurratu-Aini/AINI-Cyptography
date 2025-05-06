## task 1

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

- AES: Provides the AES encryption/decryption functions.

- get_random_bytes: Generates cryptographically secure random bytes (for keys/IVs).

- pad/unpad: Ensures data aligns with AES block size (16 bytes) by adding/removing padding.


def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = cipher.iv
    return iv, ct_bytes

- AES.new(key, AES.MODE_CBC)

Creates an AES cipher object with:

key: 16/24/32-byte secret key (128/192/256-bit).

MODE_CBC: Cipher Block Chaining mode (requires IV for security).

- pad(message.encode(), AES.block_size)

Encodes the message to bytes (e.g., "Hello" → b'Hello').

Pads the bytes to a multiple of 16 bytes (AES block size).
Example: If the message is 10 bytes, 6 bytes of padding are added.

- cipher.encrypt()
Encrypts the padded message using AES-CBC.

- cipher.iv
The IV (random 16-byte value) is generated automatically. It ensures identical messages encrypt differently.

- Returns (iv, ct_bytes)
The IV and ciphertext are needed for decryption.


def aes_decrypt(iv, ct_bytes, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt.decode()

# Example usage
key = get_random_bytes(16)  # 128-bit key
message = "Cryptography Lab by NUR QURRATU'AINI BALQIS,NWS23010039!"

iv, ciphertext = aes_encrypt(message, key)
print("Encrypted:", ciphertext.hex())

Encrypted: 43cd2e731e300b9500f34d8de043c227f43cac9405ab207878daf53375106f5f4c116726ce684d98a32f634986630f995ee8ab57ace06ce1e689a6195507069f
Decrypted: Cryptography Lab by NUR QURRATU'AINI BALQIS,NWS23010039!















## Task 2


