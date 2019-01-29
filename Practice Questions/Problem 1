# Problem Scenario 1

## Problem 1:
    - Using sqoop, import orders table into hdfs to folders /user/cloudera/problem1/orders. File should be loaded as Avro File and use snappy compression

    - Using sqoop, import order_items  table into hdfs to folders /user/cloudera/problem1/order-items. Files should be loaded as avro file and use snappy compression

    - Using Spark Scala load data at /user/cloudera/problem1/orders and /user/cloudera/problem1/orders-items items as dataframes. 

    - Expected Intermediate Result: Order_Date , Order_status, total_orders, total_amount. In plain english, please find total orders and total amount per status per day. The result should be sorted by order date in descending, order 	status in ascending and total amount in descending and total orders in ascending. Aggregation should be done using below methods.
      However, sorting can be done using a dataframe or RDD. Perform aggregation in each of the following ways

        a). Just by using Data Frames API - here order_date should be YYYY-MM-DD format
        b). Using Spark SQL  - here order_date should be YYYY-MM-DD format
        c). By using combineByKey function on RDDS -- No need of formatting order_date or total_amount

     - Store the result as parquet file into hdfs using gzip compression under folder
```
        /user/cloudera/problem1/result4a-gzip
        /user/cloudera/problem1/result4b-gzip
        /user/cloudera/problem1/result4c-gzip
```
     - Store the result as parquet file into hdfs using snappy compression under folder
```
        /user/cloudera/problem1/result4a-snappy
        /user/cloudera/problem1/result4b-snappy
        /user/cloudera/problem1/result4c-snappy
```
    - Store the result as CSV file into hdfs using No compression under folder
```
        /user/cloudera/problem1/result4a-csv
        /user/cloudera/problem1/result4b-csv
        /user/cloudera/problem1/result4c-csv
```
    - Create a mysql table named result and load data from /user/cloudera/problem1/result4a-csv to mysql table named result 

### Solution

### 1. Using sqoop, import orders table into hdfs to folders /user/cloudera/problem1/orders. File should be loaded as Avro File and use snappy compression

First make sure that the directories exists /user/cloudera/problem1/orders.
```
hadoop fs -ls /user/cloudera/problem1/orders/
```
If you get response that the path does not exists then create a new directory
```
hadoop fs -mkdir /user/cloudera/problem1/
```

Now the folder is created start importing using sqoop
```
sqoop import --connect "jdbc:mysql://localhost/retail_db" --username root --password cloudera --table orders --target-dir /user/cloudera/problem1/orders -z --compression-codec org.apache.hadoop.io.compress.SnappyCodec --as-avrodatafile
```
Confirm with checking the path in hdfs
```
hadoop fs -ls /user/cloudera/problem1/orders/
```
----
### 2. Using sqoop, import order_items  table into hdfs to folders /user/cloudera/problem1/order-items. Files should be loaded as avro file and use snappy compression

First make sure that the directories exists /user/cloudera/problem1/order_items.
```
hadoop fs -ls /user/cloudera/problem1/order_items/
```
If you get response that the path does not exists then create a new directory
```
hadoop fs -mkdir /user/cloudera/problem1/
```

Now the folder is created start importing using sqoop
```
sqoop import --connect "jdbc:mysql://localhost/retail_db" --username root --password cloudera --table orders --target-dir /user/cloudera/problem1/order_items -z --compression-codec org.apache.hadoop.io.compress.SnappyCodec --as-avrodatafile
```
Confirm with checking the path in hdfs
```
hadoop fs -ls /user/cloudera/problem1/order_items/
----
### 3. Using Spark Scala load data at /user/cloudera/problem1/orders and /user/cloudera/problem1/orders-items items as dataframes. 

Launch Pyspark
***Important: Make sure that you load the data as df or csv for easy processing of data. Using "com/databricks.spark.avro" loads the data as df***
```
orders = sqlContext.read.format("com.databricks.spark.avro").load("/user/cloudera/problem1/orders/")
order_items = sqlContext.read.format("com.databricks.spark.avro").load("/user/cloudera/problem1/orders/")
```
***Converting DF to RDD***

```
orders_rdd = orders.rdd.map(list)
order_items_rdd = order_items.map(list)
```

