# Adding a new column to a Dataframe in pyspark
```
from pyspark.sql.functions import lit
data_with_new_col = ori_data.withColumn("new_col_name", lit("common value for all row in new col"))
```

# Changing the column name in a DataFrame in pyspark
```
from pyspark.sql.functions import col
data = res.select(col('ori_col_name').alias("new col name"))
```

# Drop a column in a DataFrame in pyspark
```
from pyspark.sql.functions import col
data = res.drop(col,col1,col2)
or
cols = [col, col1]
data = res.drop(cols)
```

# Combining two dataframes
```
DF1 = spark.read.csv()
DF2 = spark.read.csv()
# Note DF1 and DF2 should have same schema
Combined_DF = DF1.union(DF2)
data = res.select(col('ori_col_name').alias("new col name"))
```

# Dataframe Show more than 20 rows
```
DF.show(30, false)
```

# Using where in a Dataframe
```
df.filter(df.age > 3).collect()
```

# DF read with header
```
df = spark.read.option('header',True).csv(file_path)
df.show() # displays the first row as header
```

# Get Distinct values of a column from a DF
```
distinct_values = df.select('col').distinct()
```

# Replace Null values in a DF
```
# replace 'null' with 'NA'
null_replaced_df = df_with_null.na.fill('NA')
# replace 'null' with ''
null_replaced_df = df_with_null.na.fill('')
# replace 'null' with 0
null_replaced_df = df_with_null.na.fill(0)
```


# Filter DF if the col contains a string
```
from pyspark.sql import col
filtered_data = df.filter(col('col_name').contains('some_string'))
filtered_data.show()
```














