import mysql.connector
import configparser
import os

config = configparser.ConfigParser()
# properties.ini is in the parent directory of pages/
properties_file_path = os.path.join(os.path.dirname(__file__), '..', 'properties.ini')
config.read(properties_file_path)

db_config = config['SQL']
api_config = config['API']
url = api_config['endpoint']
print(url)

conn = mysql.connector.connect(
    host=db_config['host'],
    database=db_config['database'],
    user=db_config['user'],
    password=db_config['password']
)

print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('SELECT * FROM OrderInfo')

row = cursor.fetchone()
print(row)
if row:
    print(row[3])

row_all = cursor.fetchall()
print(row_all)

print(conn.is_connected())                                                 
cursor = conn.cursor()                                                     
cursor.execute('SELECT * FROM CustomerInfo')                               
row = cursor.fetchone()                                                    
print(row)                                                                 
print(row[3])                                                              
row_all = cursor.fetchall()                                                
print(row_all)                                                             
summation = 0                                                              

for rows in row_all:                                                       
    summation += row[3]                                                    
    print(summation)  
    if summation == 33:
        print("Assertion passed") 
    else:
        print("Assertion failed")                                                  
try:                                                                       
    # Update name where age is 35                                          
    update_query = "UPDATE CustomerInfo SET Name = %s WHERE Age = %s"      
    update_data = ("Sachin Nimbalkar", "35")                               
    cursor.execute(update_query, update_data)                              
                                                                           
    # Delete customer with ID 3                                            
    delete_query = "DELETE FROM CustomerInfo WHERE CustomerID = %s"        
    delete_data = ("3",)                                                   
    cursor.execute(delete_query, delete_data)                              
                                                                           
    # Commit once after all operations                                     
    conn.commit()                                                          
                                                                           
except Exception as e:                                                     
    conn.rollback()                                                        
    print("Transaction failed:", e)                                        
                                                                           
finally:                                                                   
    conn.close()                                                           
conn.close()