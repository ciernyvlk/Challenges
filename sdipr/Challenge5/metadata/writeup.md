# Dumb User

## What type of attack to use?

Cost: 5%

Brute-force attack.

## What is vulnerable? 

Cost: 25%

Tomcat Manager.

## What payload/exploit to use?

Cost: 40%

```bash
use auxiliary/scanner/http/tomcat_mgr_login
 ```
 
## How to set up values in the module correctly?

Cost: 20%

set username to user dumb, ip address to IP_address and port

## Complete solution

When choosing the correct module and settings, run it and you will see brute-force attack on tomcat manager service.
This result shows us that we found more passwords different users - dumb, admin, manager, role1 and root. The result is the password of dumb user, thus the flag is role1.
#### Lessons learned

  * How we can do brute-force on service through metasploit.
  * How we can set username that we want the password of.
