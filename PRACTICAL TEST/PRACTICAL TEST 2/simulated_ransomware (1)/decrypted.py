from Crypto.Cipher import AES
import os
from hashlib import sha256

# === Key Recovery ===
KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]

# === Remove PKCS#7 Padding ===
def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# === Decrypt a single .enc file ===
def decrypt_file(input_path, output_path):
    with open(input_path, "rb") as f:
        ciphertext = f.read()

    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)

    with open(output_path, "wb") as f:
        f.write(plaintext)

    print(f"✅ Decrypted: {input_path} -> {output_path}")

# === Batch decrypt all files in a folder ===
def batch_decrypt(input_folder="../simulated_ransomware/locked_files", output_folder="decrypted"):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".enc"):
            input_path = os.path.join(input_folder, filename)
            output_filename = filename.replace(".txt.enc", ".txt")
            output_path = os.path.join(output_folder, output_filename)
            decrypt_file(input_path, output_path)

if __name__ == "__main__":
    batch_decrypt()
