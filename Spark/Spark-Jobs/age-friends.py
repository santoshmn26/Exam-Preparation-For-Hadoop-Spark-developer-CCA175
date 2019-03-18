from pyspark import SparkConf, SparkContext 
import collections

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf = conf)

# data contains (age,friend)
# required initial output (age,(total_friends, num of people with age = age)
# required final output (age, avg_num of friends)

data = [(50, 49), (50, 96), (72, 34), (25, 11), (20, 0), (33, 39), (33, 16), (25, 91), (55, 64), (50, 8), (50, 54), (72, 89), (20, 77), (20, 10), (72, 53), (33, 86), (50, 37), (10, 30), (72, 79), (25, 95), (33, 67), (55, 25), (72, 52), (72, 97), (33, 75), (20, 71), (20, 92), (16, 54), (33, 59), (33, 91), (25, 90), (50, 62), (55, 49), (25, 19), (55, 84), (25, 80), (20, 30), (55, 73), (72, 90), (10, 73), (20, 98), (72, 80), (50, 74), (72, 55), (72, 12), (55, 21), (50, 86), (33, 63), (55, 66), (50, 39), (25, 40), (10, 33), (16, 81), (55, 24), (10, 95), (25, 38), (10, 2), (25, 29), (55, 96), (20, 97), (25, 15), (72, 24), (72, 39), (16, 6), (72, 86), (50, 96), (55, 65), (20, 9), (20, 70), (50, 35), (72, 40), (16, 95), (16, 69), (16, 64), (33, 37), (16, 78), (16, 92), (55, 36), (50, 98), (50, 46), (16, 65), (16, 60), (25, 79), (33, 69), (50, 38), (25, 33), (16, 83), (20, 23), (16, 79), (10, 6), (50, 71), (10, 95), (10, 66), (50, 57), (16, 32), (16, 66), (55, 6), (20, 66), (72, 94), (16, 12)]

# convert data [list] to data_rdd [rdd]
data_rdd = sc.parallelize(data)

# map each age group to (age,(friends,1))
data_mapped = data_rdd.map(lambda x: (x[0],(x[1],1)))

# test output
print(data_mapped.first())

# get count of age group and total friends
res = data_mapped.reduceByKey(lambda x,y: (x[0]+y[0],x[1]+y[1]))

# final result (age, avg_num of friends)
result = res.mapValues(lambda x: x[0]/x[1])

for i in result.collect():
	print(i)





