from pyspark import SparkConf, SparkContext 
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

# read the data
data = sc.textFile("/user/cloudera/1800.csv")

# Check the meta data
data.first()

# Fliter only minimum temp data
tmin  = data.filter(lambda x: "TMIN" in x).map(lambda x: (x.split(",")[1],x.split(",")[3]))

# Minimum temp for a perticular location ID
res = tmin.reduceByKey(lambda x,y: min(x,y))

for i in res.take(10):
	print(i)

# Similarly for Max temperature by location ID'
tmax = temp.filter(lambda x: "TMAX" in x).map(lambda x: (x.split(",")[0],x.split(",")[3]))
tmax = tmax.map(lambda x: (x[0],int(x[1])*0.1 * (9.0/5.0)+32.0))
res = tmax.reduceByKey(lambda x,y: max(x,y))
print(res.collect())


