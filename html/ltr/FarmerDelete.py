#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

mydb = mysql.connector.connect(
    host="localhost",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",
    database="cropshield",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
mycursor = mydb.cursor()

form = cgi.FieldStorage()
Id = form.getvalue("fid")

query = f"""Delete from farmerlogin where FId={Id}"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Farmer Deleted!");
    location.href="FarmerList.py";
    </script>''')