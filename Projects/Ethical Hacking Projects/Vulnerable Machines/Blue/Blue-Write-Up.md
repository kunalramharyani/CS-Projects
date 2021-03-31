# Blue

This is the write-up for a machine called Blue.

## Scanning & Enumeration

Let's start with an nmap scan:

```markdown
nmap -T4 -A -p- 10.10.10.40
```

Relevant results of the scan:

```markdown
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows
```

## SMB Exploitation 

This machine has a Windows 7 OS with an SMB port open (139+445) and has message signing disabled or enabled but not required. It is most likely vulnerable to the exploit known as **EternalBlue** or **MS17-010**.
The metasploit module **exploit windows/smb/ms17_010_eternalblue** is useful in this case. Configure RHOSTS, set a staged or a stageless payload, check your targets, and run the exploit.
This will start a Meterpreter session and the session will be running as **NT Authority\SYSTEM**.
