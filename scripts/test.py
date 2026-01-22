from snowflake.snowpark.session import Session

def get_session():
    return Session.builder.config("connection_name", "cienqlo").getOrCreate()

session = get_session()

print(session)
