# Ransomware Static & Dynamic Analysis Documentation

This analysis outlines the reverse engineering and decryption process for the file `simulated_ransomware.exe`, a simulated ransomware used in a practical exercise.

We conducted both static and dynamic analysis to understand how the ransomware operates, extract its logic, recover the encryption key, and successfully decrypt the locked files.

---

## Static Analysis

We begin by analyzing the binary using static techniques to gather insights without executing it. The file is a Windows executable with an `.exe` extension and appears unreadable when opened, suggesting it's compiled or packed.

We first calculated the hash of the ransomware binary using PowerShell’s `Get-FileHash` command to identify the file and ensure its integrity.

Next, we used **Detect It Easy (DIE)** to inspect the file's internal structure. The result shows that the file is a **PE (Portable Executable)** and packed using **PyInstaller**, a tool commonly used to package Python scripts into standalone executables. DIE also confirms the file was built using **Python 3.8**, which is important since only specific versions of decompilers support this.

---

## Extracting Embedded Files

Knowing that the ransomware was packaged with PyInstaller, we used **pyinstxtractor-ng.exe**, a PyInstaller archive extractor. The following command was used to extract the contents of the `.exe` file:

.\pyinstxtractor-ng.exe "simulated_ransomware.exe"

yaml
Copy code

After extraction, a new folder named `simulated_ransomware.exe_extracted` was created. Inside it, we found the bytecode file `simulated_ransomware.pyc`, which is a compiled Python script.

We attempted to read this `.pyc` file using `Get-Content` and confirmed that it was unreadable in its current state — which is expected for bytecode files.

---

## Decompiled to Source Code

To understand the internal workings of the ransomware, we decompiled the `.pyc` file back into Python source code using **uncompyle6**.

Before running the decompiler, we ensured that we were using Python 3.8 and activated our virtual environment:

.\venv38\Scripts\activate

javascript
Copy code

Then, we used this command to decompile the `.pyc` file:

uncompyle6 -o . simulated_ransomware.pyc

yaml
Copy code

This produced the readable file `simulated_ransomware.py`.

---

## Understanding the Ransomware Logic

Upon inspection of the source code in `simulated_ransomware.py`, we discovered the following functionality:

1. It defines a hardcoded key string using:

   ```python
   KEY_SUFFIX = "RahsiaLagi"
   KEY_STR = f"Bukan{KEY_SUFFIX}"
   KEY = sha256(KEY_STR.encode()).digest()[:16]
This key is derived from the SHA-256 hash of the string "BukanRahsiaLagi", and the first 16 bytes are used as the AES key.

It writes three plaintext files into a folder called locked_files:

maklumat1.txt

maklumat2.txt

maklumat3.txt

Each file contains motivational or instructional messages.

The ransomware then encrypts each .txt file using AES in ECB mode with PKCS#7 padding and saves the encrypted files as .txt.enc.

Finally, it deletes the original plaintext files, leaving only the encrypted versions behind.

Key Recovery and Vulnerabilities
The ransomware has a serious design flaw: the encryption key is hardcoded and not obfuscated, meaning anyone with access to the source code (like we now have) can regenerate the key.

The use of ECB (Electronic Codebook) mode is also insecure, as it does not use an IV (Initialization Vector) and leaks patterns in the data.

This means that with the key and knowledge of the algorithm, we can fully decrypt all the locked files without needing to brute-force anything.

Decryption Script
We wrote a Python script called decrypt.py to decrypt the .enc files. This script reads each encrypted file, decrypts it using the same key and mode, removes padding, and writes the plaintext to a decrypted/ folder.

The script performs the following:

Regenerates the same key from "BukanRahsiaLagi"

Decrypts each file with AES in ECB mode

Removes the padding

Saves the output with a .txt extension

After creating this script and placing it in the project directory, we executed it using:

nginx
Copy code
python decrypt.py
If the virtual environment is not activated, we ran:

Copy code
.\venv38\Scripts\activate
The output shows:

bash
Copy code
✅ Decrypted: locked_files/maklumat1.txt.enc -> decrypted/maklumat1.txt
✅ Decrypted: locked_files/maklumat2.txt.enc -> decrypted/maklumat2.txt
✅ Decrypted: locked_files/maklumat3.txt.enc -> decrypted/maklumat3.txt
This confirms successful decryption.

Decryption Results
After running the decryption script, a new folder named decrypted was created in the project root. It contains the original text files in plaintext form:

decrypted/maklumat1.txt

decrypted/maklumat2.txt

decrypted/maklumat3.txt

Each file contains the exact motivational message that was originally encrypted by the ransomware.

Final Notes
This practical demonstrates how insecure design choices in malware allow recovery of encrypted data. The use of:

Hardcoded keys

AES-ECB mode

No file integrity protection

No network communication or persistence

...makes this ransomware entirely reversible. This was a good simulation for understanding how static and dynamic analysis tools help in reverse engineering and building counter-scripts for malware.

All evidence including screenshots, decrypted files, source code, and this documentation are uploaded to the GitHub repository.

vbnet
Copy code

Let me know if you'd like a `.md` file generated or screenshots embedded with correct f