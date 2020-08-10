FROM httpd:2.4.46-alpine
RUN apk update && apk add mc apache2 apache2-proxy
COPY src/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY src/httpd-vhosts.conf /usr/local/apache2/conf/extra/
