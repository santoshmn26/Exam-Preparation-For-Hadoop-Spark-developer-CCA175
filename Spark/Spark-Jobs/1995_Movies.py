# get a list of rating value and total number of movies
from pyspark import SparkConf, SparkContext 
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)
# Load the file from hdfs
item = sc.textFile('movie/u.item')
item.first()

# Initilize the result list
res = []

# Get only first 3 columns
for i in item.collect():
    temp = i.split("|")
    res.append(temp[:3])

# Confirm the Output
for i in res[:3]:
    print(i)

# Convert it back to RDD
res_rdd = sc.parallelize(res)
res_rdd.first()

# Get all the movies in the year 1995
res = res_rdd.filter(lambda x: "1995" in x[1])

# Verify the result
for i in res.take(3): print (i)

# Get the total number of movies in the year 1995 (Ans: 296)
res.count()





