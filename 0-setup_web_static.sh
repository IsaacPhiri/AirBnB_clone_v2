#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.

# Update and Install nginx
echo "Beginning installation of nginx"
if ! which nginx > /dev/null 2>&1; then
	echo "Nginx is not installed"
else
	echo "Updating"
	sudo apt update -y
	echo "Installing nginx"
	sudo apt install nginx -y
fi

# Create directories
if [[ ! -e /data/web_static/releases/ ]]; then
	sudo mkdir -p /data/web_static/releases/test
	sudo mkdir -p /data/web_static/shared/
fi

# Create a fake HTML file
sudo echo "<h1>Welcome, this is {$hostname} Server</h1>" > /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu group
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
replace="server_name _;"
new="server_name tecsee.tech;\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"
sudo sed -i "s/$replace/$new/" /etc/nginx/sites-enabled/default

# Restart nginx
sudo service nginx restart
