FROM avatao/ubuntu:16.04
RUN apt-get update
RUN apt-get install supervisor -y
RUN apt-get update \
	&& apt-get install snmpd -qy
RUN echo "rocommunity public" > /etc/snmp/snmpd.conf

#RUN 

RUN echo "[supervisord]\n\
nodaemon=true\n\
\n\
[program:snmpd]\n\
command=/usr/sbin/snmpd\n\
#command=service ntp start\n\
autostart=true\n\
autorestart=true\n\
priority=958\n\
\n\
[program:flag]\n\
command=bash -c 'exec -a Flag:G00d sleep 1000000000' &\n\
autostart=true\n\
autorestart=true\n\
priority=958" > /etc/supervisor/supervisord.conf

#EXPOSE 22
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
