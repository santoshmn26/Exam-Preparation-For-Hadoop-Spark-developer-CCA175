### Problem Scenerio 5: 
You have been given following data format file. Each datapoint is separated by '|'.
```
Name|Location1,Location2...Location5|Sex,Age|Father_Name:Number_of_Child
```
Example Record:
> Anupam|Delhi,Mumbai,Chennai|Male,45|Daulat:4

Write a Hive DDL script to create a table named "FamilyHead" which should be capable of holding these data. 

Also note that it should use complex data type e.g. Map, Array,Struct

```
create table FamilyHead(
    name string,
    location array<string>,
    sex_age struct<sex: string, age: int>,
    dicts map<string,int>,
    )
    row format delimited
    fields terminate by "|",
    collection items terminated by ",",
    map keys terminated by ":";
```






