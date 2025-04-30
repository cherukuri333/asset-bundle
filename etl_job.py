from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETLJob").getOrCreate()

# Sample ETL
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
df = spark.createDataFrame(data, ["name", "age"])

df = df.filter("age > 30")
df.show()

spark.stop()