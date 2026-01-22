# Imports remain the same
import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, udf
from snowflake.snowpark.types import StringType
from snowflake.snowpark.session import Session

# Function definition (main)
def main(session: snowpark.Session):
    # All the following code is now correctly indented inside the 'main' function.

    # Define a TEMPORARY UDF for capitalizing a string.
    # Notice is_permanent and stage_location are removed. No stage needed!
    @udf(name="capitalize_first_temp", return_type=StringType(), replace=True)
    def capitalize_first(s: str) -> str:
        return s.capitalize()

    # Create a DataFrame with a sample string
    df = session.create_dataframe([["snowflake"]]).to_df("example_column")
    df.show()
    # Apply the UDF to the DataFrame
    df_with_udf = df.select(capitalize_first(col("example_column")).alias("capitalize"))

    # Display result
    df_with_udf.show()

    return df_with_udf

if __name__ == '__main__':
    session = Session.builder.config("connection_name", "cienqlo").getOrCreate()
    main(session)
