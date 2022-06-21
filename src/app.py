import mysql.connector
import http.client
import time

mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  password="root",
  database="scrapper"
)

conn = http.client.HTTPConnection("receitaws.com.br")
headers = { 'Content-Type': "application/json" }

cnpj = '''00013099000166'''

list = cnpj.rsplit("\n")

for item in list:
    conn.request("GET", "/v1/cnpj/" + item, headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    time.sleep(21)
