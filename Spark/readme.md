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
| **persist()** | **DF** | ***Store the DF in memory to avoid recomputation of the DF.*** |
| **columns** | **DF** | ***Display only column names.*** |
| collect() | RDD/DF | Displays the entire content of the rdd_file/DF. ***CAUTION while using this can cause huge load since the files are large.*** |
| map() | RDD/DF | Return a new distributed dataset formed by passing each element of the source through a function func. |
| filter() | RDD/DF | Return a new dataset formed by selecting those elements of the source on which func returns true. |
| flatMap() | RDD/DF | Return a new dataset formed by selecting those elements of the source on which func returns true. |
| join() | RDD | Perform ***Inner*** join |
| leftOuterJoin()| RDD | Perform ***left*** outer join |
| rightOuterJoin()| RDD | Perform ***right*** outer join |
| fullOuterJoin()| RDD | Perform ***full*** outer join |
| distinct() | RDD/DF | Get a list of all distinct values in a RDD |
| reduceByKey(f) | RDD/DF | Returns (K,count(V)) for a list of inputs (K,V). Requires a lambda function |
| groupByKey(f) | RDD/DF | For input pairs (K,V) returns pairs of (K, special_rdd_list(\[all values of Key k])) |
| aggregateByKey(,s,c) | RDD/DF | For input pairs (K,V) returns output pairs of (K,U), where V and U need not be of same data-type |
| countByKey() | RDD/DF | Get a count of keys provides (K,V) returns (K,count(K)). Does not need a lambda function |
| sample(rep,fraction,seed) | RDD/DF | returns a fraction of sample. |   
| top(n,key) | RDD/DF | Returns a python list sorted based on key (lambda function) in ***desc (can be manipulated to return in desc)*** 
| takeOrdered(n,key) | RDD/DF | Similar to top() but returns python list in ***asc (can be manipulated to return in desc)*** |
| parallelize() | RDD | takes a list as input and converts it to rdd |
| countByKey() | RDD | Takes (K,V) as inputs and returns (K,count(V)) as output. O/P format:  Python dict |
| sortByKey() | RDD | Takes (K,V) or ((K1,K2),V).. sorts based on keys asc = True by default |
| Union | RDD/DF | Gets all the elements from both the data sets |
| Intersection | RDD/DF | Gets elements that are common in both data sets | 
| Distinct | RDD/DF | Gets distinct elements from the data set |
| saveAsTextFile | RDD/DF | Save a rdd or df to HDFS as a text file |
| saveAsSequenceFile | RDD/DF | Save a rdd or df to HDFS as a sequence file |
| ***save(path,format)*** | RDD/DF | ***Save a DF (Not RDD)to HDFS*** |
| ***write.format(path)*** | RDD/DF | ***Save a  DF (Not RDD)to HDFS*** |

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
| 14. | Using reduceByKey(f) |
| ***15.*** | ***Using groupByKey()*** |
| 16. | Using reduceByKey(f) for advance operations |
| ***17.*** | ***Using aggregateByKey(,s,c)*** |
| 18. | Using sortByKey([asc=1]) |
| 19. | Using sortByKey() advanced for multiple sorts |
| 20. | Using top() and takeOrdered() |
| ***21.*** | ***Using groupByKey() and sorted(K, Key, reverse=False)*** |
| ***22.*** | ***Load avrofile as a normal csv file using sqlContext*** |
| 23. | Using groupByKey() and python API sorted(K, Key=, reverse=False) |
| 24. | Using itertools python's collection package* |


> Note: If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using reduceByKey or aggregateByKey will yield much better performance. 

> Note: reduceByKey and aggregateByKey uses combiner which increases the performance compared to groupByKey.

> Note: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numTasks argument to set a different number of tasks.

> Note: DataFrame (DF): also known as RDD with a Data structure associated with it.

> Note: countByKey() returns a python Dict and not a RDD. Not practical for large datasets. Use reduceByKey() or aggrigateByKey().

