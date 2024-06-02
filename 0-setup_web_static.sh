#!/usr/bin/env bash
# write a bash script that sets up the env of you dep of web_statc
# it must include the next:

sudo apt-get update
sudo apt-get install -y nginx


sudo cp fake.html /data/web_static/releases/test/index.html
# creating a symbolic link , delete
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo service nginx restart


sudo cp hbnb_.text /etc/nginx/sites-available/default
