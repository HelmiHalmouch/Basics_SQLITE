'''
 Main task :
 			- Readsql filein python
 			- Dmonstrate SQL to fetch data 
 			- Select and update data of the SQL table 
'''  
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

def read_all_task(connection):
    # cursor object 
    crsr = connection.cursor() 

    #update the value of age as fucntion of the id 
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

    print("the filtred list by age is :",filtred_list)
    #return filtred_list

# add delete function 

#Delete based on a character 
'''##Delete based on a character 

DELETE FROM employees WHERE job_title IS NULL;
SELECT * FROM employees;'''

def delete_task_by_job(connection, age):

	cur = connection.cursor()
	cur.execute("DELETE FROM lesemployers WHERE age = ?",(age,))

	rows=cur.fetchall()

	for row in rows:
		print(row)


if __name__ =='__main__':


    print("#------------------#")
    delete_task_by_job(connection, age = 63)

    print('The all task in je bdd file are :')
    read_all_task(connection)

    #try the function 

    print('The selction of the employees by a defiend age is :')
    select_task_by_age(connection, age=28)
