'''
 Main task :
 			- Readsql filein python
 			- Dmonstrate SQL to fetch data 
 			- Select and update data of the SQL table 
'''  
  
# importing the module 
import sqlite3 
  
# connect withe the myTable database 
connection = sqlite3.connect("sample.db") 
  
# cursor object 
crsr = connection.cursor() 

#update the vaue of age as fucntion of the id 
crsr.execute("UPDATE lesemployers SET age = 30 WHERE id =1")
  
# execute the command to fetch all the data from the table emp 
#SELECT * FROM employees;
crsr.execute("SELECT * FROM lesemployers")  
  
# store all the fetched data in the ans variable 
ans= crsr.fetchall()  
  
# loop to print all the data 
for i in ans: 
    print(i) 


def select_task_by_age(connection, age):
    """
    Query tasks by age
    :param conn: the Connection object
    :param age:
    :return:
    """
    cur = connection.cursor()
    cur.execute("SELECT * FROM lesemployers WHERE age=?", (age,))
 
    rows = cur.fetchall()

    filtred_list = []
    for row in rows:
        print(row)
        filtred_list.append(row)

    print("he filtred list by age is :",filtred_list)
    #return filtred_list
 
#try 
print('The selction of the employees by a defiend age is :')
select_task_by_age(connection, age=28)