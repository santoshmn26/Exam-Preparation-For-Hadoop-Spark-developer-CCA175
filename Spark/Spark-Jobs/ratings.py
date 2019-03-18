# get a list of rating value and total number of movies
from pyspark import SparkConf, SparkContext 
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("movie/u.data")
ratings = lines.map(lambda x: x.split()[2])
res = ratings.countByKey()

for i in res:
	print "%s %i" %(i, res[i])

