from flask import *  # 必要なライブラリのインポート
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, func
from flaski.database import db_session
from flaski.models import GPSinfo
import os
import sqlite3
import datetime

app = Flask(__name__)  # アプリの設定


@app.route("/")  # どのページで実行する関数か設定
def main():

    contents = GPSinfo.query.all()

    return render_template("index.html", contents=contents)


#sigfoxから受信したデータをDBに格納する（x, y, time）
@app.route("/top", methods=["GET", "POST"])
def set_location():

    gps_data = []
    all_column = GPSinfo.query.all()

    if request.method == "POST":
        gps_data = []
        gps_data = request.json

        column_first = GPSinfo.query.first()

        gpsinfo = GPSinfo()
        gpsinfo.gps_x = float(gps_data["people_float"])
        gpsinfo.gps_y = float(gps_data["people_float"])
        gpsinfo.date = datetime.datetime.now()

        x = float(gps_data["people_float"])
        y = float(gps_data["people_float"])
  
        db_session.add(gpsinfo)
        db_session.commit()


    return render_template("top.html", info=gps_data, all_column=all_column)

@app.route("/getInfo", methods=["GET", "POST"])
def get_info():
    latest_column = GPSinfo.query.order_by(GPSinfo.date.desc()).first()
    return_info = {}

    if latest_column:

        return_info["gps_x"] = latest_column.gps_x
        return_info["gps_y"] = latest_column.gps_y
        return_info["date"] = latest_column.date


    return jsonify(**return_info)



if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行