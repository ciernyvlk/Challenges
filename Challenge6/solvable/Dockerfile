FROM avatao/ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install apache2 -y
RUN apt-get install wget -y

#install vulnerable version of bash
RUN wget http://snapshot.debian.org/archive/debian/20130101T091755Z/pool/main/b/bash/bash_4.2%2Bdfsg-0.1_amd64.deb -O /tmp/bash_4.2+dfsg-0.1_amd64.deb && \
 dpkg -i /tmp/bash_4.2+dfsg-0.1_amd64.deb

#configuration of vulnerable cgi-bin scripts for bash and initial setting for running these scripts
RUN echo "#!/bin/bash\n\
\n\
echo \"Content-type: text/html\";\n\
echo \"\"\n\
\n\
uptime" > /usr/lib/cgi-bin/vuln

RUN echo "<VirtualHost *:80>\n\
        ServerAdmin webmaster@localhost\n\
\n\
        DocumentRoot /var/www/html\n\
        <Directory />\n\
                Options FollowSymLinks\n\
                AllowOverride None\n\
        </Directory>\n\
        <Directory /var/www/html/>\n\
                Options Indexes FollowSymLinks MultiViews\n\
                AllowOverride None\n\
                Order allow,deny\n\
                allow from all\n\
        </Directory>\n\
\n\
        ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/\n\
        <Directory \"/usr/lib/cgi-bin\">\n\
                AllowOverride None\n\
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch\n\
#               Order allow,deny\n\
#               Allow from all\n\
                Require all granted\n\
        </Directory>\n\
\n\
        ErrorLog ${APACHE_LOG_DIR}/error.log\n\
\n\
        # Possible values include: debug, info, notice, warn, error, crit,\n\
        # alert, emerg.\n\
        LogLevel warn\n\
\n\
        CustomLog ${APACHE_LOG_DIR}/access.log combined\n\
</VirtualHost>" > /etc/apache2/sites-enabled/000-default
RUN echo "<VirtualHost *:80>\n\
        ServerAdmin webmaster@localhost\n\
\n\
        DocumentRoot /var/www/html \n\
        <Directory />\n\
                Options FollowSymLinks\n\
                AllowOverride None\n\
        </Directory>\n\
        <Directory /var/www/html/>\n\
                Options Indexes FollowSymLinks MultiViews\n\
                AllowOverride None\n\
                Order allow,deny\n\
                allow from all\n\
        </Directory>\n\
\n\
        ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/\n\
        <Directory \"/usr/lib/cgi-bin\">\n\
                AllowOverride None\n\
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch\n\
                Order allow,deny\n\
                Allow from all\n\
        </Directory>\n\
\n\
        ErrorLog ${APACHE_LOG_DIR}/error.log\n\
\n\
        # Possible values include: debug, info, notice, warn, error, crit,\n\
        # alert, emerg.\n\
        LogLevel warn\n\
\n\
        CustomLog ${APACHE_LOG_DIR}/access.log combined\n\
</VirtualHost>" > /etc/apache2/sites-available/default

RUN chmod 777 -R /etc/apache2/
RUN chmod 777 -R /usr/lib/cgi-bin/
RUN a2enmod cgid
RUN a2enconf serve-cgi-bin

#simple web text for shellshock vulnerability
RUN echo "<html>\n\
    <head><title>ShellShock</title></head>\n\
    <body>\n\
        <pre>The script is at /cgi-bin/vuln</pre>\n\
    </body>\n\
</html>" > /var/www/html/index.html

RUN chown www-data:www-data /var/www/html/index.html
RUN echo "n1ceJ0B" > /usr/lib/cgi-bin/flag

RUN apt-get autoremove
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
