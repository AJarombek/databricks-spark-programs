# Databricks notebook source
# MAGIC %md
# MAGIC # Data Source Formats

# COMMAND ----------

# MAGIC %md
# MAGIC * Read from a CSV

# COMMAND ----------

activities_df = spark.read.format("csv").option("header", "true").load("/src/strava_activities.csv")
activities_df.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE data_source_formats_demo

# COMMAND ----------

# MAGIC %sql
# MAGIC USE data_source_formats_demo

# COMMAND ----------

import pyspark.sql.functions as F

strava_activity_stats_df = (
    activities_df
    .select(["Activity Date", "Activity Name", "Activity Type", "Elapsed Time5", "Distance6"])
    .withColumn("Activity Date", F.to_timestamp(F.col("Activity Date"), "MMM d, yyyy, h:mm:ss a"))
    .withColumn("Elapsed Time5", F.col("Elapsed Time5").cast("int"))
    .withColumn("Distance6", F.col("Distance6").cast("float"))
    .withColumnRenamed("Activity Date", "date")
    .withColumnRenamed("Activity Name", "name")
    .withColumnRenamed("Activity Type", "type")
    .withColumnRenamed("Elapsed Time5", "time_seconds")
    .withColumnRenamed("Distance6", "miles")
)

strava_activity_stats_df.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE strava_activity_stats (
# MAGIC   date TIMESTAMP,
# MAGIC   name STRING,
# MAGIC   type STRING,
# MAGIC   time_seconds INT,
# MAGIC   miles FLOAT
# MAGIC )

# COMMAND ----------

strava_activity_stats_df.write.mode("overwrite").saveAsTable("strava_activity_stats")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM strava_activity_stats

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL strava_activity_stats

# COMMAND ----------

# MAGIC %md
# MAGIC * Write to Parquet Files

# COMMAND ----------

(
    strava_activity_stats_df.write
    .format("parquet")
    .mode("overwrite")
    .option("compression", "snappy")
    .save("/parquet/strava_activity_stats")
)

# COMMAND ----------

dbutils.fs.ls("/parquet/strava_activity_stats")

# COMMAND ----------

# MAGIC %md
# MAGIC * Write to Avro Files

# COMMAND ----------

(
    strava_activity_stats_df.write
    .format("avro")
    .mode("overwrite")
    .save("/avro/strava_activity_stats")
)

# COMMAND ----------

dbutils.fs.ls("/avro/strava_activity_stats")
