import requests
import pyodbc


def mysql_con():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=databaseserver;'
                      'Database=mytodo;'
                      'Trusted_Connection=yes;')

    return conn


def add_to_do(msdata):
        conn = mysql_con()
        corsor = conn.cursor()
        query = """INSERT INTO mytodo.dbo.mytodo (
                        
                        [todo_name],
                        [date],
                        [desc],
                        
                        ) values"""


        try:
            corsor.execute(query + str(msdata))
            corsor.close()
            conn.commit()
            return True
        except Exception as e:
            return str(e)
        
def Read_todo(date_):
    conn = mysql_con()
    cursor = conn.cursor()
    cursor.execute("select *  FROM mytodo)
    # fetch all of the rows from the query
    data = cursor.fetchall()
    # create a list with dictionary of rows
    data_set = []
    for row in data:
        data = {
            "Date_": row[0],
            "Threat_type": row[1],
            "Threat_name": row[2],
        }
        data_set.append(data)
    return data_set
