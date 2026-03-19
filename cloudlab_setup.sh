#!/bin/bash

sudo apt install openjdk-17-jdk
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH

sudo groupadd docker
sudo usermod -aG docker ${USER}
sudo chown root:docker /var/run/docker.sock

sudo apt install npm

# after deploy
wsk -i property set --apihost 10.0.1.2
wsk -i property set --auth `cat ansible/files/auth.guest`