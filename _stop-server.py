"""
run this command to start the server: python3 _stop-server.py
note that the server stops automatically when the raspberryPi / host stops

this script stops the check for minecraft updates in regular time intervals as well
"""
import os

os.system('service minecraft-server stop')
