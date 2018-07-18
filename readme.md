# A fake userslist table generater for mysql  
Some times for security reason we want some fake table in our database to trap intruder,in some situation it's maybe the last defence line,no matter you have a trigger to receive alert or just want waste some time to let intruder disappointed on you database,you may want this table be as "real" as we can.

1.You have python2.7 installed  
2.For chinese user,you need  
```
pip install pypinyin
```
for english user,I bet you can comment line in fake_generater.py which function used lib pypinyin.  
3.import table structure ts.sql to your database.  
4.change the database connection information in fake_generater.py  
```
    xsql=sql.connect(host="localhost",user="root",
 	password="123456",db="test",port=3306,charset="utf8")
```
5.execute the script and got print like below.

```
31569
31570
31571
31572
31573
31574
31575
31576
31577
31578
31579
31580
31581
31582
31583
31584
31585
31586
31587
31588
31589
31590
31591
31592
31593
``` 
6.when it's over,check if you got the fake data table.
![data](/1.png)