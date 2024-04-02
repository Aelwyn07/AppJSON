FROM debian:stable-slim
RUN apt-get update && apt-get install -y apache2
WORKDIR /var/www/html
RUN rm -f /var/www/html/index.html
COPY index.html /var/www/html/index.html
COPY script.js /var/www/html/script.js
EXPOSE 80
ENTRYPOINT apache2ctl -D FOREGROUND