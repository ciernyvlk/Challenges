Your boss thinks that scanning using the nmap tool was too easy. Can you scan it in a different way?

On the vulnerable host, you can find a task (this task runs on UDP port) which you can use in next step. Mostly, this task is used to monitor systems. Try to gain as much information about whole system as possible and I guarantee you that the flag will be somewhere there. In next step, I recommend you to find the unit linked to the running task on UDP port which enables you to find necessary information.

When searching the unit, it is necessary to choose the correct one. Many of them are destined for concrete types of systems.


PS: Do not forget, that the IP and port below won't accept netcat connections (despite the message).
