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
# MAGIC ## Create an Unmanaged Table

# COMMAND ----------

strava_run_df = strava_activities_df.filter(F.col("type") == 'Run')
strava_run_df.display()

# COMMAND ----------

(
    strava_run_df.write
    .option('path', 'dbfs:/user/hive/warehouse/tables_and_views_demo.db/strava_run')
    .saveAsTable("strava_run")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM strava_run

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL strava_run

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY strava_run

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Temporary View with SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW runs_2022 AS
# MAGIC SELECT * FROM strava_run WHERE date LIKE '2022%'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM runs_2022

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Temporary View with Python

# COMMAND ----------

runs_2021_df = spark.sql("SELECT * FROM strava_run WHERE date LIKE '2021%'")
runs_2021_df.createOrReplaceTempView("runs_2021")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM runs_2021

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Global Temporary View with SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE GLOBAL TEMP VIEW rides_2022 AS
# MAGIC SELECT * FROM strava_activities WHERE type = 'Ride' AND date LIKE '2022%'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM global_temp.rides_2022

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Global Temporary View with Python

# COMMAND ----------

rides_2021_df = spark.sql("SELECT * FROM strava_activities WHERE type = 'Ride' AND date LIKE '2021%'")
rides_2021_df.createOrReplaceGlobalTempView("rides_2021")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM global_temp.rides_2021

# COMMAND ----------

# MAGIC %md
# MAGIC ## Viewing Metadata

# COMMAND ----------

spark.catalog.listDatabases()

# COMMAND ----------

spark.catalog.listTables()

# COMMAND ----------

spark.catalog.listColumns("strava_activities")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Caching Tables

# COMMAND ----------

# MAGIC %sql
# MAGIC CACHE LAZY TABLE strava_activities

# COMMAND ----------

# MAGIC %sql
# MAGIC UNCACHE TABLE strava_activities
