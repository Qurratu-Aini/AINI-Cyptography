
# LABWORK-3
 
# Hands-on Exploration of Cryptographic Tools: Hashing, Encryption, and Digital Signatures 🔐


---
### 🎯 Objectives

---

### 🛠️ Tools Used

- Kali Linux 

- openssl

## 📌 Task 1: Symmetric Encryption and Decryption using AES-256-CBC


 ### **1.1 Generate a 256-bit (32-byte) random key:** 

```bash
openssl rand -out key.bin 32
```
✅ This creates a secure random binary file (key.bin) of 32 bytes, suitable for AES-256.

### **1.2 Generate a 128-bit (16-byte) random IV:** 

```bash
openssl rand -out iv.bin 16
```
✅ The IV (Initialization Vector) is required for CBC mode encryption to ensure

### **1.3 Create a plaintext message file:**

```bash
echo "You did great mal :)" > aini.txt
```
✅ This writes your test message to aini.txt, which will be encrypted.


### **🔒 Encryption**

### **1.4 Convert binary key and IV to hex format without line breaks:**

```bash
openssl enc -aes-256-cbc -in aini.txt -out aini.enc -K $(xxd -p key.bin) -iv $(xxd -p iv.bin)
```

![alt text](image.png)

 "aes-256-cbc" "d3b4"
usually happens because $(xxd -p key.bin) or $(xxd -p iv.bin) is producing line breaks or spaces, which messes up the -K or -iv option.

### **✅ Fix: Convert binary to hex without newline** ###

Try using xxd -p -c 256 to ensure it's all on one line:


```bash
KEY=$(xxd -p -c 256 key.bin)
```

```bash
IV=$(xxd -p -c 256 iv.bin)
```

✅ The -c 256 option ensures that the entire hex string is on one line. This prevents formatting errors when passing to OpenSSL.


### **🔍 Check values if needed:** ###

```bash
echo $KEY  
```
![alt text](image-1.png)

```bash
echo $IV  
```
![alt text](image-2.png)

This will ensure the key and IV are correctly passed to the openssl enc command.


### **1.5 Encrypt the message using AES-256-CBC:**

```bash
openssl enc -aes-256-cbc -in aini.txt -out aini.enc -K $KEY -iv $IV
```
✅ This encrypts the content of aini.txt using the specified key and IV and saves the output to aini.enc.


### **🔒 Decryption**

```bash
openssl enc -d -aes-256-cbc -in aini.enc -out decrypted_aini.txt -K $KEY -iv $IV 
```

### ** 1.6 Display the decrypted content:** ###

```bash
cat decrypted_aini.txt 
```

![alt text](image-3.png)

You did great mal :)



##  📌 Task 2: Asymmetric Encryption and Decryption using RSA

### **Generate a private RSA key (2048 bits):** ###

```bash
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
```

![alt text](image-4.png)


✅ This creates a private key (private_key.pem) using the RSA algorithm with a 2048-bit key size.

**Extract the corresponding public key**

```bash
openssl rsa -pubout -in private_key.pem -out public_key.pem
```
![alt text](image-11.png)

✅ This generates a public key (public_key.pem) from the private key.

- private_key.pem (only for Aini – keep secret)
- public_key.pem (to share with Akmal)

**Create a message file to encrypt**

```bash
echo "This is an RSA test message." > rsa_message.txt
```
![alt text](image-12.png)

**Encrypt the message using the Aini's public key**

```bash
openssl pkeyutl -encrypt -pubin -inkey public_key.pem -in ../rahsia.txt -out ../rahsia.enc
```

![alt text](image-13.png)

































TASK 4
Task 4: Digital Signatures using RSA (from scratch)
🎯 Scenario:
Labu wants to sign a document (agreement.txt) to prove to Labi that the message is authentic and hasn’t been tampered with.

🧪 Step-by-Step Lab Instructions
✅ Step 1: Generate RSA Keys for Labu
Generate a 2048-bit RSA private key (Labu keeps this secret):

openssl genpkey -algorithm RSA -out labu_private.pem -pkeyopt rsa_keygen_bits:2048

Extract the corresponding public key (to share with Labi)
openssl rsa -pubout -in akmal_private.pem -out akmal_public.pem  


✅ Step 2: Create the document to sign
Labu creates the document:
echo "This is the agreement between Labu and Labi." > agreement.txt


✅ Step 3: Sign the document using Labu’s private key
Generate a SHA-256 digital signature:
cd /home/akmal/Downloads
openssl dgst -sha256 -sign akmal_private.pem -out signature.bin ../agreement.txt

This creates signature.bin, the signed hash of the document.


✅ Step 4: Verify the signature using Labu’s public key
Labi receives agreement.txt, signature.bin, and labu_public.pem, then verifies:

openssl dgst -sha256 -verify labu_public.pem -signature signature.bin agreement.txt
If the file is unaltered, you’ll see:
Verified OK

✅ Step 5: Simulate tampering and verify again
Modify the document:

echo "This clause is added without consent." >> agreement.txt
Now verify again:

openssl dgst -sha256 -verify labu_public.pem -signature signature.bin agreement.txt
You’ll see:
Verification Failure

🧠 Explanation: Why does verification fail?
The signature is based on a hash of the original file content. When even one character is changed:
The hash changes
The signature no longer matches the new hash
So OpenSSL fails the verification to protect against tampering or forgery.