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
FId = form.getvalue("fid")
FarmerName = form.getvalue("FarmerName")
CropName = form.getvalue("CropName")
fi = form["sImg"]
fn = os.path.splitext(fi.filename)
uploadFileName = 'fquery' + fn[1]
PartName = form.getvalue("PartName")
symtomes = form.getvalue("symtomes")

insert_query = f"""INSERT INTO farmerquery (FId, FarmerName, CropName, PartName, SymptomsDetails, SImg) VALUES ('{FId}', '{FarmerName}', '{CropName}', '{PartName}', '{symtomes}', '{uploadFileName}')"""
# print(insert_query)
mycursor.execute(insert_query)
mydb.commit()

query = mycursor.lastrowid

upload_dir=f"html/ltr/assets/FqueryImg/{query}"
os.makedirs(upload_dir, exist_ok=True)
file_path=os.path.join(upload_dir, uploadFileName)
open(file_path, 'wb').write(fi.file.read())

print(f'''
    <script>
    alert(" Query Submit Successfully!");
    location.href="faq.py?fid={FId}";
    </script>''')


