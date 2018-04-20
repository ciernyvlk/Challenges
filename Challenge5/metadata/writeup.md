# Hidden in the sand

## What vulnerability I have to tested?

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

You have to set RHOST to IP_address and targeturi to /cgi-bin/vuln
 
## Complete solution

Yes, it was shellshock vulnerability and unfortunately our host is vulnerable to it.
When you set all attributes correctly and run the module, you can see Meterpreter console.
And there is file called flag. Just open it and see flag: n1ceJ0B.

#### Lessons learned

  * How we can do bruteforce on service throught metasploit.
  * How we can set username that we want its password.
