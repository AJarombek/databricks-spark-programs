# Databricks notebook source
# MAGIC %md
# MAGIC # Data Workflow Transform Stage

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM zwift_raw_data

# COMMAND ----------

df = spark.table("zwift_raw_data")
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Compute the Number of Days Spent at Each Level

# COMMAND ----------

import pyspark.sql.functions as F

grouped_df = (
    df
    .groupBy(F.col("date"))
    .agg(F.max("level").alias("max_level"))
    .orderBy(F.col("max_level").desc())
)
    
grouped_df.display()

# COMMAND ----------

result_df = (
    grouped_df
    .groupBy(F.col("max_level"))
    .count()
    .withColumnRenamed("max_level", "level")
    .withColumnRenamed("count", "days")
    .orderBy(F.col("level").asc())
)

result_df.display()

# COMMAND ----------

result_df.write.mode("overwrite").saveAsTable("zwift_level_duration")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM zwift_level_duration;
