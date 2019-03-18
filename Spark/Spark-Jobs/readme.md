## Spark

 Spark: Fast and general engine for large scale data processing

 Spark can run on Spark cluster, YARN or Hadoop cluster.

 Spark is faster than Hadoop MapReduce beause of ***DAG Engine***. It creates a graph of all the steps to take untill the res is required.

 Note: Noting happens unless an action is called in spark.l

 Code in 
```
Python,
Java
Scala
```

 Spark is built around one main concept: That is RDD

 Spark supports (ALL built on Spark Core)
```
Spark streaming
Spark SQL
ML-lib
GraphX (Networks)
```

 Spark - RDD - Resilient Distributed Dataset

 Fudamentally it's a ***Dataset***, which can be distributed across multiple clusters and also supports Fault tolerance.

 We can create RDD's using spark context ***sc***
```
nums=sc.parallelize([1,2,3])
sc.textFile('/path')
	path can be
	- Local://
	- HDFS://
	- AWS s3n://
HiveCt = HiveContext(sc)
JDBC
Cassandra
Hbase
Elastisearch
Json, CSV, sequence Files, OBject Files, various compressed formats
```

 We can Perform two main operations on RDD
```
1. Transformation
	a. map
	b. flatMap
	c. filter
	d. distinct
	e. sample
	f. union, intersection, subtract, cartesian
2. Action	
	a. collect
	b. take
	c. top
	d. reduce
	e. ... many more...
```










