#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
Id = form.getvalue("Id")
CropId = form.getvalue("CropName")
PartId = form.getvalue("PartName")
Name = form.getvalue("DiseaseName")
# print(Id, CropId, PartId, Name)

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
    
query = f"""UPDATE diseases SET CropId='{CropId}', PartId='{PartId}', Name='{Name}' WHERE DId ={Id}"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Diseases Update Successfully!");
    location.href="DiseasesList.py";
    </script>''')
