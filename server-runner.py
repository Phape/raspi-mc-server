import os, getpass, time

# print("Current User:", getpass.getuser())
process_name= "java"

while True:
    tmp = os.popen("ps -Af").read()

    if process_name not in tmp[:]:
        print("(Re)Starting Server with JVM Arguments from server-runner.py")
        os.system('screen -S minecraft -d -m java -Xms1G -Xmx2500M -jar minecraft_server.jar nogui')

    time.sleep(10)


