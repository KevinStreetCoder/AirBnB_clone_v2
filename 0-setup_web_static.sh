#!/usr/bin/env bash
# Setup a web server for the deployment of web_static.

# Update package lists and install Nginx
apt update -y
apt install -y nginx

# Create directory structure if it doesn't already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a sample HTML file for testing
echo "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>" | tee /data/web_static/releases/test/index.html

# Create a symbolic link to the /data/web_static/releases/test/ folder
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data

# Update Nginx configuration to serve the content at /data/web_static/current/
# with alias /hbnb_static
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# Restart Nginx to apply the configuration
sudo service nginx restart
