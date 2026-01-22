from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import col
import sys

session = Session.builder.config("connection_name", "cienqlo").getOrCreate()

print(f"current interpreter: {sys.executable}")

df = session.table("SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CATALOG_SALES").limit(100)

df.show()
