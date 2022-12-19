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
    ("Triple Loops in Watopia", 26.17, "London", ["Triple Loops"], datetime(2022, 12, 18), 21),
    ("Hilly Loop in Watopia", 12.51, "Watopia", ["Hilly Loop"], datetime(2022, 12, 17), 21),
    ("Beach Island Loop in Watopia", 12.51, "Watopia", ["Beach Island Loop"], datetime(2022, 12, 17), 21),
    ("Watopia's Waistband in Watopia", 21.20, "Watopia", ["Watopia's Waistband"], datetime(2022, 12, 16), 21),
    ("Four Horsemen in Watopia", 56.01, "Watopia", ["Four Horsemen"], datetime(2022, 12, 15), 21),
    ("Legends and Lava in Watopia", 15.64, "Watopia", ["Legends and Lava"], datetime(2022, 12, 13), 20),
    ("Greater London 8 in London", 15.64, "London", ["Greater London 8"], datetime(2022, 12, 7), 20),
    ("Classique in London", 3.78, "London", ["London Classique"], datetime(2022, 12, 7), 20),
    ("Sleepless City in Makuri Islands", 13.76, "Makuri Islands", ["Sleepless City"], datetime(2022, 12, 2), 20),
    ("Three Village Loop in Makuri Islands", 11.27, "Makuri Islands", ["Three Village Loop"], datetime(2022, 12, 1), 20),
    ("Two Village Loop in Makuri Islands", 10.59, "Makuri Islands", ["Two Village Loop"], datetime(2022, 11, 30), 20),
    ("Knickerbocker Reverse in New York", 11.27, "New York", ["Knickerbocker Reverse"], datetime(2022, 11, 30), 19),
    ("Flatland Loop in Makuri Islands", 12.47, "Makuri Islands", ["Flatland Loop"], datetime(2022, 11, 29), 19),
    ("Sprinter's Playground in Makuri Islands", 11.27, "Makuri Islands", ["Sprinter's Playground"], datetime(2022, 11, 29), 19),
    ("Island Outskirts in Makuri Islands", 8.17, "Makuri Islands", ["Island Outskirts"], datetime(2022, 11, 28), 19),
    ("Roule Ma Poule in France", 18.69, "France", ["Roule Ma Poule"], datetime(2022, 11, 27), 19),
    ("Douce France in France", 15.56, "France", ["Douce France"], datetime(2022, 11, 26), 19),
    ("Astoria Line 8 in New York", 9.36, "New York", ["Astoria Line 8"], datetime(2022, 11, 25), 19),
    ("Fine and Sandy in Makuri Islands", 8.17, "Makuri Islands", ["Fine and Sandy"], datetime(2022, 11, 25), 19),
    ("Twilight Harbor in Makuri Islands", 7.51, "Makuri Islands", ["Twilight Harbor"], datetime(2022, 11, 24), 19),
    ("The 6 Train in New York", 7.49, "New York", ["The 6 Train"], datetime(2022, 11, 24), 19),
    ("Neon Flats in Makuri Islands", 9.36, "Makuri Islands", ["Neon Flats"], datetime(2022, 11, 24), 19),
    ("Wandering Flats in Makuri Islands", 16.83, "Makuri Islands", ["Wandering Flats"], datetime(2022, 11, 24), 19),
    ("Knickerbocker in New York", 14.36, "New York", ["Knickerbocker"], datetime(2022, 11, 23), 18),
    ("Country to Coastal in Makuri Islands", 21.22, "Makuri Islands", ["Country to Coastal"], datetime(2022, 11, 23), 18),
    ("Jungle Circuit in Watopia", 13.76, "Watopia", ["Jungle Circuit"], datetime(2022, 11, 22), 18),
    ("London Loop in London", 10.61, "London", ["London Loop"], datetime(2022, 11, 22), 18),
    ("Queen's Highway in Yorkshire", 9.55, "Yorkshire", ["Queen's Highway"], datetime(2022, 11, 22), 18),
    ("Dutchy Estate in Yorkshire", 6.86, "Yorkshire", ["Dutchy Estate"], datetime(2022, 11, 20), 18),
    ("Volcano Circuit CCW in Watopia", 8.14, "Watopia", ["Volcano Circuit CCW", "Volcano Circuit"], datetime(2022, 11, 20), 18),
    ("Tour of Tewit Well in Yorkshire", 12.48, "Yorkshire", ["Tour of Tewit Well"], datetime(2022, 11, 20), 18),
    ("Innsbruckring in Innsbruck", 11.87, "Innsbruck", ["Innsbruckring"], datetime(2022, 11, 20), 17),
    ("The Pretzel in Watopia", 62.88, "Watopia", ["The Pretzel"], datetime(2022, 11, 19), 17),
    ("Greater London Loop in London", 31.79, "London", ["Greater London Loop"], datetime(2022, 11, 18), 17),
    ("Downtown Titans in Watopia", 34.24, "Watopia", ["Downtown Titans"], datetime(2022, 11, 17), 16),
    ("Makuri 40 in Makuri Islands", 31.15, "Makuri Islands", ["Makuri 40"], datetime(2022, 11, 14), 16),
    ("Big Foot Hills in Watopia", 46.76, "Watopia", ["Big Foot Hills"], datetime(2022, 11, 13), 16),
    ("Volcano Flat in Watopia", 10.62, "Watopia", ["Volcano Flat"], datetime(2022, 11, 12), 15),
    ("Dust In The Wind in Watopia", 34.87, "Watopia", ["Dust In The Wind"], datetime(2022, 11, 11), 15),
    ("Jungle Circuit in Watopia", 13.12, "Watopia", ["Jungle Circuit"], datetime(2022, 11, 10), 15),
    ("Park Perimeter Loop in New York", 8.21, "New York", ["Park Perimeter Loop"], datetime(2022, 11, 10), 15),
    ("Island Hopper in Makuri Islands", 11.91, "Makuri Islands", ["Island Hopper"], datetime(2022, 11, 10), 15),
    ("Turf N Surf in Makuri Islands", 15.61, "Makuri Islands", ["Turf N Surf"], datetime(2022, 11, 9), 15),
    ("Neokyo All-Nighter in Makuri Islands", 15.67, "Makuri Islands", ["Neokyo All-Nighter"], datetime(2022, 11, 9), 15),
    ("Suki's Playground in Makuri Islands", 12.50, "Makuri Islands", ["Suki's Playground"], datetime(2022, 11, 9), 14),
    ("Figure 8 in Watopia", 20.57, "Watopia", ["Figure 8"], datetime(2022, 11, 8), 14),
    ("The London Pretzel in London", 40.47, "London", ["The London Pretzel"], datetime(2022, 11, 7), 14),
    ("Greater London Flat in London", 8.12, "London", ["Greater London Flat"], datetime(2022, 11, 6), 13),
    ("2019 UCI Worlds Harrogate Circuit in Yorkshire", 12.49, "Yorkshire", ["2019 UCI Worlds Harrogate Circuit"], datetime(2022, 11, 6), 13),
    ("The Highline in New York", 11.24, "New York", ["The Highline"], datetime(2022, 11, 5), 13),
    ("Chasing the Sun in Makuri Islands", 22.43, "Makuri Islands", ["Chasing the Sun"], datetime(2022, 11, 5), 13),
    ("Out And Back Again in Watopia", 31.75, "Watopia", ["Out And Back Again"], datetime(2022, 11, 4), 13),
)

df = spark.createDataFrame(data, schema)
df.display()

# COMMAND ----------

df.createOrReplaceTempView("zwift_raw_data")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM zwift_raw_data