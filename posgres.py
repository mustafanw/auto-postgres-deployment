hostname = '10.0.1.168'
username = 'postgres'
password = 'postgres'
database = 'aiops'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    # cur.execute( "CREATE TABLE public.mustafa(action_trigger character varying)" )
    sql_file = open('postgres_auto.sql','r')
    cur.execute(sql_file.read())
    conn.commit()



import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()