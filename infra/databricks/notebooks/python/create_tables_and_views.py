# Databricks notebook source
# MAGIC %md
# MAGIC # Create Tables and Views

# COMMAND ----------

activities_df = spark.read.format("csv").option("header", "true").load("/src/strava_activities.csv")
activities_df.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE tables_and_views_demo

# COMMAND ----------

# MAGIC %sql
# MAGIC USE tables_and_views_demo

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Managed Table with SQL

# COMMAND ----------

import pyspark.sql.functions as F

strava_activities_df = (
    activities_df
    .select(["Activity ID", "Activity Date", "Activity Name", "Activity Type", "Activity Description"])
    .withColumn("Activity Date", F.to_timestamp(F.col("Activity Date"), "MMM d, yyyy, h:mm:ss a"))
    .withColumnRenamed("Activity ID", "id")
    .withColumnRenamed("Activity Date", "date")
    .withColumnRenamed("Activity Name", "name")
    .withColumnRenamed("Activity Type", "type")
    .withColumnRenamed("Activity Description", "description")
)

strava_activities_df.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE strava_activities (
# MAGIC   id STRING,
# MAGIC   date TIMESTAMP,
# MAGIC   name STRING,
# MAGIC   type STRING,
# MAGIC   description STRING
# MAGIC )

# COMMAND ----------

strava_activities_df.write.mode("append").saveAsTable("strava_activities")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM strava_activities

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL strava_activities

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY strava_activities

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Managed Table with Python

# COMMAND ----------

strava_ski_df = strava_activities_df.filter(F.col("type").like('%Ski%'))
strava_ski_df.display()

# COMMAND ----------

strava_ski_df.write.saveAsTable("strava_ski")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM strava_ski

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL strava_ski

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY strava_ski

# COMMAND ----------

# MAGIC %md
# MAGIC * Create an Unmanaged Table

# COMMAND ----------

# MAGIC %md
# MAGIC * Create a Temporary View

# COMMAND ----------

# MAGIC %md
# MAGIC * Create a Global Temporary View

# COMMAND ----------

# MAGIC %md
# MAGIC * Viewing Metadata

# COMMAND ----------

# MAGIC %md
# MAGIC * Caching Tables
