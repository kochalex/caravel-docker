#!/usr/local/bin/python
import os
import psycopg2

conn = psycopg2.connect(databaseb=os.getenv('POSTGRESQL_ENV_POSTGRES_DB'),user=os.getenv('POSTGRESQL_ENV_POSTGRES_USER'),password=os.getenv('POSTGRESQL_ENV_POSTGRES_PASSWORD'),host=os.getenv('POSTGRESQL_PORT_5432_TCP_ADDR'),port=int(os.getenv('POSTGRESQL_PORT_5432_TCP_PORT')))

cur = conn.cursor()

cur.execute('select count(*) form ab_user')

res = cur.fetchall()

if(res != '' ):
  print 1
else:
  print 0

cur.close()

conn.close()
