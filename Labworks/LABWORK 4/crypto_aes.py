from Crypto.Cipher import AES
import base64

# Helper: Unpadding function
def unpad(data):
    return data[:-data[-1]]

# Paste received values here
b64_cipher=" TYdaeBBnweN7pbcjeDYLK3bKXWOr9lzws3yCXR3AzBnMAvvyuzCKOW7UW1pvaIzQ"
b64_key ="Bt3+a+1zqOz7L6JpkhoZlSf95qBUfR+7kn0/Bl7396c=="
b64_iv = "fClKMFXdlHBYJb5y+HUyuA=="

# Decode from base64
ciphertext = base64.b64decode(b64_cipher)
key = base64.b64decode(b64_key)
iv = base64.b64decode(b64_iv)

# Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(ciphertext))

# Show result
print("🔓 Decrypted message:", decrypted.decode())
