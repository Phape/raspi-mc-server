#!/bin/bash
echo "Starting Server with JVM Arguments from java-starter.sh"
echo "User: $USER"
screen -S minecraft -d -m java -Xms1G -Xmx2500M -jar minecraft_server.jar nogui