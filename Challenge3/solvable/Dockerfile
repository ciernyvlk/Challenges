FROM avatao/webide:ubuntu-14.04
RUN python3 /opt/setup.py /var/www/server /var/www/server/index.php \
    && chown -R user:user /var/www
VOLUME ["/tmp", "/var/log", "/var/lib/php5", "/var/www/server"]
VOLUME ["/var/www/codiad/data", "/var/www/codiad/plugins", "/var/www/codiad/themes", "/var/www/codiad/workspace"]
VOLUME ["/var/cache/apache2", "/var/run/apache2", "/var/lock/apache2"]
VOLUME ["/var/lib/mysql", "/var/run/mysqld"]

RUN mkdir /var/www/codiad/tmp
RUN echo "#autocomplete {\n\
        flag: cr4Wler\n\
}" >  /var/www/codiad/tmp/flag.css
RUN chmod 777 /var/www/codiad/tmp -R
USER user
EXPOSE 8008
CMD ["supervisord", "-c", "/etc/supervisor/apache-mysql.conf"]
