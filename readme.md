# raspi-mc-server

- [raspi-mc-server](#raspi-mc-server)
  - [Project Description](#project-description)
  - [how to setup](#how-to-setup)
    - [Prepare your Raspi](#prepare-your-raspi)
    - [Preparing the code on your Pi](#preparing-the-code-on-your-pi)
    - [Handling the server](#handling-the-server)
      - [Starting and Stopping the server](#starting-and-stopping-the-server)
      - [Change amount of RAM](#change-amount-of-ram)
    - [Making the server availible for the whole internet](#making-the-server-availible-for-the-whole-internet)

## Project Description

An auto-updating Minecraft server (eg. for Raspberry Pi)
The code of the updater is from this repo: [eclair4151/MinecraftUpdater](https://github.com/eclair4151/MinecraftUpdater)

## how to setup

This is a small tutorial for setting up a Minecraft server on a Raspberry Pi with the code from this repository.

### Prepare your Raspi

Note that if your intend is to use the server, I recommend using a Raspberry Pi 4 with at least 2GB of RAM or better.

1. Install Raspberry Pi OS (previously called raspbian), you can use the [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/) for that.

2. Activate SSH on your Raspi

   - [From Terminal](https://linuxize.com/post/how-to-enable-ssh-on-raspberry-pi/#enabling-ssh-from-the-terminal)
   - [With GUI](https://linuxize.com/post/how-to-enable-ssh-on-raspberry-pi/#enabling-ssh-from-gui)
   - [Without a Display](https://linuxize.com/post/how-to-enable-ssh-on-raspberry-pi/#enabling-ssh-on-raspberry-pi-without-a-screen)

3. Setup a static IP-address for your Raspi. I recommend just doing so on the configuration page of your router, since it's very simple to do so. However, you can try doing it on the Pi. Look [here](https://pimylifeup.com/raspberry-pi-static-ip-address/) for example.

4. Connect to your Pi via SSH (recommended) or have a keyboard and display connected to your Pi

5. Install java on your Pi: `sudo apt install default-jdk`

6. Install screen on your Pi: `apt-get install screen`

### Preparing the code on your Pi

1. Get the code from this repository to your Pi. For example, you could paste it here: `/home/pi/minecraft-server` You can use SSH for that. If you're a fan of VS Code, I recommend using the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). It allows you to work on your pi as you would on your local computer - via SSH

2. Copy the .service and .timer files to /etc/systemd/system/ with `sudo cp auto_updater/*.{service,timer} /etc/systemd/system/` You have to be in the `minecraft-server` directory to run that command.

3. Restart your Pi: `sudo reboot`

4. Verify that everything is working: In the [syslog](var/log/syslog), you should find some outputs from the auto-updater. `sudo tail -f /var/log/syslog` You can open the full file, if there were too many new lines. Also, you can use the `top` command to verify that java is running.

5. You can connect to the server in Minecraft using the static IP address of your Pi. You can access the server logs / server console with `screen -r minecraft` while connected to your Pi via SSH

6. (optional) If you want to quickly access your server console in the future, I recommend using a Profile in [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal-preview/9n8g5rfz9xk3). To do so, in Windows Terminal open settings and paste this profile under the existing ones:

```json
{
    "guid": "{3ddeae53-7f92-4457-a6ca-c9eaa6e237b2}",
    "name": "SSH Raspi MC",
    "commandline": "ssh -t pi@123.456.7.890 \"screen -r minecraft \"",
    "hidden": false
}
```

Don't forget to change the IP address to the one of you Pi.

### Handling the server

#### Starting and Stopping the server

- The server starts automatically when your Pi is starting
- You can manually start and stop the server using `sh _start-server.sh` and `sh _stop-server.sh` while you are in your `minecraft-server` directory

#### Change amount of RAM

- You can do so in the [java-starter.sh](java-starter.sh) file
- Note that Raspberry Pi OS is typically a 32-bit system. In my experience, you should not allow more RAM than 2500M
- `-Xms1G` defines that the server should start with 1GB of RAM
- `-Xmx2500M` defines that the server should use ~2.5GB of RAM at max

### Making the server availible for the whole internet

- At the moment, you can only connect to your server while you are in the same network as your Pi. Your friends can't join from their homes. Let's change that!
- This will be amended shortly
