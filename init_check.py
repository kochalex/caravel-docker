#!/usr/local/bin/python
#coding=utf-8
# 检查是否已经安装过，如果安装过就不再初始化数据库
#
import os
import psycopg2

conn = psycopg2.connect(databaseb=os.getenv('POSTGRESQL_INSTANCE_NAME') or os.getenv('POSTGRESQL_ENV_POSTGRES_DB'),user=os.getenv('POSTGRESQL_USERNAME') or os.getenv('POSTGRESQL_ENV_POSTGRES_USER'),password=os.getenv('POSTGRESQL_PASSWORD') or os.getenv('POSTGRESQL_ENV_POSTGRES_PASSWORD'),host=os.getenv('POSTGRESQL_PORT_5432_TCP_ADDR'),port=int(os.getenv('POSTGRESQL_PORT_5432_TCP_PORT')))

cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

res = cur.fetchall()

if(res == [] ):
  print 1
else:
  print 0

cur.close()

conn.close()
