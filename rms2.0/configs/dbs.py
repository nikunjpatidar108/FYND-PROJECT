from sqlalchemy import create_engine, MetaData
import pymysql

engine = create_engine("mysql+pymysql://root:41526374@localhost:3306/rms")
meta = MetaData()
conn = engine.connect()
