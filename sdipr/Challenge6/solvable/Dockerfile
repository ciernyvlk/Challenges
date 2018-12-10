FROM avatao/ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install apache2 -y
RUN apt-get install wget -y

#install vulnerable version of bash
RUN wget http://snapshot.debian.org/archive/debian/20130101T091755Z/pool/main/b/bash/bash_4.2%2Bdfsg-0.1_amd64.deb -O /tmp/bash_4.2+dfsg-0.1_amd64.deb && \
 dpkg -i /tmp/bash_4.2+dfsg-0.1_amd64.deb

#configuration of vulnerable cgi-bin scripts for bash and initial setting for running these scripts

COPY ./solvable/ /

RUN chmod 777 -R /etc/apache2/
RUN chmod 777 -R /usr/lib/cgi-bin/
RUN a2enmod cgid
RUN a2enconf serve-cgi-bin

RUN chown www-data:www-data /var/www/html/index.html

RUN apt-get autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
