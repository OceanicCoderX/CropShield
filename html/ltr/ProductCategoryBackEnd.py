#!C:/Python310/python.exe
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
Name = form.getvalue("ProCatName")
fi = form["ProCatImg"]
fn = os.path.splitext(fi.filename)
uploadFileName = 'procat' + fn[1]
Description = form.getvalue("Description")
# print(Name, uploadFileName, Description)


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

query = f"""INSERT INTO productcategory (Name, Image, Description) VALUES ('{Name}','{uploadFileName}', '{Description}')"""
# print(query)
mycursor.execute(query)
mydb.commit()
procat_id = mycursor.lastrowid
# print(product_id)
upload_dir=f"assets/ProductCategory/{procat_id}"
# print(upload_dir)
os.makedirs(upload_dir, exist_ok=True)
file_path=os.path.join(upload_dir, uploadFileName)
# print(file_path)
open(file_path, 'wb').write(fi.file.read())
print(f'''
    <script>alert(" Product Category Add Successfully!");
    location.href="ProductCategoryList.py";
    </script>''')