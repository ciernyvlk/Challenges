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
nmap -sV IP_address
```

## Complete solution

We want to see running services therefore we need parameter -sV in nmap -> probe open ports to determine service/version info.
When you run the command above you will see running ssh service at port 666. So the flag is: ssh.

#### Lessons learned

  * Metasploit can use also tools like nmap.
  * How to use active scanning through Metasploit.
 
