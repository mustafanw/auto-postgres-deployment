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


def doQuery_delta( conn ) :
    logs=''
    fail_queries=''
    for service in services:
        cur = conn.cursor()
        sprint_delta_path = ROOT+'/'+service+'/sprint_delta.sql'
        import pdb;pdb.set_trace()
        sprint_delta_file = open(sprint_delta_path,'r')

        data = sprint_delta_file.read()
        data = data.replace("\n","")
        new_data = data.split(";")
        queries = [query+";" for query in new_data]
        for query in queries:
            try:
                cur.execute(query)
                conn.commit()
            except Exception as e:
                fail_queries = fail_queries + str(e)+"\n"
                conn.rollback()
                continue
        service_delta_path = ROOT+'/'+service+'/service_delta.sql'
        version = CONFIG.get("EXECUTE_SCRIPTS",service)
        with open(service_delta_path, 'r') as original: old_data = original.read()
        with open(service_delta_path, 'w') as modified: modified.write("---Service Version "+version+"\n"+data+"\n-----\n" + old_data)
        logs = logs + "Successfully Executed delta for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
        # with open(sprint_delta_path, 'w') as original: original.truncate(0)
    # CONFIG.set("EXECUTE_SCRIPTS","services","")
    with open(CONFIG_FILE, 'w') as original: CONFIG.write(original)
    with open(ROOT+'/DB_Script_Logs.txt', 'r') as original: data = original.read()
    with open(ROOT+'/DB_Script_Logs.txt', 'w') as modified: modified.write(logs+"\n-----\n" + data)

    with open(ROOT+'/failure_queries.txt', 'w') as modified: modified.write(fail_queries)

def doQuery_base( conn ) :
    logs=''
    fail_queries=''
    for service in services:
        cur = conn.cursor()
        ddl_path = ROOT+'/'+service+'/DDL.sql'
        dml_path = ROOT+'/'+service+'/DML.sql'
        import pdb;pdb.set_trace()
        ddl_file = open(ddl_path,'r')
        dml_file = open(dml_path,'r')

        data_ddl = ddl_file.read()
        data_ddl = data_ddl.replace("\n","")
        new_data_ddl = data_ddl.split(";")
        queries_ddl = [query+";" for query in new_data_ddl]
        for query in queries_ddl:
            try:
                cur.execute(query)
                conn.commit()
            except Exception as e:
                fail_queries = fail_queries + str(e)+"\n"
                conn.rollback()
                continue
        data_dml = dml_file.read()
        data_dml = data_dml.replace("\n","")
        new_data_dml = data_dml.split(";")
        queries_dml = [query+";" for query in new_data_dml]
        for query in queries_dml:
            try:
                cur.execute(query)
                conn.commit()
            except Exception as e:
                fail_queries = fail_queries + str(e)+"\n"
                conn.rollback()
                continue
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
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
myConnection.autocommit = True
if script_type =='delta':
    doQuery_delta( myConnection )
else:
    doQuery_base( myConnection )
myConnection.close()
print("Success")