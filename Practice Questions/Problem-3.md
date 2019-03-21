### Problem Scenerio 3: 

You have been given MySQL DB with following details.
```
user=retail_dba 
password=cloudera 
database=retail_db
table=retail_db.categories
jdbc URL = jdbc:mysql://localhost/retail_db
```
Please accomplish following activities.
```
1. Import data from categories table, where catagory=22 (Data should be stored in categories_subset)
2. Import data from categories table, where catagory>22 (Data should be stored in categories_subset_2)
3. Import data from categories table, where catagory  between 1 and 22 (Data should be stored in categories_subset_3)
4. While importing categories data change the delimiter to '|' (Data should be stored in categories_subset_6)
5. Importing data from categories table and restrict the import to category_name,category_id columns only with delimiter as  '|'
6. Add null values in the table using below SQL statement 
ALTER TABLE categories modify category_department_id int(11);
INSERT INTO categories values (60,NULL,'TESTING');
7. Importing data from categories table (In categories_subset_17 directory) using '|' delimiter and category_id between 1 and 61 and encode null values for both string and non string columns.
8. Import entire schema retail_db in a directory categories_subset_all_tables
 ```
 
Solution:
1. Import data from categories table, where catagory=22 (Data should be stored in categories_subset) 
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --query "select * from categories where category_id = 22 and \$CONDITIONS" \
    --split-by category_id \
    --target-dir categories_subset
```
2. Import data from categories table, where catagory>22 (Data should be stored in categories_subset_2) 
 ```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table categories \
    --query "select * from categories where category_id > 22 and \$CONDITIONS" \
    --target-dir categories_subset_2
```
3. Import data from categories table, where catagory  between 1 and 22 (Data should be stored in categories_subset_3)
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table categories \
    --split-by category_id \
    --query "select * from categories where category_id between 1 and 22 and \$CONDITIONS" \
    --target-dir categories_subset_3
```

4. While importing categories data change the delimiter to '|' (Data should be stored in categories_subset_6)
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table categories \
    --split-by category_id \
    --query "select * from categories where catagory between 1 and 22 and /$CONDITIONS" \
    --fields-terminated-by "|" \
    --target-dir categories_subset_6
```
5. Importing data from categories table and restrict the import to category_name,category_id columns only with delimiter as  '|'
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table categories \
    --columns category_name,category_id \ 
    --fields-terminated-by "|"
```
6. Add null values in the table using below SQL statement 
```
ALTER TABLE categories modify category_department_id int(11);
INSERT INTO categories values (60,NULL,'TESTING');
```
7. Importing data from categories table (In categories_subset_17 directory) using '|' delimiter and category_id between 1 and 61 and encode null values for both string and non string columns.
```
sqoop import \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --table categories \
    --fields-terminated-by "|" \
    --where "category_id between 1 and 61" \ 
    --split-by category_id \
    --null-string "N" \
    --null-non-string "N" \
    --target-dir categories_subset_17
```
8. Import entire schema retail_db in a directory categories_subset_all_tables
```
sqoop import-all-tables \
    --connect jdbc:mysql://localhost/retail_db \
    --username root \
    --password cloudera \
    --target-dir categories_subset_all_tables \
    --autoreset-to-one-mapper
```
Optional:
```
ALTER TABLE categories modify category_department_id int(11) NOTNULL;
ALTER TABLE categories modify category_name varchar(45) NOT NULL;
```
