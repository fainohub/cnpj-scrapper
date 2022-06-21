import mysql.connector
import http.client
import time

mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  password="root",
  database="scrapper"
)

mycursor = mydb.cursor()
mycursor.execute('''CREATE TABLE IF NOT EXISTS cnpj (
                    id BIGINT auto_increment NOT NULL,
                  	cnpj varchar(100) NULL,
                  	status varchar(100) NULL,
                  	situacao varchar(100) NULL,
                  	data_situacao varchar(100) NULL,
                  	tipo varchar(100) NULL,
                  	nome varchar(300) NULL,
                  	porte varchar(100) NULL,
                  	data_abertura varchar(100) NULL,
                  	natureza_juridica varchar(100) NULL,
                  	atividade_principal varchar(200) NULL,
                  	atividade_principal_codigo varchar(100) NULL,
                  	PRIMARY KEY (id)
                  )''')

sql = "INSERT INTO cnpj (cnpj, status) VALUES (%s, %s)"
val = ("00013099000166", "pendente")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")