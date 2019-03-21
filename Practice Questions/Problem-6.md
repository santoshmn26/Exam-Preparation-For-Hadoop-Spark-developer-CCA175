### Problem Scenario 6
You have been given following data format file. Each datapoint is separated by '|'.
```
Name|Sex|Age|Father_Name
Example Record
Anupam|Male|45|Daulat
```
Create an Hive database named "Family" with following details. 

You must take care that if database is already exist it should not be created again.
```
Comment : "This database will be used for collecting various family data and their daily habits"
Data File Location : '/hdfs/family'
Stored other properties : "'Database creator'='Vedic'" , "'Database_Created_On'='2016-01-01'"
Also write a command to check, whether database has been created or not, with new properties.
```
**Syntax:**

>CREATE (DATABASE|SCHEMA) [IF NOT EXISTS] database_name[COMMENT 'database_comment'][LOCATION hdfs_path];

```
create database IF NOT EXISTS Family 
COMMENT "This database will be used for collecting various family data and their daily habits"
LOCATION "/hdfs/family"
WITH DBPROPERTIES("database creator" = "Vedic", "Database_Created_On" = "2016-01-01");
```

**Verify:**
```
show databases;
describe database extended Family;

family	
This database will be used for collecting various family data and their daily habits	
hdfs://quickstart.cloudera:8020/hdfs/family	
cloudera	USER	{database creator=Vedic, Database_Created_On=2016-01-01}
Time taken: 0.182 seconds, Fetched: 1 row(s)
```

