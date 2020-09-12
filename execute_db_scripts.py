import os
import psycopg2
import configparser
import json
from datetime import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'ecommerce'

SERVICE_ROOT = os.path.dirname(os.path.realpath(__file__))

CONFIG_FILE = os.path.join(SERVICE_ROOT, "config.ini")

CONFIG = configparser.ConfigParser()

CONFIG.read(CONFIG_FILE)


def doQuery( conn ) :
    notes=''
    for service in services:
        cur = conn.cursor()
        sprint_delta_path = dir_path+'/'+service+'/sprint_delta.sql'
        sprint_delta_file = open(sprint_delta_path,'r')
        data = sprint_delta_file.read()
        # cur.execute(data)
        # conn.commit()

        service_delta_path = dir_path+'/'+service+'/service_delta.sql'
        f = open(service_delta_path, "a")
        f.write(data)
        f.write("\n--------------------------------\n\n")
        f.close()
        version = CONFIG.get("EXECUTE_DELTA",service)
        notes = notes + "Successfully Executed delta for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
        sprint_delta_file = open(sprint_delta_path,'w')
        sprint_delta_file.truncate(0)
        sprint_delta_file.close()
    CONFIG.set("EXECUTE_DELTA","services","")
    configfile = open(CONFIG_FILE, 'w')
    CONFIG.write(configfile)
    configfile.close()
    f = open(dir_path+'/Release_Notes.txt', "a")
    f.write(notes)
    f.write("--------------------------------\n\n")
    f.close()

# services = CONFIG['CONFIGS']['SERVICES'].split(',')
services = CONFIG.get("EXECUTE_DELTA","services").split(',')
print(services)
print(type(services))
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()