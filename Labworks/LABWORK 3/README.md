
# LABWORK-3
 
# Hands-on Exploration of Cryptographic Tools: Hashing, Encryption, and Digital Signatures 🔐


---
### 🎯 Objectives
- Encrypt and decrypt files using symmetric and asymmetric encryption

- Generate and verify hashes

- Create and verify digital signatures.
---

### 🛠️ Tools Used

- Kali Linux 

- openssl

## 📌 Task 1: Symmetric Encryption and Decryption using AES-256-CBC

We will use OpenSSL to encrypt and decrypt the message

### Step 1 :
Generate strong Random key (on Sender /Akmal)

```bash 
openssl rand -hex 32 > key.bin``` </pre>
This command to generate 256-bit (32bytes) key
```
```bash 
openssl rand -hex 16 > iv.bin``` </pre>
Generate a 128-bit (16 bytes) IV (Initialization Vector)
```

![alt text](image.png)

 IV is a unique value

 Why IV is important:

-Prevents pattern detection in encrypted data.

-Used in block cipher modes like CBC, CTR, GCM, etc.

Must be:

-Random or unique (for CBC)

-Nonce (number used once) for CTR/GCM

- Usually not secret, but must be unpredictable

### Step 2 : Create message

```bash 
Aku pilih madu.... sila sambung " > Akmal.txt
```

![alt text](image-1.png)

### Step 3 : Encrypt the Message with AES-256-CBC 

```bash 
openssl enc -aes-256-cbc -in akmal.txt -out akmal.enc -K $(cat key.bin) -iv $(cat iv.bin)```</pre>
```

Note:
•	-K requires a hex-encoded 256-bit key (64 hex chars).
•	-iv requires a hex-encoded 128-bit IV (32 hex chars).

![alt text](image-2.png)

### Step 4 : Decrypt the Message on Aini

```bash 
openssl enc -d -aes-256-cbc -in akmal.enc -out decrypted.txt -K $(cat key.bin) -iv $(cat iv.bin)
```

![alt text](image-3.png)

Check the decrypted message:

•	Open the decrypted.txt file to verify the message:

```bash 
cat decrypted.txt
```

It should contain the original message sent by Akmal.

![alt text](image-4.png)



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

**Encrypt the message using the Aini's private key**

```bash
openssl pkeyutl -encrypt -pubin -inkey public_key.pem -in ../rahsia.txt -out ../rahsia.enc
```

![alt text](image-13.png)

✅ This encrypts the plaintext using the public key. Only the private key can decrypt this.

 **Decrypt the message using the private key**

 On Aini’s machine:

1.Receive the file rahsia.txt from Akmal.

2.Decrypt it using your public key:

```bash
openssl pkeyutl -decrypt  -inkey private_key.pem -in rahsia.enc -out rahsia_decrypted.txt
```
![alt text](image-14.png)

**View the decrypted message**

```bash
cat decrypted.txt
```
![alt text](image-15.png)

**📄 Output:**

Harini nk makan apa ek ?

**Compare the decrypted content with the original message from rahsia.txt**

```bash
diff rahsia.txt decrypted.txt
```
![alt text](image-16.png)
If there's no output, the files are identical ✅


##  📌 Task 3: Hashing and Message Integrity using SHA-256

**3.1 Create a file to hash**

```bash
echo "aku pilih madu…. sila sambung" > akmal.txt
```

**3.2 Generate SHA-256 hash**

```bash
openssl dgst -sha256 akmal.txt
```
![alt text](image-17.png)

**📄 Output:**
SHA2-256(akmal.txt)= 3650645a30afffd40020afcc6c699081ea11bf2a08199f7ee745b3178d0c457d

**You can also try:**

```bash
sha256sum akmal.txt
```
![alt text](image-18.png)

✅ Both tools give the same hash but differ in formatting. openssl prefixes with SHA256(filename)=, while sha256sum shows the hash followed by the filename.

**3.3 Modify the File**

```bash
nano akmal.txt
```
![alt text](image-19.png)


**3.4  Generate Hash of the Modified File**

![alt text](image-20.png)

This just to show that even one character changed,the whole hash also will change



##  📌 Task 4 : Digital Signatures using RSA

**4.1 Generate RSA Keys for Akmal**


```bash
openssl genpkey -algorithm RSA -out labu_private.pem -pkeyopt rsa_keygen_bits:2048
```
![alt text](image-21.png)

Generate a 2048-bit RSA private key (Akmal keeps this secret)


**4.2 Extract the corresponding public key (to share with Aini)**

```bash
openssl rsa -pubout -in akmal_private.pem -out akmal_public.pem
```
![alt text](image-22.png)

**4.2 Create the document to sign**

Akmal creates the document:

```bash
echo "This is very important Senahhhhh." > agreement.txt
```

![alt text](image-23.png)


**4.2  Sign the document using Akmal’s private key**

Generate a SHA-256 digital signature

```bash
cd /home/akmal/Downloads
```

```bash
openssl dgst -sha256 -sign akmal_private.pem -out signature.bin ../agreement.txt
```

![alt text](image-24.png)


**4.3 Verify the signature using Labu’s public key**

Labi receives agreement.txt, signature.bin, and labu_public.pem, then verifies

```bash
openssl dgst -sha256 -verify labu_public.pem -signature signature.bin agreement.txt
```

If the file is unaltered, you’ll see:

**Verified OK**

**4.4 Simulate tampering and verify again**

Modify the document:

```bash
echo "This clause is added without consent." >> agreement.txt
```

Now verify again:

```bash
openssl dgst -sha256 -verify labu_public.pem -signature signature.bin agreement.txt
```

You’ll see:

**Verification Failure**

**🧠 Explanation:Why does verification fail?**

The signature is based on a hash of the original file content. When even one character is changed:
- The hash changes
- The signature no longer matches the new hash

So OpenSSL fails the verification to protect against tampering or forgery.




