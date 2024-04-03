#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
#Installs Nginx
#Creates the folder /data/web_static/releases/
#Creates the folder /data/web_static/shared/
#Creates the folder /data/web_static/releases/test/
#Creates a fake HTML file /data/web_static/releases/test/index.html
#Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
#Gives ownership of the /data/ folder to the ubuntu user AND group
#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
