# Hidden in the Sand

## What vulnerability to test?

Cost: 30%

CVE-2014-6271

## What is vulnerable?

Cost: 15%

cgi-bin scripts

## What module to use?

Cost: 25%

```bash
use exploit/multi/http/apache_mod_cgi_bash_env_exec
 ```

## How to set up the values correctly in the module?

Cost: 20%

You have to set RHOST to IP_address and targeturi to /cgi-bin/vuln and also set payload to linux/x64/shell/bind_tcp
 
## Complete solution

Yes, it was the shellshock vulnerability and the host was vulnerable. After the correct setup of all attributes and the unit run, we can observe Meterpreter running in which we can see the flag folder.  

After opening this folder, the text: n1ceJ0B shows which is the flag in our case. 

Those were vulnerabilities {CVE-2014-6271} (Vulnerability known as Shellshock in which the most vulnerable is very commonly used Bash. Influenced versions are from 1.13 to 4.3. When the Bash is executed using Bash, original instances can export variable environment and environments’ definitions to new instance. Definitions of functions are exported using coding into the list of variable environments as variables followed by function’s definition.  New instance of Bash scans the list of variables when starting and transfers them back to internal functions, so called run functions. Defective version of Bash don’t verify whether those functions are valid and this enables the attacker to execute any command.  
Vulnerable parts can contain function ForceCommand in ssh, mod_cgi a mod_cgid units in Apache, scripts executed by unspecified DHCP clients) and {CVE-2014-6278} (This vulnerability affects aslo CVE-2014-6271 Bash 1.13 to 4.3. Bash, parses wrongly the functions’ definitions in variable environments. This vulnerability exists because of incomplete fix of vulnerability CVE-2014-6271.)







# Magic Tool

## How to start metasploit console?

Cost: 20%

If you want to start metasploit console, run command
```bash
msfconsole
```
## What command I have to use to find the flag?

Cost: 30%

You have to run 
```bash 
search
```
in running metasploit console.

## What is full solution?

Cost: 40%

You have to run command
```bash
search nmap
```
After that, you will see list of exploits/payloads/... in a row with description Setuid Nmap Exploit
you will see 2012-07-19 as date of disclosure.



## Complete solution

As the solution is a year of this date, the flag is 2012.

#### Lessons learned

  * What is metasploit.
  * How to run metasploit console.
  * How to search between metasploit modules.
Wow! Good job! Now you know how to run this magical tool. But your Boss does not want only starting the Metasploit Framework. He wants also to work with it. Next step is to scan some host. It could be vulnerable. Can you try to use some tool by metasploit or payload/exploit to scan that host? 
Good chance!

Your flag is service running on a port. (If you see service filtered please restart the challenge.)
Tip: try to use external tool through Metasploit.

PS: Do not forget, that the IP and port below won't accept netcat connections (despite the message).

# Scanner or Not?

## What kind of tool I have to use?

Cost: 0%

Active scanner.

## What could be useful to run?

Cost: 40%

Try to use Nmap tool.

## How to set it properly?

Cost: 50%

run into metasploit console:
```bash
nmap -sV IP_address -p port
```

## Complete solution

We want to see running services therefore we need parameter -sV in nmap -> probe open ports to determine service/version info.
When you run the command above you will see running ssh service at port. So the flag is: ssh.

#### Lessons learned

  * Metasploit can use also tools like nmap.
  * How to use active scanning through Metasploit.
Your Boss thinks that scanning through nmap was too easy. Could you try to scan it another way?

In the vulnerable host you can find some service (this service is running on UDP port) to use for next step. Try to find out as much information as possible and I guarantee you that the flag will be between that info. For the second step I recommend you to use module related to service running on a UDP port. 

PS: Do not forget, that the IP and port below won't accept netcat connections (despite the message).
# Somewhere in the Host
## What could I use for next step?

Cost: 20%

SNMP protocol

## What module I have to use?

Cost: 30%

```bash
use auxiliary/scanner/snmp/snmp_enum
```

## How to set the module?

Cost: 25%

You have to set RHOST to IP_address and port.
 
## Where is the flag hidden?

Cost: 15%

In the running processes.
 
 
## Complete solution

When you set all attributes correctly and run the module, you can see a lot of information about the target host from SNMP protocol.
Last part contains information about running processes that you can see process with name Flag:G00d. So, the flag for this challenge is G00d.

