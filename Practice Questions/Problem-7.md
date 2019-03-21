### Problem Scenario 7

Instructions:

Connect to mySQL database using sqoop, import all customers that lives in 'CA' state.

Data Description:

A mysql instance is running on the gateway node.In that instance you will find customers table that contains customers data.

> Installation : on the cluser node gateway 
> Database name:  retail_db
> Table name: Customers
> Username: root
> Password: cloudera



Output Requirement:

Place the customers files in HDFS directory "/user/cloudera/problem1/customers/avrodata"

Use avro format with pipe delimiter and snappy compression.

Load every customer record completely