> Note: countByKey() is a action not a transformation, where as reduceByKey() and aggrigateByKey() are transformations.

> Note: CAUTION while using this can cause huge load since the files are large.

> Note: distinct() used on DF returns DataFrame\[col_name: col_type].

 > Note: save and write works only on DF.***
### Difference between groupByKey and aggregateByKey, reduceByKey:

groupByKey uses ***single thread*** example:

Consider we need to perform sum of the key 1 which has values (1 to 1000). groupByKey uses the following method
> (1,(1 to 1000))  sum(1,1000) => 1+2+3+.....1000.
same example performed by aggregateByKey and reduceByKey which uses ***multiple resources/threads***
> (1, (1 to 1000)) sum(1,1000) => sum(sum(1,250),sum(251,500),sum(501,750),sum(751,1000)).

### Difference between aggregateByKey and reduceByKey:

In the above example we see that the logic for computing is sum(sum's) i.e the computing the intermediate values and the final value / combiner logic are same. 

When the logic for computing the ***intermediate values and combiner are same*** we need to use reduceByKey(f) and pass a lambda function with the logic

example:
> reduceByKey(lambda x,y: (x+y))

When the logic for computing the ***intermediate values and combiner are Different*** we need to use aggregateByKey(seqOP,comOp)
we need to pass both logic to compute intermediate logic and a logic for the combiner.



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
### 14. Using reduceByKey(f)

Consider the following example:

First we create a RDD for order_items 
```
order_items=sc.textFile("/user/cloudera/spark/order_items/")
order_first()
u'1,1,957,1,299.98,299.98'
```
For this example our aim is to calculate the total revenue for order_item_id = 2, for which we need the ***2nd and the 4th element from each row.***

Next step is to extract all values for order_item_id = 2
```
temp = order_items.map(lambda x: (int(x.split(",")[1]) , float(x.split(",")[4]))).filter(lambda x: (int(x[0])==2))
temp.first()
(2, , 199.99000000000001)
```
Next we need to perform the sum of the 2nd element in the list

See what happens if we use countByKey() and reduceByKey()
```
res = temp.reduceByKey(lambda x,y: x+y)
res.first()
(2, 579.98000000000002)
res_c = temp.countByKey()
res_c
defaultdict(<type 'int'>, {2: 3})
```
***As we can see countByKey() just returns number of keys present in the input.***
----

### 15. Using groupByKey()

Consider the similar example to 14. where we try to find the total revenue for all order_item_id

For this example our aim is to calculate the total revenue for all order_item_id, for which we need the ***2nd and the 4th element from each row.***

Next step is to extract all values for all order_item_id
```
temp = order_items.map(lambda x: (int(x.split(",")[1]) , float(x.split(",")[4])))
temp.first()
(1, 299.98000000000002)
```
Next we need to perform the sum of the 2nd element in the list for each order_item_id. Let's try to achieve this using groupByKey()
```
res = temp.countByKey()
res
PythonRDD[100] at RDD at PythonRDD.scala:43

for i in x.take(5): print(i)
...
(32768, <pyspark.resultiterable.ResultIterable object at 0x294c950>)
(49152, <pyspark.resultiterable.ResultIterable object at 0x294c8d0>)
(4, <pyspark.resultiterable.ResultIterable object at 0x294c290>)
(50192, <pyspark.resultiterable.ResultIterable object at 0x294c850>)
(8, <pyspark.resultiterable.ResultIterable object at 0x294c690>)

for i in x.take(5): list(i[1])
... 
[199.99000000000001, 129.99000000000001, 299.98000000000002, 399.98000000000002]
[299.98000000000002]
[49.979999999999997, 299.94999999999999, 150.0, 199.91999999999999]
[129.99000000000001, 140.0, 249.90000000000001]
[179.97, 299.94999999999999, 199.91999999999999, 50.0]

for i in x.take(5): sum(list(i[1]))
... 
1029.9400000000001
299.98000000000002
699.85000000000002
519.88999999999999
729.83999999999992
```
----
### 16. Using reduceByKey(f) for advance operations 

In this example use reduceByKey(f) for getting a list of the greatest,least sub-total for all the order_items_id
```
temp = order_items.map(lambda x: (int(x.split(",")[1]) , float(x.split(",")[4]))).filter(lambda x: (int(x.split(",")[1]==2)))
temp.take(3)
[(2, 199.99000000000001), (2, 250.0), (2, 129.99000000000001)]

res = temp.reduceByKey(lambda x,y: x+y)
res.first()
(2, 579.98000000000002) 

res = temp.reduceByKey(lambda x,y: x if x>y else y)
(2, 129.99000000000001)   

res = temp.reduceByKey(lambda x,y: x if x>y else y)
(2, 250.0)
```
Next example the problem statement is to get all the records with all fields whose sub_total value is the least for each order_item_id.

i.e for every order_item_id there are multiple row's, our aim to get only the rows wher the sub_total value is the least.

Note when we use reduceByKey(f) we have to pass a list of (K,V)'s we cannot pass a list with just one field.

***i.e we cannot perform the following:***
```
order_items.first()
u'1,1,957,1,299.98,299.98'

reduceByKey(lambda x,y: x if (float(x.split(",")[4])>float(y.split(",")[4])) else y )
ERROR!
```
***We cannot go with the above solution because x,y values in the lambda points to the V values in the list (K,V) but in the above senario we are passing a list with only one value (K)***

Alternate solution is to create a list with two values (K,V) \[(1, u'1,1,957,1,299.98,299.98')]

We are creating a list of (order_item_id, entire row)
```
order_items.first()
u'1,1,957,1,299.98,299.98'

temp = order_items.map(lambda x: (int(x.split(",")[1]) , x)))
temp.first()
(1, u'1,1,957,1,299.98,299.98')

res = temp.reduceByKey(lambda x,y: x if float(x.split(",")[4])<float(x.split(",")[4]) else y )
res.first()
(1, u'1,1,957,1,299.98,299.98')                                                 

for i in res.take(2): print(i[1])
... 
1,1,957,1,299.98,299.98
4,2,403,1,129.99,129.99
```
----

### 17. Using aggregateByKey(,s,c)

> Note: Both ***aggregateByKey(,s,c) and reduceByKey(f) uses multiple threads*** to perform its tasks.

We use aggregateByKey when we need the output in a different data type compared to input data type

***Input and output for aggregateByKey()

**Input: (K,V) pairs**

**Output: (K,U) pairs**

> Note: V and U need not be of same data type.

For this problem statement we are trying to get a list of (order_item_id, (total_revnue, count(order_item_id)))

First step lets try to get (K,V) for out problem statement, so for this example we need (order_item_id, sub_total)

If we have sub_total we can calculate total_revnue and count(order_item_id)

```
order_items = sc.textFile("/user/cloudera/spark/order_items/")
order_items.first()
u'1,1,957,1,299.98,299.98'

temp = order_items.map(lambda x: (int(x.split(",")[1]), float(x.split(",")[4])))
for i in temp.take(5): print(i)
(1, 299.98000000000002)
(2, 199.99000000000001)
(2, 250.0)
(2, 129.99000000000001)
(4, 49.979999999999997)
```

Now consider the rows only for the order_item_id = 2

We have the following
```
(2, 199.99000000000001)
(2, 250.0)
(2, 129.99000000000001)
```
We know that aggregateByKey uses threads so assume, that the first two rows will be an input for 1st thread and the 3rd row will be an input for the 2nd thread.

We need the output as (order_item_id, (sum(sub_total), count(order_item_id))) so, the logic for the threads will be as follows

\# sub-list of the output sum(sub_total) would be float and count(order_item_id) would be int

\# initilize the temp variable
```
x = (0.0 , 0) # Output
t = (2, 199.99000000000001) # Input 
y = t[1]
x = (x[0] + y, x[1] + 1) 
print(x)
(199.99000000000001, 1)

Next input 
t = (2, 250.0)              # Input 
y = t[1]
x = (199.99000000000001, 1) 
x = (x[0] + y, x[1] + 1) 
print(x)
(449.99000000000001, 2)
```
Finally output from the 1st thread will be:    x1 = (449.99000000000001, 2)

Similarly Output from the 2nd thread will be:  x2 = (129.99000000000001, 1)

Next we have to write our reducer logic
```
x = (x1[0] + x2[0], x1[1],x2[1])

print(x)
(579.9800000000002, 3)
```
Threfore we get the following:

| Initilizer / output data type | (0.0, 0) |
| Combiner Logic | (x\[0] + y, x\[1] + 1) |
| Reducer Logic | x = (x1\[0] + x2\[0], x1\[1],x2\[1]) |

### Now we can use aggregateByKey()
```
order_items = sc.textFile("/user/cloudera/spark/order_items/")
order_items.first()
u'1,1,957,1,299.98,299.98'

temp = order_items.map(lambda x: (int(x.split(",")[1]),float(x.split(",")[4])))
temp.first()

res = temp.aggregateByKey((0.0,0), lambda x,y: (x[0] + y, x[1]+1), lambda x1,x2: (x1[0] + x1[0], x1[0] + x1[0]))
res.sortByKey()
for i in res.take(6): print(i)
1, (299.98000000000002, 1))                                                    
(2, (579.98000000000002, 3))
(4, (699.85000000000002, 4))
(5, (1129.8600000000001, 5))
(7, (579.92000000000007, 3))
(8, (729.83999999999992, 4))
```
----
### 18. Using sortByKey([asc=1])

> Default sort is asc which is value 1 or sortByKey(1)

> Sorting in Desc: sortByKey(0)

Consider the output from the previous example:

```
x=res.sortByKey(0)
for i in x.take(10): print(i)
(68883, (2149.9899999999998, 2))
(68882, (109.99000000000001, 2))
(68881, (129.99000000000001, 1))
(68880, (999.76999999999998, 5))
(68879, (1259.97, 3))
(68878, (739.93000000000006, 4))
(68875, (2399.9499999999998, 2))
(68873, (859.91000000000008, 5))
(68871, (499.98000000000002, 2))
(68870, (479.91999999999996, 2))
```

### 19. Using sortByKey() advanced for multiple sorts

***Problem statement: Sort the data in acending order for order_item_id and decending for sub_total, by passing multiple keys as input ((K1,K2),V)***

First step check the first sort requirement
```
order_items.first()
u'1,1,957,1,299.98,299.98'
```
### Sort the data on field\[1] asc and then field\[4]desc

Next create keys for sortByKey()
```
temp = order_items.map(lambda x: ((int(x.split(",")[1]), float(x.split(",")[4])),x))
temp.first()
((1, 299.98000000000002), u'1,1,957,1,299.98,299.98')
```
Now we have ((K1, K2), V) so, we can perform sort
```
res = temp.sortByKey()
for i in res.take(10): print (i)
((1, 299.98000000000002), u'1,1,957,1,299.98,299.98')                           
((2, 129.99000000000001), u'4,2,403,1,129.99,129.99')
((2, 199.99000000000001), u'2,2,1073,1,199.99,199.99')
((2, 250.0), u'3,2,502,5,250.0,50.0')
((4, 49.979999999999997), u'5,4,897,2,49.98,24.99')
((4, 150.0), u'7,4,502,3,150.0,50.0')
((4, 199.91999999999999), u'8,4,1014,4,199.92,49.98')
((4, 299.94999999999999), u'6,4,365,5,299.95,59.99')
((5, 99.959999999999994), u'11,5,1014,2,99.96,49.98')
((5, 129.99000000000001), u'13,5,403,1,129.99,129.99')
```
From the output we can see that the first field is sorted asc. 

But ***We need the 2nd key to be sorted in desc***.

Instead of 
```
((2, 129.99000000000001), u'4,2,403,1,129.99,129.99')
((2, 199.99000000000001), u'2,2,1073,1,199.99,199.99')
((2, 250.0), u'3,2,502,5,250.0,50.0')
```
We need the output to be
```
((2, 250.0), u'3,2,502,5,250.0,50.0')
((2, 199.99000000000001), u'2,2,1073,1,199.99,199.99')
((2, 129.99000000000001), u'4,2,403,1,129.99,129.99')
```
***One soluton or a trick is to convert the 2nd key values to negative***

temp = order_items.map(lambda x: ((int(x.split(",")\[1]), ***-float(x.split(",")\[4])),x))***
```
temp = order_items.map(lambda x: ((int(x.split(",")[1]), -float(x.split(",")[4])),x))
temp.first()
((1, -299.98000000000002), u'1,1,957,1,299.98,299.98')

res = temp.sortByKey()

for i in res.take(5):print(i)
((1, -299.98000000000002), u'1,1,957,1,299.98,299.98')                          
((2, -250.0), u'3,2,502,5,250.0,50.0')
((2, -199.99000000000001), u'2,2,1073,1,199.99,199.99')
((2, -129.99000000000001), u'4,2,403,1,129.99,129.99')
((4, -299.94999999999999), u'6,4,365,5,299.95,59.99')

for i in res.take(5): print(i[1])
1,1,957,1,299.98,299.98
3,2,502,5,250.0,50.0
2,2,1073,1,199.99,199.99
4,2,403,1,129.99,129.99
6,4,365,5,299.95,59.99
```
----
### 20. Using top(n,key) and takeOrdered(n,key)

***Problem statement: Sort the data and get the top 10 sub_total values from order_items***
```
res = order_items.top(10, lambda x: float(x.split(",")[4]))
type(res)
<class 'list'>

for i in res: print(i)
171765,68703,208,1,1999.99,1999.99
171806,68722,208,1,1999.99,1999.99
171811,68724,208,1,1999.99,1999.99
171837,68736,208,1,1999.99,1999.99
171920,68766,208,1,1999.99,1999.99
171961,68778,208,1,1999.99,1999.99
172019,68806,208,1,1999.99,1999.99
172032,68809,208,1,1999.99,1999.99
172060,68821,208,1,1999.99,1999.99
172101,68837,208,1,1999.99,1999.99
```

To get in desc

res = order_items.top(10, lambda x: ***-float(x.split(",")\[4]))***

### OR

Use ***takeOrdered(n,key)***
```
res = order_items.takeOrdered(10, lambda x: float(x.split(",")[4]))
for i in res: print(i)
575,234,775,1,9.99,9.99
4866,1944,775,1,9.99,9.99
5066,2023,775,1,9.99,9.99
5713,2277,775,1,9.99,9.99
13487,5404,775,1,9.99,9.99
13859,5557,775,1,9.99,9.99
13959,5597,775,1,9.99,9.99
15441,6177,775,1,9.99,9.99
18434,7361,775,1,9.99,9.99
18497,7387,775,1,9.99,9.99
```
----

----
### 21. Using groupByKey() and sorted(K, Key, reverse=False)*

### Problem statement: Get order item details in descending order by revenue - groupByKey()

***Same problem statement is achieved using sortByKey() with two keys check 19***

### Solution:
```
oi = sc.textFile("/user/cloudera/spark/order_items")
for i in oi.take(4): print(i)
temp = oi.map(lambda x: (int(x.split(",")[1]),x))
for i in temp.take(4): print(i)
temp.groupByKey()
for i in temp.take(4): print(i)
res = temp.map(lambda x: sorted(x[1], key=lambda y: (float(y.split(",")[4])) ,reverse=True))
for i in res.take(4): print(i)
F_res = temp.flatMap(lambda x: sorted(x[1], key=lambda y: (float(y.split(",")[4])) ,reverse=True))
for i in F_res.take(4): print(i)
```

***Note: Check the difference of using map and flatMap***

***Note: sorted() default value for reverse = False

Steps followed:
```
1. Load the data
2. Create (K,V) for groupByKey() => (field[1],field[4])
3. Use groupByKey to create (K , resultIterable)
4. Use flatMap to map results in resultIterable and sort them using sorted
5. Verify the resultIterable
```
----
### 22. Load avrofile as a normal csv file using sqlContext*

### Problem statement: Import a table from sql as avrodata if not already present in the hdfs and create a rdd using the file in the hdfs

```
orders_DF = sqlContext.read.format("com.databricks.spark.avro").load("/user/cloudera/orders_avrodata/")
orders_RDD = orders_DF.rdd.map(list)
```
----
### 23. Using groupByKey() and python API sorted(K, Key=, reverse=False)

### Problem statement: Similar to 22 Get order item details in descending order by revenue on products table - groupByKey()

***Same problem statement is achieved using sortByKey() with two keys check 19 But here we are using sorted Python's API***

Solution:
```
products = sc.textFile("/user/cloudera/spark/products")
products = products.filter(lambda x: x.split(",")[4]!="")
temp = products.map(lambda x: (int(x.split(",")[1]),x)).groupByKey()
res = temp.flatMap(lambda x: sorted(x[1],key=lambda y: float(y.split(",")[4]),reverse=True))
for i in res.take(10): print(i)
```
----
### 24. Using itertools python's collection package*

### Problem statement: Products table have multiple sub_total for same order_item_id. Our aim to get the top 3 sub_totals for all order_item_id.

Example:
```
1,2,Quest Q64 10 FT. x 10 FT. Slant Leg Instant U,,59.98,http://images.acmesports.sports/Quest+Q64+10+FT.+x+10+FT.+Slant+Leg+Instant+Up+Canopy
2,2,Under Armour Men's Highlight MC Football Clea,,129.99,http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat
3,2,Under Armour Men's Renegade D Mid Football Cl,,89.99,http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat
4,2,Under Armour Men's Renegade D Mid Football Cl,,89.99,http://images.acmesports.sports/Under+Armour+Men%27s+Renegade+D+Mid+Football+Cleat
5,2,Riddell Youth Revolution Speed Custom Footbal,,199.99,http://images.acmesports.sports/Riddell+Youth+Revolution+Speed+Custom+Football+Helmet
6,2,Jordan Men's VI Retro TD Football Cleat,,134.99,http://images.acmesports.sports/Jordan+Men%27s+VI+Retro+TD+Football+Cleat
7,2,Schutt Youth Recruit Hybrid Custom Football H,,99.99,http://images.acmesports.sports/Schutt+Youth+Recruit+Hybrid+Custom+Football+Helmet+2014
8,2,Nike Men's Vapor Carbon Elite TD Football Cle,,129.99,http://images.acmesports.sports/Nike+Men%27s+Vapor+Carbon+Elite+TD+Football+Cleat
9,2,Nike Adult Vapor Jet 3.0 Receiver Gloves,,50.0,http://images.acmesports.sports/Nike+Adult+Vapor+Jet+3.0+Receiver+Gloves
```

***We see that for the same id = 2 we have different sub_total. Our aim is to obtain only sets top 3 values.***

**Sample result for id = 2:**
```
5,2,Riddell Youth Revolution Speed Custom Footbal,,199.99,http://images.acmesports.sports/Riddell+Youth+Revolution+Speed+Custom+Football+Helmet
6,2,Jordan Men's VI Retro TD Football Cleat,,134.99,http://images.acmesports.sports/Jordan+Men%27s+VI+Retro+TD+Football+Cleat
2,2,Under Armour Men's Highlight MC Football Clea,,129.99,http://images.acmesports.sports/Under+Armour+Men%27s+Highlight+MC+Football+Cleat
8,2,Nike Men's Vapor Carbon Elite TD Football Cle,,129.99,http://images.acmesports.sports/Nike+Men%27s+Vapor+Carbon+Elite+TD+Football+Cleat
```
### Note: In the output we have 129.99 twice.

### Solution:
```
products = sc.textFile("/user/cloudera/spark/products/")
products = products.filter(lambda x: x.split(",")[4]!='')
temp = products.map(lambda x: (int(x.split(",")[1]),x))
temp = temp.groupByKey()
temp_1 = temp.filter(lambda x: x[0]==2)
temp_2 = temp_1.flatMap(lambda x: sorted(x[1],key=lambda y: float(y.split(",")[4]),reverse=True))
for i in temp_2.take(10): print i 
temp_values = temp_2.map(lambda x: x.split(",")[4])
r = set(temp_values.collect())
s = sorted(r,reverse=True)
top_values = s[:3]
import itertools as it
k = it.takewhile(lambda x: float(x.split(",")[4]) in top_values, temp_2.collect())
for i in k: print i
```
----

def top_3_values(products_iterable):


----
----
### 25. Load data from mysql db using sqlContext

**Problem statement: Load table orders from mysql into spark Data frame**

**Solution:**
```
orders_data_frame = sqlContext.read.format("jdbc").options(
url = "jdbc:mysql://localhost/retail_db", 
user = "root", 
password = "cloudera", 
dbtable = "orders").load()
```
----
### 26. Convert DF to RDD and RDD to DF

**Problem statement: Converting a DF to RDD and RDD to DF.**
> 1. DF to RDD
```
new_rdd = old_df.rdd.map(list)
```
> 2. RDD to DF
```
new_df = rdd_file.toDF(schema = ["order_id","order_item_id"])
```
----
### 27. Using sets operations Union and Intersection.

**Note: While using Sets operation make sure data from both the setes have a similar structure.**

| Union | Full Outer join | Gets all the elements from both the data sets |
| Intersection | Inner join | Gets elements that are common in both data sets | 
| Distinct | - | Gets distinct elements from the data set |

**Syntax: res = data_set_a.union(data_set_b)** 

**Problem statement: create two data sets for year 2013-12 and 2014-01 and perform union**
```
orders = sc.textFile("/user/cloudera/spark/orders")
o_2013_12 = orders.filter(lambda x: x.split(",")[1][:7]=="2013-12")
o_2013_10 = orders.filter(lambda x: x.split(",")[1][:7]=="2013-10")
res_union = o_2013_12.union(o_2013_10)
res_intersection = o_2013_12.intersection(o_2013_10)
res_subtraction = res_union.subtract(res_intersection)
```
----
### 28. Using saveAsTextFile(path,compression=None) to save data in HDFS

Syntax: rdd.saveAsTextFile("/path",compressionCodecClass=org.apache.hadoop.io.compression.SnappyCodec")
```
orders = sc.textFile("/user/cloudera/spark/orders")
orders_map = orders.map(lambda x: (int(x.split(",")[0]),x.split(",")[3]))
orders_map.saveAsTextFile("/user/cloudera/spark/output/orders_map_text")
```
----
### 29. Using save and write to save data in HDFS

**Problem statement: Save the data in json format using save and write**

**Note: Save and write perform similar operations but with different syntax. Can use any one of the following**
```
orders.save("/user/cloudera/spark/json_orders","json")
orders.write.json("/user/cloudera/spark/json_orders")
```
----
### 30. Create a Data frame from RDD and write it to hdfs using save and write as json format.

**Problem statement: Create a rdd of orders, map field[0] and field[3] and save as a DF with id and status as fields. Write the o/p to HDFS**
```
orders = sc.textFile("/user/cloudera/spark/orders")
orders_map = orders.map(lambda x: (int(x.split(",")[0]),x.split(",")[3]))
orders_map_df = orders_map.toDF(schema = ["id","status"])
orders_map_df.show()
orders_map_df.write.json("/user/cloudera/spark/output/json_orders_map_df")
temp = sc.textFile("/user/cloudera/spark/output/json_orders_map_df")
for i in temp.take(10): print i
```
----

   
   
    

