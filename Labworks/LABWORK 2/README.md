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


**Successful Access:**

 ```bash
mysql -h 192.168.249.128 -u root --skip-ssl
```

--skip-ssl bypasses encryption entirely, sending data (including passwords) in plaintext, posing a significant security risk.

---


## ✅ Task 2 : Enumeration of Users and Authentication Weaknesses 👤 

## **Database Enumeration:**

 ```bash
USE mysql;
```
![alt text](image-6.png)

**Switch to System DB:**

Selects the mysql system database that stores user and permission info

**List Available Tables:**


 ```bash
SHOW TABLES;
```
![alt text](image-7.png)

Displays all tables in the currently selected database.

**View User Table:**

```bash
SELECT User, Host, Password FROM mysql.user;
```
![alt text](image-8.png)


This is a serious security vulnerability which is an example of broken authentication and poor cryptographic practice (i.e., no password hash stored).

- Users with no password (blank field)
- Users with easy-to-crack password hashes
- Any duplicate or strange access rules

### ❔Question: Is no password a cryptographic failure? ❔

Yes it is and it skips cryptographic protection. A secure system always authenticates users using a cryptographic mechanism (like password hashing + salting).


## ✅ Task 3: Password Hash Discovery and Hash Identification

Now that we know MySQL don't have anypassword, let's find a Databasewhich has one, in this case **`DVWA`** or `Damn Vulnerable Web Application`

## **Enter DVWA database**

```sql
USE dvwa
```

Now that we're in the database, Lets start digging ⛏️

## **Look for info from user** 

```sql
SHOW TABLES;
```

![alt text](image-9.png)


```sql
SELECT * FROM users LIMIT 5;
```
![alt text](image-10.png)


**Explanation:**

Retrieves the first 5 rows only. This avoids loading a large dataset into the terminal and speeds up inspection.


---

 ### **3.1 Identify the hash** 

### Let's try with admin user !!

![alt text](image-11.png)


### Let's try to identidy what hash it is!!

