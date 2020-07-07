import os
import getpass

print("Starting Server with JVM Arguments from java-starter.sh")
print("Current User:", getpass.getuser())
os.system('screen -S minecraft -d -m java -Xms1G -Xmx2500M -jar minecraft_server.jar nogui')