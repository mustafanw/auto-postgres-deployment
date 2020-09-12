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
        cur.execute(data)
        conn.commit()
        service_delta_path = dir_path+'/'+service+'/service_delta.sql'
        version = CONFIG.get("EXECUTE_DELTA",service)
        with open(service_delta_path, 'r') as original: old_data = original.read()
        with open(service_delta_path, 'w') as modified: modified.write("---Service Version "+version+"\n"+data+"\n-----\n" + old_data)


        notes = notes + "Successfully Executed delta for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
        # sprint_delta_file = open(sprint_delta_path,'w')
        # sprint_delta_file.truncate(0)
        # sprint_delta_file.close()
    # CONFIG.set("EXECUTE_DELTA","services","")
    # configfile = open(CONFIG_FILE, 'w')
    # CONFIG.write(configfile)
    # configfile.close()

    with open(dir_path+'/Release_Notes.txt', 'r') as original: data = original.read()
    with open(dir_path+'/Release_Notes.txt', 'w') as modified: modified.write(notes+"\n-----\n" + data)

services = CONFIG.get("EXECUTE_DELTA","services").split(',')
print(services)
print(type(services))
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()