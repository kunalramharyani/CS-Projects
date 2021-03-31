# Legacy 

This is the write-up for a machine called Legacy.

## Scanning & Enumeration 

Let's start with an nmap scan:

```markdown 
nmap -T4 -A -p- 10.10.10.4
```

Relevant results of the scan:

```markdown
PORT STATE SERVICE VERSION
139/tcp open netbios-ssn Microsoft Windows netbios-ssn
445/tcp open microsoft-ds Windows XP microsoft-ds
3389/tcp closed ms-wbt-server
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp
 Host script results:
|_clock-skew: mean: 5d00h28m04s, deviation: 2h07m16s, median: 4d22h58m04s
|_nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:b9:83:73 (VMware)
| smb-os-discovery: 
| OS: Windows XP (Windows 2000 LAN Manager)
| OS CPE: cpe:/o:microsoft:windows_xp::-
| Computer name: legacy
| NetBIOS computer name: LEGACY\x00
| Workgroup: HTB\x00
|_ System time: 2019-09-27T14:23:02+03:00
| smb-security-mode: 
| account_used: guest
| authentication_level: user
| challenge_response: supported
|_ message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)
```

## SMB Exploitation 
This machine has a Windows XP OS with an SMB port (139+445) open. Also, the smb message signing is disabled.
The Metasploit module **exploit windows/smb/ms08_067_netapi** is useful in this case. Configure RHOSTS, check your targets and then run the exploit. 
This will start a Meterpreter session and the session will be running as **NT Authority\SYSTEM**.
