# LABWORK-2 
 
# Cryptographic Attacks: Cracking Weak Password Hashes and Exploiting Poor Authentication in Databases

### 📌 Objectives

- Identify and exploit cryptographic weaknesses in database authentication and password storage.

- Perform offline hash cracking after discovering password hashes in a vulnerable database.

- Investigate real-world cryptographic failures and propose secure solutions.

---

### ⚙️ Tools Used

- Kali Linux (Attacker Machine)

- MariaDB/MySQL (Target Database)

- Wireshark (Packet Sniffing)

- John the Ripper (Hash Cracking)

- hashid / hash-identifier (Hash Detection)

---

## ✅ Task 1: Service Enumeration and Initial Access 🔍


 ### **1.1 Finding the Target IP and updates the package index in Kali Linux** 

```bash
nmap -Pn -p 3306 192.168.249.128
```

![alt text](image-4.png)

Try to look the target port on metasploit2 open or not which is mysql


```bash
sudo apt update
```

![alt text](image.png)

**Explanation:**

This command updates the package index in Kali Linux. It ensures your system has the latest information about available software and dependencies before installing anything new, which helps avoid broken or outdated packages.

 ### **Other Setup Commands**

 
```bash
sudo apt install mariadb-server -y
sudo systemctl start mariadb
sudo systemctl enable mariadb
```
![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

---- 

 ### **1.3 Verify Setup** 

 ```bash
dpkg -L mariadb-server | grep mysql_secure_installation
```

**Explanation:**
This checks the installation path for mysql_secure_installation, which helps harden MariaDB by setting root passwords and remov

---

 ### **Connection Attempts**

 ```bash
mysql -h 192.168.249.128 -u root --ssl-mode=DISABLED
mysql -h 192.168.249.128 -u root -p --ssl-mode=DISABLED
```

**Issue Encountered:
Both commands failed. Possible causes:**

- The server requires a password.
- SSL/TLS is misconfigured or unsupported.

**Explanation:**

`--ssl-mode=DISABLED` disables SSL negotiation but the server may still expect it. SSL isn't always supported by default, especially in test or misconfigured environments.


**ESuccessful Access:**

 ```bash
mysql -h 192.168.249.128 -u root --skip-ssl
```

--skip-ssl bypasses encryption entirely, sending data (including passwords) in plaintext, posing a significant security risk.

---


## ✅ Task 2 : Enumeration of Users and Authentication Weaknesses 👤 

### **2.1 Database Enumeration:** 

 ```bash
mysql -h 192.168.249.128 -u root --skip-ssl
```



