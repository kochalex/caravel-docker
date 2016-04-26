#---------------------------------------------------------
# Caravel specifix config
#---------------------------------------------------------
import os

ROW_LIMIT = os.getenv('ROW_LIMIT',5000)

WEBSERVER_THREADS = os.getenv('WEBSERVER_THREADS',8)

CARAVEL_WEBSERVER_PORT = os.getenv('CARAVEL_WEBSERVER_PORT',8088)
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.getenv('APP_SECRET_KEY','\2\1thisismyscretkey\1\2\e\y\y\h')

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# caravel metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
#SQLALCHEMY_DATABASE_URI = 'mysql://'+os.getenv('MYSQL_USERNAME')+':'+os.getenv('MYSQL_PASSWORD')+'@'+os.getenv('MYSQL_PORT_3306_TCP_ADDR')+'/'+os.getenv('MYSQL_INSTANCE_NAME')

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (
        os.getenv('POSTGRESQL_USERNAME') or os.getenv('POSTGRESQL_ENV_POSTGRES_USER','caravel'),
        os.getenv('POSTGRESQL_PASSWORD') or os.getenv('POSTGRESQL_ENV_POSTGRES_PASSWORD','caravel'),
        os.getenv('POSTGRESQL_PORT_5432_TCP_ADDR'),
        os.getenv('POSTGRESQL_PORT_5432_TCP_PORT','5432'),
        os.getenv('POSTGRESQL_INSTANCE_NAME') or os.getenv('POSTGRESQL_ENV_POSTGRES_DB','caravel')
    )

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

#debug
DEBUG = False
