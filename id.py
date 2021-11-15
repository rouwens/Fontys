import mysql.connector as mysql

naam = "daan"
db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "muziekservice_esmee",
    )
cursor = db.cursor()

get_sql = """SELECT ID FROM `test` WHERE username =  %s;"""
cursor.execute(get_sql, (naam,))
sql_hostname = cursor.fetchall()

pre_hostname = str(sql_hostname)
hostname = pre_hostname[3:-4]
print (sql_hostname)