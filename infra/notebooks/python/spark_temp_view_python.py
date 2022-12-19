# Databricks notebook source
from datetime import datetime

import pyspark.sql.types as T

schema = T.StructType(
    [
        T.StructField("name", T.StringType(), False),
        T.StructField("miles", T.DoubleType(), False),
        T.StructField("map", T.StringType(), False),
        T.StructField("routes", T.ArrayType(T.StringType()), False),
        T.StructField("date", T.DateType(), False),
        T.StructField("level", T.IntegerType(), False),
    ]
)

data = (
    ("Legends and Lava in Watopia", 15.64, "Watopia", ["Legends and Lava"], datetime(2022, 12, 13), 20),
    ("Greater London 8 in London", 15.64, "London", ["Greater London 8"], datetime(2022, 12, 7), 20),
    ("Classique in London", 3.78, "London", ["London Classique"], datetime(2022, 12, 7), 20),
    ("Sleepless City in Makuri Islands", 13.76, "Makuri Islands", ["Sleepless City"], datetime(2022, 12, 2), 20),
    ("Three Village Loop in Makuri Islands", 11.27, "Makuri Islands", ["Three Village Loop"], datetime(2022, 12, 1), 20),
)

zwift_df = spark.createDataFrame(data, schema)
zwift_df.display()

# COMMAND ----------

zwift_df.createOrReplaceTempView("zwift_rides")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM zwift_rides