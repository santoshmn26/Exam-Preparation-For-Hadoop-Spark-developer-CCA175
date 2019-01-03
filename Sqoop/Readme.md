# Sqoop v1.4.6

Latest available version 2

**Popular version among developers 1.4.6**

Sqoop is mainly used for automation of importing and exporting data.
----

### Life cycle of sqoop command

**In the first step, a SQL query is generated and execute to understand the data by fetching just one record to access the meta-data information of the columns.**
sample query
```
select * from sample_table limit 1
```
**Next a java file is generated, which is a map-reduce.**
For each table being imported a .java file is created using the columns metadata.

**Next the .java file/files are complied to generate the jar file/files.**
This jar file is executed to start the import process

**The Boundry query is executed to determine total number of records.**
Data split into mutually exclusive records based on Boundry query and num-mappers

**By default 4 mappers are used, i.e 4 threads to import the data from the source**
> More threads = faster the import process = Causes more load on the source database

----

**Note:**

- \ - line break
- 3306 default port for access RDBMS can be omitted 

**Note: Number of mappers used = Number of files generated.**

**Note: When -m 1 (Only one mapper is used) is used sqoop does not execute its Boundry query, since there is no need to split the data into files.**

**Note: When -m 1 is used the data is imported sequentially.**

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
| **21. Import data from multiple tables and specific columns** |
| **21. Import data from multiple tables and specific columns** |
----

Alias for tags

| Command | Alias-1 | Alias-2 | Description |
| ------- | ------- | ------- | ----------- |
| sqoop-help | sqoop help | - | List all commands for sqoop |
| version | - | - | Display the version of the sqoop installed |
| --Password | -P | --password-file | Password for connecting to the database |
| sqoop-list-database | sqoop list-databases | - | List all the database in source |
| --num-mappers | -m | - | Configuring the number of mappers |
| --query | -e | - | Query tag |
| -z | --compress | - | Enable\Disable compression |

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
**Note: user need access to write data!**

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

- In simple terms:
1. If target-dir is used we can specify the name of the output directory under which four part-m files are created
   ex: when we use target-dir sqoop/warehouse/output
       **The output is stored at sqoop/warehouse/output/**
       Now if we execute **hadoop fs -ls sqoop/warehouse/output** we get four files
       part-m-00001
       part-m-00002
       part-m-00003
       part-m-00004
2. If warehouse-dir is use a sub dir is created with the name of the table under which the the part-m files are created
   ex: when we use warehouse-dir sqoop/warehouse/output
       **The output files are stored under a newely created dir that with the table name
       i.e **sqoop/warehouse/output/table_name**
       Now to check the output file we need to execute
       **hadoop fs -ls sqoop/warehouse/output/table_name** we get
       part-m-00001
       part-m-00002
       part-m-00003
       part-m-00004       
       **table_name is the new dir that is created.**


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

**to over come this error use: delete-target-dir**

It deletes the target-dir if exists. Ignores if the dir is not present**
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

sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database   \
    --username user \
    -P
    --warehouse-dir path    \
    --append

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

**9. Try to run the followin import command on a table without a primary key**
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

**It's actually hint to use: "-Dorg.apache.sqoop.splitter.allow_text_splitter=True" **

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
| --as-textfile | Simple text  (Default) |
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

**cd etc/hadoop/conf

cat core-site.xml**

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

- column
- Query

We can use --column tag to specify the columns that we need  to import.
we can use --Query tag to filter the data from the table and import the data.

**20. Import data from specific columns**

```
sqoop import \
    --connect jdbc:mysql://my.server.com:3306/my_database 
    --username user \
    --password pwd  \
    --warehouse-dir <dir> \
    --columns orders_id, first_name  \
    --compress \
    --num-mappers 2
```

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
**21. Import data from multiple tables and specific columns**

**Note: When using --query tag:**
- We cannot use --table
- We cannot use --column
- we have to use --split-by or use num-mappers only 1




