FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y -q install openssh-server
RUN mkdir -p /var/run/sshd
RUN echo "Port 666" > /etc/ssh/sshd_config
#RUN /etc/init.d/sshd restart

EXPOSE 80
EXPOSE 443
EXPOSE 666

CMD ["/usr/sbin/sshd", "-D"]