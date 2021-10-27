from sqlalchemy import create_engine, MetaData
import pymysql

# engine = create_engine("mysql+pymysql://root:41526374@localhost:3306/rms")
engine = create_engine("mysql+pymysql://sql6446906:iP1UFFz35y@sql6.freemysqlhosting.net:3306/sql6446906")
meta = MetaData()
conn = engine.connect()

# meta.create_all(engine)