# Spider and his Webspider

## What tool to use?

Cost: 0%

Tool for crawling.

## What payload/exploit to use?

Cost: 40%

```bash
use auxiliary/scanner/http/crawler
```
 
## What is necessary to set up on the module?

Cost: 20%

It is necessary to set host ip address, port number in module.

## How to set up values on the module?

Cost: 30%

set RPORT port and 
set RHOST IP_address

## Complete solution

When choosing the correct module and settings, we will see list of results that were found.
In active pages and components search, we can see the line that comprises flag.css. We insert the address into the browser where we see the content of the file which includes the flag. 
The content shows that the flag for this task is the word cr4Wler.

#### Lessons learned

  * How to use crawler in metasploit.
 
