### Problem Scenerio 4:
You have been given MySQL DB with following details.
```
user=retail_dba 
password=cloudera 
database=retail_db
table=retail_db.categories
jdbc URL = jdbc:mysql://quickstart:3306/retail_db
```
Please accomplish following activities.
> 1. Import Single table categories(Subset data) to hive managed table , where category_id between 1 and 22 

Solution:
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table categories \
    --hive-import \
    --where "category_id between 1 and 22" 
```

Verify
```
hive
use default;
select * from categories;
```

