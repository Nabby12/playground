from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StructField, StructType

spark = SparkSession.builder.appName("SparkApp").getOrCreate()

schema = StructType([StructField("A", IntegerType(), True), StructField("B", IntegerType(), True)])
# schema = ["A", "B"]  # simple way

data = [(1, 2), (3, 4), (5, 6)]

df = spark.createDataFrame(data, schema)
df.show()

filtered_df = df.filter(df.A > 1)
filtered_df.show()

spark.stop()
