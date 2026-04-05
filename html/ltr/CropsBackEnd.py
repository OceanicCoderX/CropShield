#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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
# print(form)
CCId = form.getvalue("CatName")
fi = form['CropImage']
fn = os.path.splitext(fi.filename)
uploadFileName = 'crop' + fn[1]
CropName = form.getvalue("CropName")
Description = form.getvalue("Description")
# print(CCId, uploadFileName, CropName, Description)

query = f"""INSERT INTO crops (CCId, Images, CropName, Description) VALUES ('{CCId}', '{uploadFileName}','{CropName}', '{Description}')"""
# print(query)
mycursor.execute(query)
mydb.commit()

crop_id = mycursor.lastrowid
# print(crop_id)
upload_dir=f"assets/Crop/{crop_id}"
# print(upload_dir)
os.makedirs(upload_dir, exist_ok=True)
file_path=os.path.join(upload_dir, uploadFileName)
# print(file_path)
open(file_path, 'wb').write(fi.file.read())
print(f'''
    <script>alert(" Crop Add Successfully!");
    location.href="CropsList.py";
    </script>''')
