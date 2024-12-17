from sqlalchemy import create_engine
import polars as pl

engine_connection = create_engine("postgresql+psycopg2://postgres:p0s_gr3s@172.17.0.1:5431/ldf")

df = pl.read_database(
    query="SELECT * FROM profile",
    connection=engine_connection
)

print(df)