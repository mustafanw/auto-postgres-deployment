import os
import psycopg2
import configparser
import json
from datetime import datetime


hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'ecommerce'

ROOT = os.path.dirname(os.path.realpath(__file__))

CONFIG_FILE = os.path.join(ROOT, "config.ini")

CONFIG = configparser.ConfigParser()

CONFIG.read(CONFIG_FILE)

def execute_query(path):
    failed_queries=''
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    cur = conn.cursor()
    file = open(path,'r')
    data = file.read()
    query_data = data.replace("\n","")
    queries = query_data.split(";")
    queries.pop()
    import pdb;pdb.set_trace()
    for query in queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            failed_queries = failed_queries + str(e)+"\n"
            conn.rollback()
            continue
    conn.close()
    return data, failed_queries

def add_logs(new_logs, fail_queries):
    with open(ROOT+'/DB_Script_Logs.txt', 'r') as original: old_logs = original.read()
    with open(ROOT+'/DB_Script_Logs.txt', 'w') as modified: modified.write(new_logs+"\n-----\n" + old_logs)
    with open(ROOT+'/failure_queries.txt', 'w') as modified: modified.write(fail_queries)

def run_base_script() :
    logs=''
    for service in services:
        ddl_path = ROOT+'/'+service+'/DDL.sql'
        dml_path = ROOT+'/'+service+'/DML.sql'
        data, fail_queries_ddl=execute_query(ddl_path)
        data, fail_queries_dml=execute_query(dml_path)
        failed_queries = fail_queries_ddl+fail_queries_dml
        version = CONFIG.get("EXECUTE_SCRIPTS",service)
        logs = logs + "Successfully Executed base script for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
        # with open(sprint_delta_path, 'w') as original: original.truncate(0)
    # CONFIG.set("EXECUTE_SCRIPTS","services","")
    with open(CONFIG_FILE, 'w') as original: CONFIG.write(original)
    add_logs(logs, failed_queries)
    return "Success"

def run_delta_script() :
    logs=''
    for service in services:
        sprint_delta_path = ROOT+'/'+service+'/sprint_delta.sql'
        sprint_delta_data,failed_queries=execute_query(sprint_delta_path)
        service_delta_path = ROOT+'/'+service+'/service_delta.sql'
        version = CONFIG.get("EXECUTE_SCRIPTS",service)
        with open(service_delta_path, 'r') as original: old_data = original.read()
        with open(service_delta_path, 'w') as modified: modified.write("---Service Version "+version+"\n"+sprint_delta_data+"\n-----\n" + old_data)
        logs = logs + "Successfully Executed delta for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
    #     with open(sprint_delta_path, 'w') as original: original.truncate(0)
    # CONFIG.set("EXECUTE_SCRIPTS","services","")
    with open(CONFIG_FILE, 'w') as original: CONFIG.write(original)
    add_logs(logs, failed_queries)
    return "Success"


services = CONFIG.get("EXECUTE_SCRIPTS","services").split(',')
script_type = CONFIG.get("EXECUTE_SCRIPTS","type")
run_script = run_delta_script() if script_type =='delta' else run_base_script()
print(run_script)