FROM avatao/ubuntu:16.04
#update base image and install snmp protocol, set common attributes
RUN apt-get update
RUN apt-get install supervisor -y
RUN apt-get update \
	&& apt-get install snmpd -qy
RUN echo "rocommunity public" > /etc/snmp/snmpd.conf
COPY ./solvable/ /
#EXPOSE 22
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
