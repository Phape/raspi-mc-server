import os, getpass, time, logging, logging.handlers

# print("Current User:", getpass.getuser())
logging.basicConfig(level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())

process_name= "java"

while True:
    tmp = os.popen("ps -Af").read()

    if process_name not in tmp[:]:
        try:
            logging.info("(Re)Starting Server with JVM Arguments from server-runner.py")
            os.system('screen -S minecraft -d -m java -Xms1G -Xmx2500M -jar minecraft_server.jar nogui')
        except:
            logging.info("Failed to start the Minecraft Server")
    
    time.sleep(30)


