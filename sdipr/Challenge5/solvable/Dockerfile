FROM avatao/ubuntu:14.04

#update base image
RUN apt-get update
RUN apt-get install default-jdk -y
RUN groupadd tomcat
RUN useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat

#installing tomcat vulnerable version and make initial settings of it
#ADD http://apache.mirrors.ionfish.org/tomcat/tomcat-7/v7.0.85/bin/apache-tomcat-7.0.85.tar.gz /tmp/
ADD https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.85/bin/apache-tomcat-7.0.85.tar.gz /tmp/
RUN mkdir /opt/tomcat
RUN tar xzvf /tmp/apache*tar.gz -C /opt/tomcat --strip-components=1
RUN cd /opt/tomcat
RUN chgrp -R tomcat /opt/tomcat
RUN ls -all /opt/tomcat
RUN pwd
RUN chmod -R g+r /opt/tomcat/conf
RUN chmod g+x /opt/tomcat/conf

RUN chown -R tomcat /opt/tomcat/webapps/ /opt/tomcat/work/ /opt/tomcat/temp/ /opt/tomcat/logs/
COPY ./solvable/ /

RUN initctl reload-configuration
RUN initctl start tomcat

RUN initctl restart tomcat
RUN /opt/tomcat/bin/startup.sh
EXPOSE 8080
CMD /opt/tomcat/bin/catalina.sh run
