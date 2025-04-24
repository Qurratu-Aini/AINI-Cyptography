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


 ### **1.1 Updates the package index in Kali Linux** 



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

 ### **1.2 Verify Setup** 

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

