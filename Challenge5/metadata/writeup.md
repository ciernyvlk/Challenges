# Dumb user

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

set username to user dumb, ip address to IP_address and port to 8080

## Complete solution

When you set the module correctly, run it and you will see bruteforce attack on tomcat manager service.
Some of the accounts will have guessed the password correctly. Now you have to only choose the correct one what is for user dumb - flag: role1.

#### Lessons learned

  * How we can do bruteforce on service throught metasploit.
  * How we can set username that we want its password.
