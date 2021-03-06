# Sqoop v1.4.6
![alt text](https://github.com/santoshmn26/CCA175-Hadoop-Spark-developer/blob/master/Sqoop/sqoop.png)

Latest available version for sqoop 1 is 1.4.7
Latest available version for sqoop 2 is 1.99.7

**Stable/Most popular version among developers is 1.4.6**

Sqoop is mainly used for automation of importing and exporting data.
----

### Life cycle of sqoop command
### Assume that we are executing the following sqoop command
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table orders
```
### Steps:

1. A SQL query is generated

2. Next step the generated SQL is executed

**Note: The first two steps are performed to understand the data by fetching just one record to access the meta-data information of the columns.**
sample generated query
```
select * from sample_table limit 1
```
Executing the above query returns just 1 record which is sufficient to get the **metadata information about the fields in the source database.**

3. Next a java file is generated, which is a nothing but a map-reduce program.

For each table being imported a .java file is created using the columns metadata.

**Note: The total number of java files generated dependes on the number tables imported.**

4. A Boundry query is generated

**The Boundry query is executed to determine total number of records needs to be imported.**

5. Data split into mutually exclusive records based on Boundry query and num-mappers

**Next the .java file/files are complied to generate the jar file/files.**

6. This jar file is executed to start the import process

**By default 4 mappers are used, i.e 4 threads to import the data from the source**

> In theory More threads = faster the import process but it Causes more load on the source database which is not recomended
----

**Note:**

- \ - line break.
- 3306 default port for access RDBMS can be omitted. 
- Only mappers operations are performed for sqoop. Hence part-m files are generated in the output.

**Note: Number of mappers used = Number of files generated in the output directory.**
```
-   part-m-00000
-   part-m-00001
and so on..
```

**Note: When -m 1 (Only one mapper is used) is used sqoop does not execute its Boundry query, since there is no need to split the data into files.**

**Note: When importing data from multiple columns, there should not be any empty space between the column names supplied**

**Note: When -m 1 is used the data is imported sequentially.**

**Note: While importing data the column passed in split-by must also be imported**

----
| **Sqoop commands list** |
| ------------------- |
| **1. List databases** |
| **2. List tables for a given database** |
| **3. Using sqoop eval** |
| **4. Import table new_table to warehouse-dir** |
| **5. Configure mappers to 2** |
| **6. import data with 2 mappers to warehouse-dir** |
| **7. Using --delete-target-dir command** |
| **8. Append additional imported files to existing dir** |
| **9. Try to run the following import command on a table without a primary key** |
| **10. Use split-by to import data from a table without PK** |
| **11. Use split-by on a non numberic column** |
| **12. Use split-by on a non numberic column and set: -Dorg.apache.sqoop.splitter.allow_text_splitter to True** |
| **13. Import data as sequencefile** |
| **14. Import data as avrodatafile** |
| **15. Import data as textfile** |
| **16. Import data as parquetfile** |
| **17. Import data as text file and compress the data.** |
| **18. Import data as text file and compress the data into SnappyCodec format.** |
| **19. Import data as text file and compress with specific bounding query** |
| **20. Import data from specific columns** |
| **22. Import data from multiple column from a single table** |
| **23. import data from multiple tables and multiple column** |
| **24. Using autoreset-to-one-mapper** |
| **25. Manage NULL values while importing** |
| **26. Change delimiter to ASCII NULL "\000" which is "^@"** |
| **27. Import data of type date using query.** |
| **28. Incremental Imports using query and append** |
| **29. Using where parameter with append** |
| **30. Import data using sqoop's incremental append** |
| **31. Import a table into hive using sqoop** |
| **32. Using hive-overwrite to overwrite existing data in hive tables** |
| **33. Default behaviour of hive import if a table already exists the append the data, copy of part-m files are created** |
| **34. Using hive-create-table.** |
| **35. Using import-all-tables** |
| **36. Simple export** |





----

**Usefull Sqoop commands for CCA175 certification**

| Command | Alias-1 | Alias-2 | Description |
| ------- | ------- | ------- | ----------- |
| sqoop-help | sqoop help | - | List all commands for sqoop |
| version | - | - | Display the version of the sqoop installed |
| username | - | - | Name of the user trying to access data |
| Password | -P | password-file | Password for connecting to the database |
| sqoop-list-database | sqoop list-databases | - | List all the database in source |
| num-mappers | -m | - | Configuring the number of mappers |
| query | -e | - | Query tag |
| compress | -z | - | Enable\Disable compression |
| list-tables | sqoop-list-tables | - | List all the tables in the database |
| import | - | - | import data |
| connect | - | - | Connection string with a jdbc |
| warehouse-dir | - | - | path where the output files needs to be generated |
| target-dir | - | - | path with a new folder name where the o/p files needs to be generated |
| table | - | - | tables to be imported / exported |
| delete-target-dir | - | - | Delete target dir if present |
| as-textfile | - | - | import / export data in textfile format |
| as-avrodata | - | - | import / export data in Binary JSON format |
| as-sequence | - | - | import / export data in Binary format |
| as-parquetfile | - | - | import / export data in Binary Colomnar format |
| split-by | - | - | split the data into multiple files based on a specified colomn |
| colomn | - | - | specify the column to be imported |
| autoreset-to-one-mapper | - | - | resets to one mapper if PK and split-by is not present |
| null-string | - | - | Replace a null value of a type string to a desired value |
| null-non-string | - | - | Replace a null value of a type numeric to a desired value |
| fields-terminated-by | - | - | Change the delimiter |
| lines-terminated-by | - | - | Change the new line character |
| enclosed-by | - | - | Change the enclosing character |
| escaped-by | - | - | Change the escape character |
| optionally-enclosed-by | - | - | Change the enclosing char when the value is same as the delimiter |
| check-column | - | - | Used for incremental append, Column to be verified for the latest value |
| incremental <mode> | - | - | Mode for incremental update of data |
| last-value | - | - | latest value updated/inserted into the HDFS |
| hive-import | - | - | enable import data into hive data store |
| hive-database | - | - | Define the database to which the table needs to be copied |
| hive-table | - | - | Name of the table to be created in HIVE to upload the imported data |    
| hive-overwrite | - | - | Overwrite existing data in hive |
| export-dir | - | - | Location of dir in hdfs with data to be exported |
    



----

**1. List databases**
```
sqoop list-databases \
    -- connect jdbc:mysql//my.server.com:3306     \
    -- username user \
    -- password pass
```

----

**2. List tables for a given database**
```
sqoop list-tables \ 
    -- connect jdbc:mysql//my.server.com:3306/my_database \
    -- username user \
    -P
```

----
    
**3. Using sqoop eval**

eval is used to execute SQL queries.
```
sqoop eval \
    --connect jdbc:mysql//my.server.com:3306/my_database    \
    --username user \
    -P  \
    -e "selet * from orders limit 10"
```

``` 
sqoop eval \
    --connect jdbc:mysql//my.server.com:3306/my_database    \
    --username user \
    -P  \
    --query "insert into order values (100,\"2018-10-31\",100,'adb')"
```
**Note: user need access to write data! Make sure that the user information provided has access to make changes to the DB**

**sqoop eval with DDL command**
```
sqoop eval \
    --connect jdbc:mysql//my.server.com:3306/my_database    \
    --username user \
    -P  \
    -e "create table new_table(i INT)"
```
**Verify creation of table**
```
sqoop eval \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    --password pass \
    --query "select * from new_table limit 5"
```

----

**4. Import table new_table to warehouse-dir**

**Note: Default mappers: 4**

**Note: If target-dir and warehouse-dir not passed then by defalut the imported data is stored in the home path of hdfs. i.e /table_name
--num-mappers or -m decide how many mappers are used for importing data
```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    --password pass \
    --table new_table
    --warehouse-dir /path   \
```

**5. Configure mappers to 2**
```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    --password pass \
    --table new_table
    --warehouse-dir /path   \
    --num-mappers 2
```

```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    --password pass \
    --table new_table
    --warehouse-dir /path   \
    -m 2
```
----
### Difference between target-dir and warehouse-dir:

- --target-dir <dir> HDFS destination dir, No sub directory created all the imported files are imported to specified <dir>
    
- --warehouse-dir <dir> sub dir created with table name and that dir contains data files

- Explanation:

1. If target-dir is used we can specify the name of the output directory under which four part-m files are created
   
   ex: when we use target-dir sqoop/warehouse/output
   
       The output is stored at sqoop/warehouse/output/
       
       Now if we execute hadoop fs -ls sqoop/warehouse/output we get four files
       
       - part-m-00001
       - part-m-00002
       - part-m-00003
       - part-m-00004
       
2. If warehouse-dir is use a sub dir is created with the name of the table under which the the part-m files are created

   ex: when we use warehouse-dir sqoop/warehouse/output
   
   
   **The output files are stored under a newely created dir that with the table name**
   
       i.e sqoop/warehouse/output/table_name
       
       Now to check the output file we need to execute
       
       hadoop fs -ls sqoop/warehouse/output/table_name we get
       
       - part-m-00001
       - part-m-00002
       - part-m-00003
       - part-m-00004       

       table_name is the new dir that is created.


**Note: --delete-target-dir: No additional arguments passed, delete dir if exists**

----

**6. import data with 2 mappers to warehouse-dir**
```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    --password pass \
    --table new_table
    --warehouse-dir /path   \
    -m 2
```  

**7. Execute 6. again to check if we can overwrite output dir**

An error occurs stating target-dir already exists

**to overcome this error use: delete-target-dir**

It deletes the target-dir if exists. Ignores if the dir is not present
```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    --password pass \
    --table new_table
    --warehouse-dir /path   \
    --delete-target-dir     \
    -m 2    
```
**Now it execute without any error even if the dir is alread present**
    
----

**8. Append additional imported files to existing dir**

**Note: This command should not be used with --delete-target-dir**

--append: No additional arguments are needed to be passed
```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    -P
    --warehouse-dir path    \
    --append
```
----

**Using --split-by command**

By default sqoop generate a **Boundry query** and executes it to determine the total number of files present and splits them m (No. of mappers) number of files.
Because all the primary key values defined in a table are **indexed**.

**Drawbacks of following this method:**

1. By default the Boundry query is executed on primary key.
```
    - What if the primary key is not of type INT? (Works when -m 1, because PK is always indexed)
    - What if the table does not contain any primary key? (Works when used --split-by on indexed column)
    - what if the primary key not evenly spaced even though it is of type INT?
```

**9. Try to run the following import command on a table without a primary key**
```
sqoop import \
    --connect jdbc:mysql://localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --table table_no_pk \
    --target-dir sqoop/warehouse/no_pk \
    --as-textfile \
    -z \
    --compression-codec org.apache.hadoop.io.compress.SnappyCodec
```

We get an ERROR! as follows
```
Error during import: No primary key could be found for table table_without_PK. 

Please specify one with --split-by or perform a sequential import with -m 1
```

Note: When -m 1 (Only one mapper is used) is used sqoop does not execute its Boundry query, since there is no need to split the data into files.

When -m 1 is used the data is imported sequentially.

**10. Use split-by to import data from a table without PK**

First create a table without a primary key
execute the following sql
create table table_no_pk ( select * from customers);

Now type **describe table_no_pk** to confirm that there is no PK.
```
sqoop import \
     --connect jdbc:mysql://localhost:3306/retail_db \
     --username root \
     --password cloudera \
     --table table_no_pk \
     --target-dir sqoop/warehouse/no_pk \
     --as-textfile \
     -z \
     --compression-codec org.apache.hadoop.io.compress.SnappyCodec
```
we get error as follows:
**Import failed: No primary key could be found for table table_no_pk. Please specify one with --split-by or perform a sequential import with '-m 1'.** as expected!

To avoid this error use -m 1 as suggested.
```
sqoop import \
     --connect jdbc:mysql://localhost:3306/retail_db \
     --username root \
     --password cloudera \
     --table table_no_pk \
     --target-dir sqoop/warehouse/no_pk \
     --as-textfile \
     -z \
     --compression-codec org.apache.hadoop.io.compress.SnappyCodec \
     -m 1
```

Another method to avoid this error is to use split-by command

**split-by criteria**
```
- Column should be indexed on which split-by is performend. (for performance)
- Values in the fields should be sparse.
- Values in the fields should often be sequential generated or evenly spaced.
- The column should not have null values
```

```
sqoop import \
     --connect jdbc:mysql://localhost:3306/retail_db \
     --username root \
     --password cloudera \
     --table table_no_pk \
     --target-dir sqoop/warehouse/no_pk \
     --as-textfile \
     -z \
     --compression-codec org.apache.hadoop.io.compress.SnappyCodec \
     --split-by customer_id
```
**Now try using split-by on non numeric column**

**11. Use split-by on a non numeric column**
```
sqoop import \
     --connect jdbc:mysql://localhost:3306/retail_db \
     --username root \
     --password cloudera \
     --table table_no_pk \
     --delete-target-dir \
     --target-dir sqoop/warehouse/no_pk \
     --as-textfile \
     -z \
     --compression-codec org.apache.hadoop.io.compress.SnappyCodec \
     --split-by customer_fname
```
sqoop import \
    --connect jdbc:mysq://my.server.com:3306/my_database    \
    --username user     \
    -P      \
    --table table_without_PK    \
    --warehouse-dir <dir>   \
    --split-by first_name

**We get an ERROR! as follows**
```
Caused by: Generating split for a textual index column allowed only in case of "-Dorg.apache.sqoop.splitter.allow_text_splitter=True" 

Property passed as parameter
```

**It's actually hint to use: "-Dorg.apache.sqoop.splitter.allow_text_splitter=True"**

**12. Use split-by on a non numberic column and set: -Dorg.apache.sqoop.splitter.allow_text_splitter to True**
```
sqoop import \
    -Dorg.apache.sqoop.splitter.allow_text_splitter=True    \
    --connect jdbc:mysq://my.server.com:3306/my_database    \
    --username user     \
    -P      \
    --table table_without_PK    \
    --warehouse-dir <dir>   \
    --split-by first_name
```
----

**Importing files in various file formats**

### Popular file types:
| Command | Description |
| ------- | ----------- |
| --as-avrodatafile | Binary JSON format |
| --as-sequencefile | Binary format |
| ***--as-textfile*** | ***Simple text  (Default)*** |
| --as-parquetfile | Binary Columnar file format |

**13. Import data as sequencefile**
```
sqoop import    \
    --connect jdbc:mysql://my.server.com/my_database    \
    --username user     \
    -P      \
    --table orders_table    \
    --warehouse-dir <dir>   \
    --split-by orders   \
    --as-sequencefile
```

**14. Import data as avrodatafile**
```
sqoop import    \
    --connect jdbc:mysql://my.server.com/my_database    \
    --username user     \
    -P      \
    --table orders_table    \
    --warehouse-dir <dir>   \
    --split-by orders   \
    --as-avrodatafile 
```

**15. Import data as textfile**
```
sqoop import    \
    --connect jdbc:mysql://my.server.com/my_database    \
    --username user     \
    -P      \
    --table orders_table    \
    --warehouse-dir <dir>   \
    --split-by orders   \
    --as-textfile
```
  
**16. Import data as parquetfile**
```
sqoop import    \
    --connect jdbc:mysql://my.server.com/my_database    \
    --username user     \
    -P      \
    --table orders_table    \
    --warehouse-dir <dir>   \
    --split-by orders   \
    --as-parquetfile
```

----

**Compressing data**

We compress data due to
```
- Easy IO operation
- Contain/reduce the size of the files
- Reduce the storage requirements of the storage capacity
- Due to replication factor we need 3x of storage space by default
```

Compression enabling 
-z or --compress

**17. Import data as text file and compress the data.**
```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user     \
    -P  \
    --table order_table     \
    --warehouse-dir <dir>   \
    -m 2    \
    --as-textfile   \
    --compress
```
**18. Import data as text file and compress the data into SnappyCodec format.**

```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user     \
    -P  \
    --table order_table     \
    --warehouse-dir <dir>   \
    -m 2    \
    --as-textfile   \
    --compress      \
    --compression-codec org.apache.hadoop.io.compress.SnappyCodec
    
```

**Note: To get all the availabe compression formats navigate to**

**cd etc/hadoop/conf**

**cat core-site.xml**

Search for the line with **codec**
and check to the values\formats enabled

----

**Using  Boundary query**

--Boundary-query used when we want to specify the min and max value specifically

**19. Import data as text file and compress with specific bounding query**

```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user     \
    -P  \
    --table order_table     \
    --warehouse-dir <dir>   \
    -m 2    \
    --as-textfile   \
    --compress      \
    --boundary-query "select min(order_item_id), max(order_item_id) from order_items where order_items_id > 9999"
```

```
sqoop import \
     --connect jdbc:mysql://localhost:3306/retail_db \
     --username root \
     --password cloudera \
     --table orders \
     --delete-target-dir \
     --target-dir sqoop/warehouse/partial_orders \
     --as-textfile \
     -z \
     --compression-codec org.apache.hadoop.io.compress.SnappyCodec \
     --boundary-query "select min(order_id),max(order_id) from orders where order_id >=30000";
```

**Note: Same task can be achieved with the following commands**
```
sqoop import \
     --connect jdbc:mysql://localhost:3306/retail_db \
     --username root \
     --password cloudera \
     --table orders \
     --columns order_id \
     --where "order_id>30000" \
     --delete-target-dir \
     --target-dir sqoop/warehouse/partial_orders \
     --as-textfile \
     -z \
     --compression-codec org.apache.hadoop.io.compress.SnappyCodec 
```

----

**Boundary query for Transformations and Filtering on**

- Column
- Query

We can use --column tag to specify the columns that we need  to import.
we can use --Query tag to filter the data from the table and import the data.

**20. Import data from specific columns**
**Note: When importing data from multiple columns, there should not be any empty space between the column names supplied**

***Invalid syntax: --columns col1, col2, col3***

***Correct syntax: --columns col1,col2,col3***

```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database 
    --username user \
    --password pwd  \
    --warehouse-dir <dir> \
    --columns orders_id,first_name  \
    --compress \
    --num-mappers 2
```

```
sqoop import \
     --connect jdbc:mysql://localhost:3306/retail_db \
     --username root \
     --password cloudera \
     --table orders \
     --columns order_id,order_status \
     --where "order_id>30000" \
     --delete-target-dir \
     --target-dir sqoop/warehouse/partial_orders \
     --as-textfile \
     -z \
     --compression-codec org.apache.hadoop.io.compress.SnappyCodec 
```
----

**Note: Parameters and their uses**

``` 
1. Table: Import entire table 
2. column: Import all rows but perticular column
3. query: Perform any transformation on data
```
The tags column and/or table should not be used along with query.

Table and/or column is mutually exclusive with query.

**22. Import data from multiple column from a single table**

```
sqoop import \
    --connect jdbc:mysql/localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --delete-target-dir \
    --target-dir sqoop/warehouse/column_data \
    --table orders \
    --columns col1,col2,col3 \
    --num-mappers 2 
```

**Note: whenever we use column we must use the table parameter**
```
sqoop import \
    --connect jdbc:mysql://localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --delete-target-dir \
    --target-dir sqoop/warehouse/joing \
    -z \
    --as-textfile \
    --table orders \
    --columns order_id,order_status \
    -m 1
``` 
----
**Note: Even though we have specified only few columns to import, the generated sql imports * to get the metadata about all columns.**

**23. import data from multiple tables and multiple column**

There are two was to achieve this
```
1. Use both table (specify all the table) and column (specify all the columns from the tables)
2. Use a query and perform join operation and pass a split-by tag when m > 1.
```

Using query to perform join operation:

**When we are importing data from multiple table we cannot use warehouse dir, because when we use warehouse-dir a folder which a table name is created
but we are trying to import data from multiple table. There for we need to use target-dir.**

**When we use a query tag we must all pass a \$CONDITION. Which is nothing but a place holder**

```
sqoop import \
    --connect jdbc:mysql/localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --delete-target-dir \
    --target-dir sqoop/warehouse/column_data \
    --query " " \
    --split-by \
    -m 2 \
    --split-by order_id
```
**Note: Either use split-by or use m 1 when query parameter is used**
```
sqoop import \
    --connect jdbc:mysql/localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --delete-target-dir \
    --target-dir \
    -z \
    --as-textfile \
    --query 'select o.order_id, o.order_status, oi.order_item_id from orders o join order_items oi on o.order_id = oi.order_item_id where $CONDITIONS' \
    --split-by order_id
```

----

**24. Using autoreset-to-one-mapper**

This tag will come in handy when are importing data from 100's of table from a database where **some of the table might not have any primary key.**

As we know already, when there is no PK we have to pass a split-by or use -m 1.

Another work around would be to use autoreset-to-one-mapper where the code automatically activates m to 1 when there is no PK.

```
sqoop import \
    --connect jdbc:mysql/localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --delete-target-dir \
    --table table_no_pk \
    --target-dir sqoop/warehouse/column_data \
    --autoreset-to-one-mapper
```
----

**Managing Null values and Delimiters**

**25. Manage NULL values while importing**

```
1. For string values:       --null-string <null-string>
2. For non-string values:   --null-non-string <null-string>
```

```
sqoop import \
    --connect jdbc:mysql/localhost/retail_db \
    --username root \
    --password cloudera \
    --table orders \
    --warehouse-dir sqoop/warehouse/tab_terminated_data \
    --null-non-string -1 \
    --null-string "empty" \
    --fields-terminated-by "\t" \
    --lines-terminated-by "\n" \
    --m 2
```

**26. Change delimiter to ASCII NULL "\000" which is "^@"***
```
sqoop import \
    --connect jdbc:mysql/localhost/retail_db \
    --username root \
    --password cloudera \
    --table orders \
    --warehouse-dir sqoop/warehouse/tab_terminated_data \
    --null-non-string -1 \
    --null-string "empty" \
    --fields-terminated-by "\000" \
    --lines-terminated-by "\n" \
    --m 2
```
----

**27. Import data of type date using query**

**NEEDS UPDATE**

----
 **Incremental Imports**
 
**28. Incremental Imports using query and append**

**First load all the data for the year 2013**

**It is pointless to use delete-target-dir with append**

```
sqoop import \
    --connect jdbc:mysql://localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --target-dir sqoop/warehouse/append \
    -z \
    --as-textfile \
    --query "select order_date from orders where order_date like '2013-%' and \$CONDITIONS' \
    -m 1
```
**Now assume that there is a new data added to the source database with the year 2014. By using --append we can append the new data to the old files.**
```
sqoop import \
    --connect jdbc:mysql://localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --target-dir sqoop/warehouse/append \
    --append \
    -z \
    --as-textfile \
    --query "select order_date from orders where order_date like '2013-%' and \$CONDITIONS' \
    -m 1
```
**Using query and split-by is not recomended for loading data frequently or large amount of data on of the work around method is to use where parameter.**

**29. Using where parameter with append**
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table orders \
    --column orders_data \
    --where "orders_date like '2013%'" \
    -z \
    --as-textfile \
    -m 1
```
**While performing data import for appending, there are few Problems with using where or query parameters**

- We need to keep track of the latest imported rows in the destination.
- We need to keep track of the latest rows updated in the source database.
- To perform the above two operation we need to perform eval before and after importing data from the source.

**To overcome all the above problems we can use:**
```
1. check-column
2. Incremental
3. last-value
```
**30. Import data using sqoop's incremental append**

**Example: Let us first import order data for the year 2013**
```
sqoop import \
    --connect jdbc:mysql://localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --target-dir sqoop/warehouse/append \
    --append \
    -z \
    --as-textfile \
    --query "select order_id, order_date from orders where order_date like '2013-%' and \$CONDITIONS' \
    --split-by order_id
```
**Run the following command to check the latest value in the hdfs for orders table**
```
hadoop fs -cat /sqoop/warehouse/append/part-m-00003 | tail 
```
**Now copy the latest value with the latest date.**

**Now assume the data at the source database orders has increased with data for 2014, let us use sqoop's incremental append to upload the new data into HDFS.**

**Paste the latest value copied to the last-value parameter.**
```
sqoop import \
    --connect jdbc:mysql://localhost:3306/retail_db \
    --username root \
    --password cloudera \
    --target-dir sqoop/warehouse/append \
    --table orders \
    --columns order_id,order_date \
    --check-column order_date \
    --incremental append \
    --last-value "2013-10-31"
```

----

## HIVE and SQOOP

**Importing data into hive using sqoop**

**31. Import a table into hive using sqoop**
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table order_items \
    --hive-import \
    --hive-database retail_db \
    --hive-table hive_order_items \
    --num-mappers 2
```
**Note: --hive-table is optional, if the paramater is not passed a by default the table's original name from the source is used to create the table in the hive database**

**Note: --hive-database is also optional we can directly pass hive-table retail_db.order_items**

**Note if we --hive-database is not provided and the database name is not provided in --hive-table then the data is loaded into the default database in hive that is 'default'**

**Note: If the database name is not passed by defalut the data is uploaded to the default database in hive.**

**Three senarios that can happen during hive import**
```
1. Table that we are trying to import already exists in HIVE.
When we try and import the table again, we do not get any error, the import will run successfully and create more part-m-files in the same directory.
2. We know that the table already exists so we use --hive-overwrite to overwrite the existing data in the hive instead of making copies
When we pass the parameter --hive-overwrite the table in the hive is dropped and recreated so are the files in the HDFS.
3. We know that the table already exists so, we try to append new data into the hive table
```

**For senario 2**

**32. Using hive-overwrite to overwrite existing data in hive tables**
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table order_items \
    --hive-import \
    --hive-database retail_db \
    --hive-table hive_order_items \ 
    --hive-overwrite \
    --num-mappers 2
```
**For senario 1**

**33. Default behaviour of hive import if a table already exists the append the data, copy of part-m files are created**

```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table order_items \
    --hive-import \
    --hive-database retail_db \
    --hive-table hive_order_items \
    --num-mappers 2
```

**For senario 3**

**Note: hive-create-table and hive-overwwite are mutually exclusive, Not recommended to use both**

**Note: hive-create-table does not work as the name suggest.**

**It throws an exception or fail if the target table already exists**
Even before failing the data from the source is loaded into a staging table in hdfs default user location.

So, if the job fails there is still data present in hdfs which we may have to handle.

**34. Using hive-create-table. ***

```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table order_items \
    --hive-import \
    --hive-create-table \
    --hive-database retail_db \
    --hive-table hive_order_items \
    --num-mappers 2
```

**Hive import-all tables**

**Note: when we use import-all-tables we cannot use the following. i.e we cannot perform any transformation on the data.**
```
1. --query
2. --table
3. --where
4. --target-dir
5. --columns
```

**35. Using import-all-tables**

**Note: Passing --hive-import is mandatory or all the data is just loaded into hdfs and not in hive table**

**Note: To confirm that the data is loaded into HIVE and not just in hdfs, view the content of part-m files in hdfs, the delimited should be '^@' and not ','.**

**Note: If a warehouse-dir not passed during import then the default /user/hive/warehouse/ stored all the imported tables. To verify the default hive/warehouse location if changed in conf files go to hive and type**

> describe formated table_name 

To get additional information about the table scroll down to find the Location column copy the path and verify by 

> hadoop fs -ls copied_path.

**Recommended to use --autoreset-to-one-mapper **
```
sqoop import-all-tables \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --autoreset-to-one-mapper \
    --hive-import
```

----

## Sqoop Export

**While exporting make sure that the target database has write permission to the user to write the data from hdfs to target database.** 

**Note: While importing data from mysql to hive if the table does not exist in the hive a new table is created with the name obtained from the target dir. We do not get any error**

**Note: The same does not apply the other way around. While importing data from hdfs to target (mysql) if a table does not exist in the traget (mysql) we get an error as table not found.**

## Steps to follow during import:

> First step during export make sure that a table exist in the target database.
> Make sure that the user has access to write data into the targe database.
> Data stored in hdfs is noting but a directory, similar to data stored in hive so, while exporting we need to provide the export-dir

**36. Simple export**

**Note: The table name orders provided by --table refers to the table name in the target dir and not in the source dir. In the source we do not have a table we have a dir.**

**Note: When we export data from hive to target dir remember that the delimited should match between the source and target and the default demilited for hive is "\001" which is the ascii code for '^@'**


```
sqoop export \
    --connect jdbc:mysql://localhost/retail_export \
    --username root \
    --password cloudera \
    --table ordres \
    --export-dir /user/hive/warehouse/orders \
    --fields-terminated-by "\001" \
    --lines-terminated-by "\n"
```

## Life cycle of Export

> Similary to import, during export the first step is to get the meta data. 

This is achieved by generating and executing a SQL to retrive just 1 record from the target database.

> Once the SQL is executed jar files are generated. 

The number of jar files generated depends on the number of tables being exported similar to the import process.

> Service address created

A service link is generated to track the import process.

These jar files are injected into sqoop to start the export process

> NO BOUNDRY QUERY IS GENERATED!. But insted the sqoop uses hadoop internal block sizes to determine how to split the data between number of mappers.


## Export column mapping.

!!Update last 3










