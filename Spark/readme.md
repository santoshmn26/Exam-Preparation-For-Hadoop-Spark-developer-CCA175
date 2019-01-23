# Spark 1.6.0

![alt text](https://github.com/santoshmn26/CCA175-Hadoop-Spark-developer/blob/master/Spark/download.png)




| Command | Files | Description | 
| ------- | --------- | ----------- |
| textFile() | RDD | Create a rdd file from a file present in HDFS, path of the file is passed as args. | 
| take(n) | RDD/DF | Displays/create a list of size n with the records from the rdd_file/DF. | 
| first() | RDD/DF | Display the first element from the rdd_file/DF | 
| **takeSample(rep,n,seed)** | **RDD** | ***Returns a list of size n with random number records from the rdd_file.*** |
| count() | RDD/DF | count the number of records in the rdd_file/DF | 
| **show()** | **DF** | ***Display pretty table of top 20 rows of a DF.*** | 
| **persist()** | **DF** | ***Display column name and data type.*** |
| **columns** | **DF** | ***Display only column names.*** |
| collect() | RDD/DF | Displays the entire content of the rdd_file/DF. ***CAUTION while using this can cause huge load since the files are large.*** |
| map() | | |
| filter() | | |
| flatMap() | | Return a new dataset formed by selecting those elements of the source on which func returns true. |
| reduceByKey() | | |
| join() | RDD | Perform ***Inner*** join |
| leftOuterJoin()| RDD | Perform ***left*** outer join |
| rightOuterJoin()| RDD | Perform ***right*** outer join |
| fullOuterJoin()| RDD | Perform ***full*** outer join |
| distinct() | RDD | Get a list of all distinct values in a RDD |
| countByKey() | RDD | Get a count of keys provides (K,V) returns (K,count(V))
| sample(rep,fraction,seed) | RDD/DF | returns a fraction of sample. |   

| No. | Examples |
| --- |-------- |
| 1. | Creating RDD from a list |
| 2. | Create a RDD from a local file |
| 3. | Using sqlContext.load() and sqlContext.read() |
| 4. | Using map() transformation function |
| 5. | Using filter() |
| 6. | Create a Rdd from a file in hdfs |
| 7. | Create a RDD from a file in local file system |
| 8. | Word ocunt using flatMap(), map() and reduceByKey() |
| 9. | Using sample() |
| 10. | Using distinct() |
| 11. | Using joins() |
| 12. | Using leftOuterJoin(), rightOuterJoin() and fullOuterJoin() |
| 13. | Using countByKey() for word count |

> Note: If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using reduceByKey or aggregateByKey will yield much better performance. 

> Note: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numTasks argument to set a different number of tasks.

> Note: DataFrame (DF): also known as RDD with a Data structure associated with it.

> Note: countByKey() returns a python Dict and not a RDD. Not practical for large datasets. Use reduceByKey() or aggrigateByKey().

> Note: countByKey() is a action not a transformation, where as reduceByKey() and aggrigateByKey() are transformations.

> Note: CAUTION while using this can cause huge load since the files are large.


### 1. Creating RDD from a list
```
list to rdd 
1 = list()
l = range(1,1000)
l_rdd = sc.parallelize(l)
```
----
### 2. Create a RDD from a local file

First download the file from HDFS
```
hadoop fs -get /user/cloudera/spark/orders/part-m-00000 /home/cloudera/spark/
```
Now open pyspark to execute the following
```
orders_raw = open("/home/cloudera/spark/part-m-00000").read().splitlines()
type(orders_raw)
orders_rdd = sc.prallelize(orders_raw)
type(orders_rdd)
```
### File type for reading data 

> text

> parquet

> orc

> json
----

### 3. Using sqlContext.load() and sqlContext.read()

**sqlContext.load("path",format)**
```
sqlContext.load("/user/cloudera/spark/orders/*",json)
```
**sqlContext.load.format()**
```
sqlContext.read.json("/user/cloudera/spark/orders/*")
```
----

### 4. Using map() transformation function

First create a RDD from a file in hdfs
```
rdd_file=sc.textFile("/home/cloudera/spark/orders/")
```
Perform transformation in spark shell
```
rdd_file.map(lambda x: x.split(",")[3]).first()
```
----
## 5. Using filter()

Return a new dataset formed by selecting those elements of the source on which func returns true. 

In this example lets get all the records from orders which have the status = 'CLOSED'
```
orders.take(2)
[u'1,2013-07-25 00:00:00.0,11599,CLOSED', u'2,2013-07-25 00:00:00.0,256,PENDING_PAYMENT']
res = orders.filter(lambda x: x.split(',')[3]=='CLOSED')
res.take(2)
[u'1,2013-07-25 00:00:00.0,11599,CLOSED', u'4,2013-07-25 00:00:00.0,8827,CLOSED']
res.count()
7556
```
----
### 6. Create a Rdd from a file in hdfs

First load the file into HDFS if the file is not already present either using sqoop to import if the file is in a database or just -put if the file is in local.

Now execute the following in spark shell
```
orders = sc.textFile("/user/cloudera/spark/orders/*")
orders.first()
u'1,2013-07-25 00:00:00.0,11599,CLOSED'
type(orders.first())
<type 'unicode'>
```
----

### 7. Create a RDD from a file in local file system

```
raw_file = open("/home/cloudera/spark/word_count").read().splitlines()
type(raw_file)
<type 'list'>
rdd_file = sc.parallelize(raw_file)
type(rdd_file)
<class 'pyspark.rdd.RDD'>
```
----

### 8. Word ocunt using flatMap(), map() and reduceByKey()

To understand this word count we need understand the difference between map() and flatMapt()

word_count file:
```
Hello this is a 
word connt program demo
agin this is just a
demo for the word count
program written in pyhon!
```

> map() function returns a list of values with the count similar to the input

> flatMap() function returns a list of values which is not similar to the input. The output may increase, decrease or even remain the same depending on the input.

```
wc = sc.textFile("/home/cloudera/spark/word_count")
keys = wc.flatMap(lambda x: x.split(" ")).map(lambda x: (x,1))
res = keys.reduceByKey(lambda x,y: (x+y))
for i in res.take(10): print (i)
```
In this example: 

> flatMap() returns ["Hello","this","is","a",..]

> map() returns[("Hello",1),("this",1),("a",1),...]

> reduceByKey() returns[("Hello",1),("this",2),("a",2),...]

```
wc = sc.textFile("/home/cloudera/spark/word_count")
res = wc.flatMap(lambda x: x.split(" ")).map(lambda x: (x,1)).reduceByKey(lambda x,y: (x+y))
for i in res.take(10): print (i)
```
----

### 9. Using sample()

> syntax: sample(replacement,fraction,seed)

seed is optional
```
res = wc.sample(True,0.5,2)
res.collect()
[u'demo for the word count', u'program written in pyhon!']
```

In the above example:

> Replacement is set to True

> Fraction is set to 0.5

> Seed is set to 2
----

### 10. Using distinct()

As the name suggests returns the distinct values in the list
```
res=wc.distinct()
res.collect()
```
----

### 11. Using joins()

First step is to load the two files to perform join
```
orders = sc.textFile("/user/cloudera/spark/orders/")
order_items = sc.textFile("/user/cloudera/spark/order_items/")
```
Next step is to create two lists of (K,V) and (K,W) to get the output of (K,(V,W))

Now create a list of sets (K,V) and (K,W)
```
om = orders.map(lambda x: (int(x.split(',')[1]),x.split(',')[-1]))
oim = order_items.map(lambda x: (int(x.split(',')[0]),x.split(',')[-1]))
om.first()
(1, u'CLOSED')
oim.first()
(1, u'299.98')
```
Now we can perform join between the two RDD's
```
join = om.join(oim)
join.first()
(32768, (u'PENDING_PAYMENT', u'199.99'))
```
----
### 12. Using leftOuterJoin(), rightOuterJoin() and fullOuterJoin()

When performing ***left*** outer join between table A and B: All records from table A and matches with table B (Possible Null/None values from table B added to res)

> Syntax: join = a.leftOuterJoin(b)

When performing ***right*** outer join between table A and B: All records from table B and matches with table A (Possible Null/None values from table A added to res)

> Syntax: join = b.rightOuterJoin(a)

When performing ***full*** outer join between table A and B: All records from table A and B (Possible Null/None values from table A and B added to res).

> Syntax: join = b.fullOuterJoin(a)

```
ljoin = om.leftOuterJoin(oim)
rjoin = oim.rightOuterJoin(om)
fjoin = om.fullOuterJoin(oim)
```
----

### 13. Using countByKey() for word count

countByKey() is only available on RDDs of type (K, V). Returns a hashmap of (K, Int) pairs with the count of each key. 

**Note: countByKey() returns a python Dict and not a RDD. Not practical for large datasets**

```
res = temp.flatMap(lambda x: x.split(" ")).map(lambda x: (x,1)).countByKey()
type(res)
<type 'collections.defaultdict'>
res
defaultdict(<type 'int'>, {u'a': 2, u'': 1, u'pyhon!': 1, u'word': 2, u'agin': 1, u'just': 1, u'this': 2, u'demo': 2, u'is': 2, u'count': 1, u'for': 1, u'written': 1, u'program': 2, u'in': 1, u'the': 1, u'Hello': 1, u'connt': 1})
```
----

### 14. 





