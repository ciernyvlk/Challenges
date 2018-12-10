# Scanner or Not?

## What type of tool is necessary to use?

Cost: 0%

Active scanner.

## What can be useful to run?

Cost: 40%

Try to use Nmap tool.

## How to set it up correctly?

Cost: 50%

run into metasploit console:
```bash
nmap -sV IP_address -p port
```

## Complete solution

We want to see running services therefore we need parameter -sV in nmap -> probe open ports to determine service/version info.
After the command execution, you can see that on the port the task ssh is running. That is why ssh is the flag for this task.

#### Lessons learned

  * Metasploit can use also tools like nmap.
  * How to use active scanning through Metasploit.
 
