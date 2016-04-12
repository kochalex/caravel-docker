#!/usr/local/bin/python
import os
import MySQLdb

conn = MySQLdb.connect(host=os.getenv('MYSQL_PORT_3306_TCP_ADDR'),user=os.getenv('MYSQL_USERNAME'),passwd=os.getenv('MYSQL_PASSWORD'),db=os.getenv('MYSQL_INSTANCE_NAME'),port=int(os.getenv('MYSQL_PORT_3306_TCP_PORT')))

cur = conn.cursor()

res = cur.execute('show tables')

if(res == 0):
  print 1
else:
  print 0

cur.close()

conn.close()
