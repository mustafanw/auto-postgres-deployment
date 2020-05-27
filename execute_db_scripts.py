import os
import psycopg2

dir_path = os.path.dirname(os.path.realpath(__file__))

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'sprint30'

def doQuery( conn ) :
    cur = conn.cursor()

    version_file = open('devdb.version','r')
    version = version_file.read()
    sql_path = dir_path+'/sprint33/dev/postgres_dev_'+version+'.sql'
    sql_file = open(sql_path,'r')
    cur.execute(sql_file.read())
    conn.commit()


myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()