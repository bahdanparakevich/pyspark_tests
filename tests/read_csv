from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.option("delimiter", ",") \
    .option("quote", "\"") \
    .option("multiLine", True) \
    .option("escape", "\"") \
    .csv("raw_data/DataEngineer.csv", header=True, inferSchema=True)

df.show()
