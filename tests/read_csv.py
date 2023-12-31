from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.option("delimiter", ",") \
    .option("quote", "\"") \
    .option("multiLine", True) \
    .option("escape", "\"") \
    .csv("D:/deproject/pyspark_tests/raw_data/DataEngineer.csv",  # change the file path to your own
         header=True, inferSchema=True)

df.show()
