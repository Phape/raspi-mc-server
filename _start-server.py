"""
run this command to start the server: python3 _start-server.py
note that the server starts automatically when the raspberryPi / host starts

this script starts the check for minecraft updates in regular time intervals as well
to check whether the server is running use one of the following two commands:
top       --> java process should be listed
service minecraft-server status
"""
import os

os.system('service minecraft-server start')
