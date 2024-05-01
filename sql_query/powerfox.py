import pyodbc

"""
    pip install pyodbc 
    brew install unixodbc 
    brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
    brew update
    brew install msodbcsql mssql-tools
"""


DRIVER = '{ODBC Driver 17 for SQL Server}'
SERVER = 'pfox-omega-de-sqlserver.database.windows.net,1433'
DATABASE = 'pfox-db-prod'
USERNAME = 'qateam'
PASSWORD = '9i@I40LY3Gwa'

connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()
cursor.execute("""SELECT * FROM Customers
                WHERE customer_id BETWEEN 11760 AND 11770""")
result = cursor.fetchall()

columns = [description[0] for description in cursor.description]
print(columns)

for raw in result:
    print(raw)


