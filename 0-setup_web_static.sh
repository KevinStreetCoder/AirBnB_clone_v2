#!/usr/bin/env bash

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file for testing
echo "Hello, this is a test." | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i "s|server_name _;|server_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n|" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

