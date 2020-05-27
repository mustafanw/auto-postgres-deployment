# hostname = 'localhost'
# username = 'postgres'
# password = 'postgres'
# database = 'sprint30'

hostname = '34.194.174.76'
username = 'postgres'
password = 'postgres'
database = 'aiops'

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    # cur.execute( "CREATE TABLE public.mustafa(action_trigger character varying)" )
    version_file = open('devdb.version','r')
    version = version_file.read()
    print(version)
    print(dir_path)
    sql_path = dir_path+'/sprint33/postgres_'+version+'.sql'
    print(sql_path)
    sql_file = open(sql_path,'r')
    cur.execute(sql_file.read())
    conn.commit()



import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()