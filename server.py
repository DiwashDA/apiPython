from flask import Flask, make_response
import oracledb
import json
from flask import jsonify
import dbtest
from flask.wrappers import Response
app = Flask(__name__)

@app.route('/ledger', methods=['GET'])
def recommend_drugs():
    print("executing")
    username = 'IMS7980'
    password = 'IMS7980'
    host = 'localhost'
    port = 1521
    service = 'DIWASHXDB'
    connection =   oracledb.connect(user=username, password=password, host=host, port=port,service_name=service)
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM V$VIRTUAL_SUB_LEDGER where company_code='02'  and sub_code='C1180'")
    return  jsonify(list(data))
    
@app.route('/customers',methods=['GET'])
def getCustomers():
    print("executing")
    username = 'IMS7980'
    password = 'IMS7980'
    host = 'localhost'
    port = 1521
    service = 'DIWASHXDB'
    connection =   oracledb.connect(user=username, password=password, host=host, port=port,service_name=service)
    cursor = connection.cursor()
    data = cursor.execute("SELECT DISTINCT sub_edesc as customer,sub_code as customer_code FROM V$VIRTUAL_SUB_LEDGER")
    columns = [col[0] for col in cursor.description]
    print(columns)
    cursor.rowfactory = lambda *args: dict(zip(columns, args))
    data = cursor.fetchall()
    res = make_response()
    res.status_code = 200
    res.status = "success"
    res.data = {
        "data":data
    }
    return {
        "data":data
    }

if __name__=='__main__':
    app.run(port=8080, debug=True,host="localhost")