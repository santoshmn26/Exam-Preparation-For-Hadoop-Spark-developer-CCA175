## Common issues in spark-sql

### Note: .persist() .cache() is not an action!
### Note: .head() method should only be used if the resulting array is expected to be small, since as all the data is loaded into the driver’s memory.

#### :set tabstop=4                                                                                                                                                

### Running hive queries using spark

### Spark-SQL vs DF vs RDD
```
stackoverflow: https://stackoverflow.com/questions/45430816/writing-sql-vs-using-dataframe-apis-in-spark-sql
RDD is always faster for most types of Data processing.
Most of the time Spark-sql and DF performance are consistant with each other.
```

```
spark = SparkSession.builder.getOrCreate()
query = "Select * from dummy_table"

### Note this is not an action so, spark does not execute this statement as long as you don't perform any action on it.
query_res = spark.sql(query)

### Action on the dataframe

query_res.show()
```
### Adding a new column to a Dataframe in pyspark
```
from pyspark.sql.functions import lit
data_with_new_col = ori_data.withColumn("new_col_name", lit("common value for all row in new col"))
example: 
### select null as new_col_name
data_with_new_col = ori_data.withColumn("new_col_name", list(None))
```

### Changing the column name in a DataFrame in pyspark
```
from pyspark.sql.functions import col
data = res.select(col('ori_col_name').alias("new col name"))
or
data = res.select((data.ori_col_name).alias("new_col_name"))
or
data = res.withColumnRenamed("count","distinct_name")
```

### Drop a column in a DataFrame in pyspark
```
from pyspark.sql.functions import col
data = res.drop(col,col1,col2)
or
cols = [col, col1]
data = res.drop(cols)
```

### Combining two dataframes
```
DF1 = spark.read.csv()
DF2 = spark.read.csv()
### Note DF1 and DF2 should have same schema
Combined_DF = DF1.union(DF2)
data = res.select(col('ori_col_name').alias("new col name"))
```

### Dataframe Show more than 20 rows
```
DF.show(30, false)
```

### Using where in a Dataframe
```
df.filter(df.age > 3).collect()
```

### DF read with header
```
df = spark.read.option('header',True).csv(file_path)
df.show() # displays the first row as header
```

### Get Distinct values of a column from a DF
```
distinct_values = df.select('col').distinct()
or 
from pyspark.sql import functions as F
distinct_values = df.agg(F.countDistinct(df.col_name))
```

### Replace Null values in a DF
```
# replace 'null' with 'NA'
null_replaced_df = df_with_null.na.fill('NA')
# replace 'null' with ''
null_replaced_df = df_with_null.na.fill('')
# replace 'null' with 0
null_replaced_df = df_with_null.na.fill(0)
```


### Filter DF if the col contains a string
```
from pyspark.sql import col
filtered_data = df.filter(col('col_name').contains('some_string'))
filtered_data.show()
```


### Adding a string to a col value 
```
from pyspark.sql.functions import concat
### Create a new col
res = data.withColumn('new_col', col("existing_col") + col("string_to_add"))

### select from an existing col
res = data.select(col("existing_col") + col("string_to_add")).alias("col_name")
```

### Read textfile with custom delimiter
```
data = spark.read.option('delimiter', "|").csv("path")
```

### Filter out df is a column contains a substring
```
data = df.filter(~col('col_name').contains('tmp_string'))
```


### Multiple join condition between two DF
```
df1 = spark.sql("select * from table_1")
df2 = spark.sql("select * from table_2")

join_df = df1.join(df2, [ df1.col_1 == df2.col1, df1.col_2 == df2.col_2 ], 'left')
```

### Multiple where conditions in a DF
```
df1 = spark.sql("select * from table_1")
df2 = spark.sql("select * from table_2")

join_df = df1.join(df2, [ df1.col_1 == df2.col1, df1.col_2 == df2.col_2 ], 'left'). \
              where((df1.col_1 == 'tmp') & (df2.col_2 == 'tmp'))
```

### Decimal value limit decimal points
```
from pyspark.sql import functions as F
df = df.withColumn('col_with_decimal_value', F.round(df.m_revenue,2))
```


### When reading from multiple partitions get the source location for a each record
```
Ex: 
data  = spark.read.parquet("data/01/","data/02/")
Here 01 and 02 are partitions whose value will be missing in data.columns
to get those values for each record
from  pyspark.sql.functions import input_file_name
res = data.withColumn("partition_value", input_file_name)

Or

basepath = "/data/"
partition_read_path = "/data/01/"
data = spark.read.option("basePath",basepath).parquet(partition_read_path)
partition_read_path.show() will contain the partition value too.
```

### Casting column in DF
```
from pyspark.sql.functions import col
data = ori_data.withColumn('col_1',col(col_1).cast('int')).alias('new_int_col')
```

### Adding new columns using UDF
### Note: UDF's are not recommended in spark they are slower compared to spark's inbuilt api functions
### Therefore always try to avoid UDF's in spark process.
```
from pyspark.sql import udf
from pyspark.sql.types import *
from pyspark.sql.functions import lit

# Define a function
udf_function(data):
	return(data*0.1)

# Define the UDF
udf_function = udf(udf_function, FloatType())
			   # Function_name, return_type

# new_df
new_df = ori_df.withColumn('new_col', udf_function(lit(ori_df.col_1))

```


### Spark read with custom schema

```
from pyspark.sql.types import *  #(StructType, StringType, IntegerType)
columns = ([StructField('col_string',StringType()),
			StructField('col_int',IntegerType())
		   ]
		  )
		  
custom_schema = StructType(fields = schema)

data = spark.read.format('csv').options('sep', '/x100').load(path,schema = custome_schema)
```
