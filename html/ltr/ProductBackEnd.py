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
# print(form)
PCId = form.getvalue("ProCategory")
DId = form.getvalue("DesName")
Name = form.getvalue("ProName")
fi = form["ProImg"]
fn = os.path.splitext(fi.filename)
uploadFileName = 'product' + fn[1]
Detail = form.getvalue("ProDetails")
Usege = form.getvalue("Usage")
# print(Name, PCId, DId, uploadFileName, Detail, Usege)

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

query = f"""INSERT INTO product (PCId, DId, Name, Image, Detail, Usege) VALUES ('{PCId}', '{DId}', '{Name}', '{uploadFileName}', '{Detail}', '{Usege}')"""
# print(query)
mycursor.execute(query)
mydb.commit()
pro_id = mycursor.lastrowid
# print(product_id)
upload_dir=f"assets/Product/{pro_id}"
# print(upload_dir)
os.makedirs(upload_dir, exist_ok=True)
file_path=os.path.join(upload_dir, uploadFileName)
# print(file_path)
open(file_path, 'wb').write(fi.file.read())
print(f'''
    <script>alert(" Product Add Successfully!");
    location.href="ProductList.py";
    </script>''')
