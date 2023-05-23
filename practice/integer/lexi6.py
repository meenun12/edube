from pyspark.sql.functions import lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from pyspark.sql import SparkSession


class CouncilsJob:


def __init__(self):
    self.spark_session = (SparkSession.builder
                          .master("local[*]")
                          .appName("EnglandCouncilsJob")
                          .getOrCreate())
    self.input_directory = "data"


def extract_councils(self, spark):
    path = "input_directory/data/england_councils"
    df_district_councils = spark.read.csv(f"{path}/district_councils.csv", header=True)
    df_london_boroughs = spark.read.csv(f"{path}/london_boroughs.csv", header=True)
    df_metropolitan_districts = spark.read.csv(f"{path}/metropolitan_districts.csv", header=True)
    df_unitary_authorities = spark.read.csv(f"{path}/unitary_authorities.csv", header=True)

    df_district_councils = df_district_councils.withColumn("council_type", lit("District Council"))
    df_london_boroughs = df_london_boroughs.withColumn("council_type", lit("London Borough"))
    df_metropolitan_districts = df_metropolitan_districts.withColumn("council_type", lit("Metropolitan District"))
    df_unitary_authorities = df_unitary_authorities.withColumn("council_type", lit("Unitary Authority"))

    df_all_councils = df_district_councils.union(df_london_boroughs).union(df_metropolitan_districts).union(
        df_unitary_authorities)

    return df_all_councils.select("council", "county", "council_type")


def extract_avg_price(self, spark):
    path = "input_directory/data"
    df_avg_price = spark.read.csv(f"{path}/property_avg_price.csv", header=True)

    return df_avg_price.select("local_authority", "avg_price_nov_2019")


def extract_sales_volume(self, spark):
    path = "input_directory/data"
    df_sales_volume = spark.read.csv(f"{path}/property_sales_volume.csv", header=True)

    return df_sales_volume.select("local_authority", "sales_volume_sep_2019")


def transform(self, spark):
    councils_df = self.extract_councils(spark)
    avg_price_df = self.extract_avg_price(spark)
    sales_volume_df = self.extract_sales_volume(spark)

    joined_df = councils_df.join(avg_price_df, councils_df.council == avg_price_df.local_authority, how="left") \
        .join(sales_volume_df, councils_df.council == sales_volume_df.local_authority, how="left") \
        .select(councils_df.council, councils_df.county, councils_df.council_type,
                avg_price_df.avg_price_nov_2019, sales_volume_df.sales_volume_sep_2019)

    return joined_df


def run(self):
    return self.transform(self.extract_councils(),
                          self.extract_avg_price(),
                          self.extract_sales_volume())
