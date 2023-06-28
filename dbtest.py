import oracledb
import os

oracledb.init_oracle_client(lib_dir=r"C:\Users\adhee\OneDrive\Documents\oracle_client\instantclient_21_10")


username = 'IMS7980'
password = 'IMS7980'
host = 'localhost'
port = 1521
service = 'DIWASHXDB'


un = os.environ.get('PYTHON_USERNAME')
pw = os.environ.get('PYTHON_PASSWORD')
cs = os.environ.get('PYTHON_CONNECTSTRING')


print(un)
print(pw)
print(cs)

connection =   oracledb.connect(user=username, password=password, host=host, port=port,service_name=service)
cursor = connection.cursor()
data = cursor.execute("SELECT * FROM V$VIRTUAL_SUB_LEDGER where company_code='02'  and sub_code='C1180'")
print("Cursor executed")
rows = data.fetchall()
print(rows)
for d in rows:
    print("data")
    print(d)