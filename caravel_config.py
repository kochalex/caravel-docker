#---------------------------------------------------------
# Caravel specifix config
#---------------------------------------------------------
import os

ROW_LIMIT = 5000

WEBSERVER_THREADS = 8

CARAVEL_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.getenv('APP_SECRET_KEY','1234546774')

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# caravel metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
#SQLALCHEMY_DATABASE_URI = 'mysql://'+os.getenv('MYSQL_USERNAME')+':'+os.getenv('MYSQL_PASSWORD')+'@'+os.getenv('MYSQL_PORT_3306_TCP_ADDR')+'/'+os.getenv('MYSQL_INSTANCE_NAME')

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (
        os.getenv('MYSQL_USERNAME', 'root'),
        os.getenv('MYSQL_PASSWORD', '1234'),
        os.getenv('MYSQL_PORT_3306_TCP_ADDR', '10.211.55.2'),
        os.getenv('MYSQL_INSTANCE_NAME', 'caravel'),
    )

# Flask-WTF flag for CSRF
CSRF_ENABLED = True
