#!/usr/bin/python

from subprocess import PIPE,Popen



def dump_db(host, dbname, user, password, **kwargs):
        command = f'pg_dump --host={host} ' \
            f'--dbname={dbname} ' \
            f'--username={user} ' \
            f'--no-password ' \
            f'--schema-only --format=p >> /tmp/schema1.sql'

        proc = Popen(command, shell=True, env={
            'PGPASSWORD': password
        })
        proc.wait()

def dump_table(host, dbname, user, password, table):
        # command = f'pg_dump --host={host} ' \
        #     f'--dbname={dbname} ' \
        #     f'--username={user} ' \
        #     f'--no-password ' \
        #     f'--data-only --column-inserts -t {table} --format=p >> /tmp/schema2.sql'
        
        command = f'pg_dump -d dvdrental -a -t {table} --data-only --column-inserts -U aiops | grep -i INSERT -m 5 >> /tmp/schema2.sql'

        proc = Popen(command, shell=True, env={
            'PGPASSWORD': password
        })
        proc.wait()

def restore_schema(host, dbname, user, password, **kwargs):
        command = f'psql --host={host} ' \
            f'--dbname={dbname} ' \
            f'--username={user} ' \
            f'--no-password < /tmp/schema1.sql'

        proc = Popen(command, shell=True, env={
            'PGPASSWORD': password
        })
        proc.wait()

def main():
    # dump_db('localhost','dvdrental','aiops','aiops')
    dump_table('localhost','dvdrental','aiops','aiops', 'public.category')
    dump_table('localhost','dvdrental','aiops','aiops','test_1.actor')
    # restore_schema('localhost','aiops','aiops','aiops')

if __name__ == "__main__":
    main()

#pg_dump -d dvdrental -a -t category --data-only --column-inserts -U aiops | grep -i INSERT -m 1000