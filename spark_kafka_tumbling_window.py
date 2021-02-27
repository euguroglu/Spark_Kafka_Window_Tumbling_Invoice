from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import from_json, col, to_timestamp, window, expr, sum
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Tumbling Window Steram")
        .master("local[3]")
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.sql.shuffle.partitions", 2) \
        .getOrCreate()


    stock_schema = StructType([
        StructField("CreatedTime", StringType()),
        StructField("Type", StringType()),
        StructField("Amount", IntegerType()),
        StructField("BrokerCode", StringType())
    ])
