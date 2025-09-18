from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import rand, when
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

spark = SparkSession.builder.appName("SparkApp").getOrCreate()

schema = StructType([StructField("Primary", StringType(), True)])
data = [("A",), ("B",), ("C",)]

df = spark.createDataFrame(data, schema)


def random_null_or_int():
    return when(rand() < 0.7, None).otherwise((rand() * 100).cast(IntegerType()))
    # return when(rand() < 1, None).otherwise((rand() * 100).cast(IntegerType()))  # always null for test


df = df.withColumn("Random1", random_null_or_int())
df = df.withColumn("Random2", random_null_or_int())
df = df.withColumn("Random3", random_null_or_int())
df = df.withColumn("Random4", random_null_or_int())
df = df.withColumn("Random5", random_null_or_int())

KEYS = ["Primary", "Random1", "Random2", "Random3", "Random4", "Random5"]
df = df.select(
    *KEYS,
    F.least(
        F.col("Random1"),
        F.col("Random2"),
        F.col("Random3"),
        F.col("Random4"),
        F.col("Random5"),
    ).alias("Result")
)

df.show()

spark.stop()
