FROM avatao/ubuntu:14.04

RUN apt-get update
RUN apt-get install default-jdk -y
RUN groupadd tomcat
RUN useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat

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

RUN echo "description \"Tomcat Server\"\n\
  start on runlevel [2345]\n\
  stop on runlevel [!2345]\n\
  respawn\n\
  respawn limit 10 5\n\
  setuid tomcat\n\
  setgid tomcat\n\
  env JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre\n\
  env CATALINA_HOME=/opt/tomcat\n\
  env JAVA_OPTS=\"-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom\"\n\
  env CATALINA_OPTS=\"-Xms512M -Xmx1024M -server -XX:+UseParallelGC\"\n\
  exec $CATALINA_HOME/bin/catalina.sh run\n\
  post-stop script\n\
    rm -rf $CATALINA_HOME/temp/*\n\
  end script"> /etc/init/tomcat.conf
RUN initctl reload-configuration
RUN initctl start tomcat

RUN echo "<?xml version='1.0' encoding='utf-8'?>\
<tomcat-users>\
  <role rolename=\"tomcat\"/>\
  <role rolename=\"admin\"/>\
  <role rolename=\"role1\"/>\
  <role rolename=\"manager\"/>\
  <role rolename=\"manager-gui\"/>\
  <user username=\"root\" password=\"tomcat\" roles=\"admin,role1,tomcat,manager,manager-gui\"/>\
  <user username=\"role1\" password=\"root\" roles=\"admin,role1,tomcat,manager,manager-gui\"/>\
  <user username=\"admin\" password=\"s3cret\" roles=\"role1,manager-gui,tomcat,manager\"/>\
  <user username=\"dumb\" password=\"role1\" roles=\"manager,tomcat,role1,manager-gui\"/>\ 
  <user username=\"manager\" password=\"manager\" roles=\"admin,manager,tomcat,role1,manager-gui\"/>\ 
</tomcat-users>"  > /opt/tomcat/conf/tomcat-users.xml

RUN initctl restart tomcat
RUN /opt/tomcat/bin/startup.sh
EXPOSE 8080
CMD /opt/tomcat/bin/catalina.sh run
