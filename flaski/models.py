# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from flaski.database import Base
from datetime import datetime


class GPSinfo(Base):
    __tablename__ = 'gpsinfos'                  # テーブル名
    # id = Column(Integer, primary_key=True, autoincrement=True)          # カラム１(id)
    gps_x = Column(Float)        # カラム２(title)
    gps_y = Column(Float)                             # カラム3(body)
    date = Column(DateTime, default=datetime.now(), primary_key=True)# カラム４(date) デフォルト現在日時を設定

    def __init__(self, gps_x=None, gps_y=None, date=None):
        self.gps_x = gps_x
        self.gps_y = gps_y
        self.date = date
