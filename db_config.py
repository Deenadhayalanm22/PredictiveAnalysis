from app import app
from flaskext.mysql import MySQL
from sqlalchemy import create_engine

mysql = MySQL()
 
# MySQL configurations - Direct configuration
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'system'
app.config['MYSQL_DATABASE_DB'] = 'tez'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# MySQL configurations - Pandas configuraion
db_connection_str = 'mysql+pymysql://root:system@localhost/tez'
db_connection = create_engine(db_connection_str)
