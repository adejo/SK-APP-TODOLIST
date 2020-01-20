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
        query = """INSERT INTO ISM_KPI.dbo.mytodo (
                        
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
