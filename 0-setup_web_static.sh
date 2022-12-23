#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static
 
#install nginx
#sudo apt purge nginx nginx-common nginx-core -y
#sudo apt remove nginx nginx-common nginx-core -y
#sudo apt autoremove -y

sudo apt-get update -y
sudo apt-get install nginx -y
 
#create neccessary folders
sudo mkdir -p '/data/web_static/shared/'
sudo mkdir -p '/data/web_static/releases/test'
sudo touch '/data/web_static/releases/test/index.html'
 
# index.html message
sudo echo "Welcome, this is $(hostname) server" |sudo tee /data/web_static/releases/test/index.html
 
# creates symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
 
# ownership
sudo chown -hR ubuntu:ubuntu /data/
 
# configuration to serve the content
sudo sed -i "59i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default
 
# restart nginx server
sudo service nginx restart
