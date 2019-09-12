import pymysql
import pickle
import pandas.io.sql as pd
from pandas import DataFrame
from app import app
from flask import request, jsonify, render_template
from db_config import mysql
from db_config import db_connection


app.config["DEBUG"]=True


@app.route('/', methods=['GET'])
def home():
    return "<h2>Hello!!</h2>"

@app.route('/data', methods=['GET'])
def show_data():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM POPULATION")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/index')
def load_data():
		df=pd.read_sql("SELECT * FROM POPULATION", con=db_connection)
		return render_template('index.html', result = df)

if __name__ == "__main__":
    app.run()