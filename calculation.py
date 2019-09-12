import pymysql
import pandas as pd
from app import app
from db_config import mysql

app.config["DEBUG"]=True


def load_data():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        df= pd.read_sql("SELECT * FROM POPULATION", cursor)

        print(df.describe())
    except Exception as e:
	    print(e)
    finally:
	    cursor.close() 
	    conn.close()

if __name__ == "__main__":
    app.run()