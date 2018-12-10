Your boss fired the “dumb” user. Good job (in positive way, of course ??)
Now, something harder. In the company, rumor has it there is a vulnerability in the system, some problem with Bash. Many systems had this problem a couple of years ago and some still have it. 
Could you test the vulnerability of our system? The rumours mentioned some vuln file.

When finding the vulnerability marked by its CVE, it is necessary to find the vulnerable file on which we’ll use the unit because this vulnerability can have various vulnerable parts, thus it is necessary to find the correct ones :-).

As part of this task is the creation of reverse shell which Avatao platform does not support, it is necessary to use tcp bind payload which will firstly run one port where the connection opens and then second port (already with payload setting changed) which enables us to work with Meterpret using the established connection.

PS: Do not forget, that the IP and port below won't accept netcat connections (despite the message).

