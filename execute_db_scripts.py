import os
import psycopg2
import configparser
import json
from datetime import datetime

ROOT = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = os.path.join(ROOT, "config.ini")
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)

hostname = CONFIG.get("DATABASE_CONFIGS","hostname")
username = CONFIG.get("DATABASE_CONFIGS","username")
password = CONFIG.get("DATABASE_CONFIGS","password")
database = CONFIG.get("DATABASE_CONFIGS","database")

def execute_query(path, service, version):
    failed_queries=''
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    cur = conn.cursor()
    file = open(path,'r')
    data = file.read()
    if data:
        query_data = data.replace("\n","")
        queries = query_data.split(";")
        queries.pop()
        for query in queries:
            try:
                cur.execute(query)
                conn.commit()
            except Exception as e:
                failed_queries = failed_queries + str(e)+"\n"
                conn.rollback()
                continue
        conn.close()
        if failed_queries:
            failed_queries = "---Failed Queries in service {0} version {1}\n {2}".format(service, version, failed_queries)
    return data, failed_queries

def add_logs(new_logs, new_failed_queries):
    with open(ROOT+'/DB_Script_Logs.txt', 'r') as original: old_logs = original.read()
    with open(ROOT+'/DB_Script_Logs.txt', 'w') as modified: modified.write(new_logs+"\n-----\n" + old_logs)
    if new_failed_queries:
        with open(ROOT+'/Failed_Queries.txt', 'r') as original: old_failed_queries = original.read()
        with open(ROOT+'/Failed_Queries.txt', 'w') as modified: modified.write(new_failed_queries+"\n-----\n" + old_failed_queries)

def run_base_script() :
    try:
        logs=''
        error_flag = 0
        for service in services:
            try:
                version = CONFIG.get("EXECUTE_SCRIPTS",service)
                ddl_path = ROOT+'/'+service+'/DDL.sql'
                dml_path = ROOT+'/'+service+'/DML.sql'
                data, fail_queries_ddl=execute_query(ddl_path,service, version)
                data, fail_queries_dml=execute_query(dml_path,service, version)
                failed_queries = fail_queries_ddl+fail_queries_dml

                logs = logs + "Successfully Executed base script for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
                with open(sprint_delta_path, 'w') as original: original.truncate(0)
            except:
                logs = logs + "Error while Executed base script for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
                error_flag = 1
                continue
        # CONFIG.set("EXECUTE_SCRIPTS","services","")
        with open(CONFIG_FILE, 'w') as original: CONFIG.write(original)
        add_logs(logs, failed_queries)
        response = "Successfully executed base scripts" if error_flag==1 else "Partially executed base scripts"
    except:
        response = "Error while executing base scripts"
    return response

def run_delta_script() :
    try:
        logs=''
        error_flag = 0
        for service in services:
            try:
                version = CONFIG.get("EXECUTE_SCRIPTS",service)
                sprint_delta_path = ROOT+'/'+service+'/sprint_delta.sql'
                sprint_delta_data,failed_queries=execute_query(sprint_delta_path,service, version)
                service_delta_path = ROOT+'/'+service+'/service_delta.sql'
                with open(service_delta_path, 'r') as original: old_data = original.read()
                with open(service_delta_path, 'w') as modified: modified.write("---Service Version "+version+"\n"+sprint_delta_data+"\n-----\n" + old_data)
                logs = logs + "Successfully Executed delta for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
                with open(sprint_delta_path, 'w') as original: original.truncate(0)
            except:
                logs = logs + "Error while Executed delta for " + service + " version " + version+ " at " + str(datetime.now())+"\n"
                error_flag = 1
                continue
        # CONFIG.set("EXECUTE_SCRIPTS","services","")
        with open(CONFIG_FILE, 'w') as original: CONFIG.write(original)
        add_logs(logs, failed_queries)
        response = "Successfully executed delta scripts" if error_flag==1 else "Partially executed delta scripts"
    except:
        response = "Error while executing delta scripts"
    return response

services = CONFIG.get("EXECUTE_SCRIPTS","services").split(',')
script_type = CONFIG.get("EXECUTE_SCRIPTS","type")
run_script = run_delta_script() if script_type =='delta' else run_base_script()
print(run_script)