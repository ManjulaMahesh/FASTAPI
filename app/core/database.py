import pyodbc

servername = 'LAPTOP-35KK1PBI\SQLEXPRESS'
database = 'Training'
username = 'sa'
password = 'password-1'
driver = '{ODBC Driver 17 for SQL Server}'


def get_connection():
    conn = pyodbc.connect(  
     f'DRIVER={driver};SERVER={servername};DATABASE={database};UID={username};PWD={password}')
    return conn

