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
fi = form["CropCatImage"]
fn = os.path.splitext(fi.filename)
uploadFileName = 'cropcat' + fn[1]
Name = form.getvalue("CropCatName")
Description = form.getvalue("Description")

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

query = f"""INSERT INTO cropcategory (Image, Name, Description) VALUES ('{uploadFileName}','{Name}', '{Description}')"""
# print(query)
mycursor.execute(query)
mydb.commit()

cropcat_id = mycursor.lastrowid
# print(product_id)
upload_dir=f"assets/CropCategory/{cropcat_id}"
# print(upload_dir)
os.makedirs(upload_dir, exist_ok=True)
file_path=os.path.join(upload_dir, uploadFileName)
# print(file_path)
open(file_path, 'wb').write(fi.file.read())
print(f'''
    <script>alert(" Crop Category Add Successfully!");
    location.href="CropCategoryList.py";
    </script>''')
