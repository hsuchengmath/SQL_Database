
import mysql.connector
import pandas as pd
from tqdm import tqdm

profile = {'host':'localhost','user':'hsucheng','password':'hsucheng'}



mysql_connection = mysql.connector.connect(
    host = profile['host'],
    user = profile['user'],
    password = profile['password'])

cursor = mysql_connection.cursor()
cursor.execute('use testDB')


# load data
df = pd.read_csv('train')
feature = list(df.columns)


batch_container, batch_size = [],10024
basic_query = 'INSERT INTO Avazu' \
              + ' VALUES '\
              + '(' + ','.join(["%s" for _ in range(len(feature)) ]) + ')' 
index = 0
for row in tqdm(df.itertuples(index=False),total=df.shape[0]):
    # collect data and transfoerm into tuple format
    value = tuple(row)
    value = (index,) + value[1:]
    batch_container.append(value)
    # if achieve batch, then I/O into DB.
    if (index+1) % batch_size == 0:
        cursor.executemany(basic_query ,batch_container)
        mysql_connection.commit()
        batch_container = []
    index +=1



#cursor = mysql_connection.cursor()
#cursor.execute('use Avazu')
#cursor.execute('select * from student')
#values = cursor.fetchall()


# cursor = mysql_connection.cursor()
# sql = "INSERT INTO student VALUES (%s, %s, %s)"
# val = [
#     (1, 'boom', 'Taoyuan'),
#     (2, 'banh', 'Tainan'),
#     (3, 'champion', 'New Taipei'),
# ]

# cursor = mysql_connection.cursor()
# cursor.execute('use testDB')
# for student in val:
#     cursor.execute(sql, student)

# mysql_connection.commit()
