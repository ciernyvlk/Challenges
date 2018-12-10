# Somewhere in the Host
## What can be used in the next step?

Cost: 20%

SNMP protocol

## What module to use?

Cost: 30%

```bash
use auxiliary/scanner/snmp/snmp_enum
```

## What is necessary to set up on the module?

Cost: 25%

You have to set RHOST to IP_address and port.
 
## Where is the flag hidden?

Cost: 15%

In the running processes.
 
 
## Complete solution

After choosing the correct module and settings, you can see the result of module run where is a lot of information about the target host. Last part of this information includes a statement of running processes where the flag is hidden under the name Flag:G00d. The result of this task is the word G00d.

#### Lessons learned

  * How to obtain some information from snmp protocol with right community.
