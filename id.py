import mysql.connector as mysql


db = mysql.connect(
    host = "rouwens.ddns.net",
    user = "fontys",
    passwd = "E6g2sAnv4FHBB4HB",
    database = "muziekservice_esmee",
    )
cursor = db.cursor()

naam = "esmee"

get_sql = """SELECT pop FROM `test` WHERE `username` = %s;"""
cursor.execute(get_sql, (naam,))
sql_hostname = cursor.fetchall()

pre_hostname = str(sql_hostname)
hostname = pre_hostname[3:-4]
print (sql_hostname)
print (hostname)

if hostname == "yes":
    print ("Je hebt toegang tot de genere pop")

else:
    print ("Je hebt geen toegang")