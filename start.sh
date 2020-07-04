#!/bin/bash
echo "Starting Server with JVM Arguments from start.sh"
echo "$USER"
screen -S minecraft -d -m java -Xms1G -Xmx2500M -jar minecraft_server.jar nogui
# tmux new -d -s minecraft

# while :
# do
#     sleep 1
# done
# java -Xmx2800M -Xms2G -jar minecraft_server.jar nogui
# su pi

# screen minecraft -d -m java -Xms2G -Xmx3G -jar minecraft_server.jar nogui
# screen -S minecraft -X stuff 'echo Minecraft Screen\n'


# screen alternative: https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session
# YT tutorial: https://www.youtube.com/watch?v=LrugHAcgLz4&t=722s