#### Lessons learned

  * How to obtain some information from snmp protocol with right community.

Nice job. Now you know how to scan target host. Your next job is to find all active web sites
on the IP_address. Are you bold enough to do that?
The flag could be somewhere in the webpages or plugins or …

Tip: you do not have to do it manually. If one module does not find the flag, try another one (description of this challenge could be helpful).

PS: Do not forget, that the IP and port below won't accept netcat connections (despite the message).

# Spider and his Webspider

## What kind of tool I have to use?

Cost: 0%

Crawler tool.

## What payload/exploit I have to use?

Cost: 40%

```bash
use auxiliary/scanner/http/crawler
```
 
## How to set it?

Cost: 20%

It is necessary to set host ip address, port number in module.

## Values to set in module

Cost: 30%

set RPORT port and 
set RHOST IP_address

## Complete solution

When we run crawler module with correct parameters, we will see list of results that were found.
Between them you will see flag.css. When you run the whole path into browser you will see the flag: cr4Wler.

#### Lessons learned

  * How to use crawler in metasploit.
Good job!
You are master of crawling. Now something harder. Your Boss knows that he has some dumb
employees. Could you help him to retrieve password of user "dumb"? He knows only username and
that this user works with tomcat service. But that all.
It is up to you.
Your flag will be password of this dumb user.
PS: Do not forget, that the IP and port below won't accept netcat connections (despite the message).

# Dumb User

## What kind of attack can I use?

Cost: 5%

Brute-force attack.

## What is vulnerable? 

Cost: 25%

Tomcat Manager.

## What payload/exploit I have to use?

Cost: 40%

```bash
use auxiliary/scanner/http/tomcat_mgr_login
 ```
 
## How to set it?

Cost: 20%

set username to user dumb, ip address to IP_address and port

## Complete solution

When you set the module correctly, run it and you will see brute-force attack on tomcat manager service.
Some of the accounts will have guessed the password correctly. Now you have to choose only the correct one which is for user dumb - flag: role1.

#### Lessons learned

  * How we can do brute-force on service through metasploit.
  * How we can set username that we want the password of.

Your Boss fired the dumb employee. Good job (in a possitive way of course ;) ).
Now something harder. In the enterprise there are some rumours about vulnerability in the system.
Something like bash problem? A lot of systems had problem with this vulnerability a few years ago or they still have it.
Could you test our system if it is vulnerable? In the rumours it was mentioned something like filename vuln.

PS: Do not forget, that the IP and port below won't accept netcat connections (despite the message).

# Hidden in the Sand

## What vulnerability I have to test?

Cost: 30%

CVE-2014-6271

## What could be vulnerable?

Cost: 15%

cgi-bin scripts

## What module I have to use?

Cost: 25%

```bash
use exploit/multi/http/apache_mod_cgi_bash_env_exec
 ```

## How to set the module?

Cost: 20%

You have to set RHOST to IP_address and targeturi to /cgi-bin/vuln and also set payload to linux/x64/shell/bind_tcp
 
## Complete solution

Yes, it was the shellshock vulnerability and the host was vulnerable. After the correct setup of all attributes and the unit run, we can observe Meterpreter running in which we can see the flag folder.  

After opening this folder, the text: n1ceJ0B shows which is the flag in our case. 

Those were vulnerabilities {CVE-2014-6271} (Vulnerability known as Shellshock in which the most vulnerable is very commonly used Bash. Influenced versions are from 1.13 to 4.3. When the Bash is executed using Bash, original instances can export variable environment and environments’ definitions to new instance. Definitions of functions are exported using coding into the list of variable environments as variables followed by function’s definition.  New instance of Bash scans the list of variables when starting and transfers them back to internal functions, so called run functions. Defective version of Bash don’t verify whether those functions are valid and this enables the attacker to execute any command.  
Vulnerable parts can contain function ForceCommand in ssh, mod_cgi a mod_cgid units in Apache, scripts executed by unspecified DHCP clients) and {CVE-2014-6278} (This vulnerability affects aslo CVE-2014-6271 Bash 1.13 to 4.3. Bash, parses wrongly the functions’ definitions in variable environments. This vulnerability exists because of incomplete fix of vulnerability CVE-2014-6271.)


#### Lessons learned

  * How we can use exploit and payload at the same time.
  * How we can create session.
