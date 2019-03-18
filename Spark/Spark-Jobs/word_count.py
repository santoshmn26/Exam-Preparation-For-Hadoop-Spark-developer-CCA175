from pyspark import SparkConf, SparkContext 
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

def normalize(text):
	return re.compile(r'\W+' , re.UNICODE).split(text.lower())

data = sc.textFile("anyfile.txt")

data_filter = data.flatmap(lambda x: x.split())

res = data_filter.countByValue()

