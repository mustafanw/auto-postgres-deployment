import os
import psycopg2
import configparser
import json
from datetime import datetime

# ROOT = os.path.dirname(os.path.realpath(__file__))

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'ecommerce'

ROOT = os.path.dirname(os.path.realpath(__file__))

CONFIG_FILE = os.path.join(ROOT, "config.ini")

CONFIG = configparser.ConfigParser()

CONFIG.read(CONFIG_FILE)


def doQuery_delta() :
    logs=''
    for service in services:
        sprint_delta_path = ROOT+'/'+service+'/sprint_delta.sql'
        sprint_delta_data,fail_queries=execute_query(sprint_delta_path)
        service_delta_path = ROOT+'/'+service+'/service_delta.sql'
        version = CONFIG.get("EXECUTE_SCRIPTS",service)
        with open(service_delta_path, 'r') as original: old_data = original.read()
        with open(service_delta_path, 'w') as modified: modified.write("---Service Version "+version+"\n"+sprint_delta_data+"\n-----\n" + old_data)
        logs = logs + "Successfully Executed delta for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
        # with open(sprint_delta_path, 'w') as original: original.truncate(0)
    # CONFIG.set("EXECUTE_SCRIPTS","services","")
    with open(CONFIG_FILE, 'w') as original: CONFIG.write(original)
    with open(ROOT+'/DB_Script_Logs.txt', 'r') as original: data = original.read()
    with open(ROOT+'/DB_Script_Logs.txt', 'w') as modified: modified.write(logs+"\n-----\n" + data)

    with open(ROOT+'/failure_queries.txt', 'w') as modified: modified.write(fail_queries)

def execute_query(path):
    fail_queries=''
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    cur = conn.cursor()
    file = open(path,'r')
    data = file.read()
    query_data = data.replace("\n","")
    queries = query_data.split(";")
    for query in queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            fail_queries = fail_queries + str(e)+"\n"
            conn.rollback()
            continue
    conn.close()
    return data, fail_queries

def doQuery_base() :
    logs=''
    for service in services:
        ddl_path = ROOT+'/'+service+'/DDL.sql'
        dml_path = ROOT+'/'+service+'/DML.sql'
        data, fail_queries_ddl=execute_query(ddl_path)
        data, fail_queries_dml=execute_query(dml_path)
        fail_queries = fail_queries_ddl+fail_queries_dml
        version = CONFIG.get("EXECUTE_SCRIPTS",service)
        logs = logs + "Successfully Executed base script for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
        # with open(sprint_delta_path, 'w') as original: original.truncate(0)
    # CONFIG.set("EXECUTE_SCRIPTS","services","")
    with open(CONFIG_FILE, 'w') as original: CONFIG.write(original)
    with open(ROOT+'/DB_Script_Logs.txt', 'r') as original: data = original.read()
    with open(ROOT+'/DB_Script_Logs.txt', 'w') as modified: modified.write(logs+"\n-----\n" + data)

    with open(ROOT+'/failure_queries.txt', 'w') as modified: modified.write(fail_queries)

services = CONFIG.get("EXECUTE_SCRIPTS","services").split(',')
script_type = CONFIG.get("EXECUTE_SCRIPTS","type")
if script_type =='delta':
    doQuery_delta()
else:
    doQuery_base()

print("Success")