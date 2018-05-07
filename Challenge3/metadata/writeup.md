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
Last part contains information about running processes that you can see process with name Flag:g00d. So, the flag for this challenge is g00d.

#### Lessons learned

  * How to obtain some information from snmp protocol with right community.
