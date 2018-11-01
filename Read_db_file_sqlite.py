'''
 Main task :
 			- Readsql filein python
 			- Dmonstrate SQL to fetch data 
 			- Select and update data of the SQL table 
'''  
# importing the module 
import sqlite3 
 
# connect withe the myTable database 
connection = sqlite3.connect("sampleTable.db") 

# cursor object 
crsr = connection.cursor() 
  
# execute the command to fetch all the data from the table emp 
crsr.execute("SELECT * FROM lesemplyers")  
  
# store all the fetched data in the ans variable 
ans= crsr.fetchall()  
  
# loop to print all the data 
for i in ans: 
    print(i) 

