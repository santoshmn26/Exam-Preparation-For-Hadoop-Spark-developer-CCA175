### Problem Scenario 2 

There is a parent organization called "Acmeshell Group Inc", which has two child companies named QuickTechie Inc and HadoopExam Inc. 

Both compnaies employee information is given in two separate text file as below. Please do the following activity for employee details.
```
quicktechie.txt
1,Alok,Hyderabad
2,Krish,Hongkong
3,Jyoti,Mumbai
4,Atul,Banglore
5,Ishan,Gurgaon
```
```
hadoopexam.txt
6,John,Newyork
7,alp2004,California
8,tellme,Mumbai
9,Gagan21,Pune
10,Mukesh,Chennai
```
Perform the following:
```
1. Which command will you use to check all the available command line options on HDFS and How will you get the Help for individual command.
2. Create a new Empty Directory named Employee using Command line. And also create an empty file named in it quicktechie.txt 
3. Load both companies Employee data in Employee directory.
4. Merge both the Employees data in a Single file called MergedEmployee.txt, merged files should have new line character at the end of each file content.
5. Upload merged file on HDFS and change the file permission on HDFS merged file , so that owner and group member can read and write, other user can read the file.
6. Write a command to export the individual file as well as entire directory from HDFS to local file System.
```
Solution: 

1. Which command will you use to check all the available command line options on HDFS and How will you get the Help for individual command.
```

```
2. Create a new Empty Directory named Employee using Command line. And also create an empty file named in it quicktechie.txt 
```
mkdir Employee
touch quicktechie.txt
```
3. Load both companies Employee data in Employee directory.
```
cp quicktechie.txt Employee
cp hadoopexam.txt Employee
```
4. Merge both the Employees data in a Single file called MergedEmployee.txt, merged files should have new line character at the end of each file content.
```
cat quicktechie.txt hadoopexam.txt > MergedEmployee.txt
```
5. Upload merged file on HDFS and change the file permission on HDFS merged file , so that owner and group member can read and write, other user can read the file.
```
hadoop fs -put /user/Employee/MergedEmployee.txt /home/output/
```
6. Write a command to export the individual file as well as entire directory from HDFS to local file System.
```
hadoop fs -get /home/output/ /user/Employee/MergedEmployee.txt
```



