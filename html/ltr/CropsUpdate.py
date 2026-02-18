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
Id = form.getvalue("Id")
CCId = form.getvalue("CatName")
OldImage = form.getvalue("OldImage")
CropName = form.getvalue("CropName")
Description = form.getvalue("Description")
# print(Id, CCId, OldImage, CropName, Description)

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


if "Image" in form:
    NewImg = form["Image"]
    # print(NewImg)
else:
    NewImg = None
    
ImgName = OldImage # Keep old photo by default
# print(ImgName)

if "Image" in form and form["Image"].filename:
    NewImg = form["Image"]
    fn = os.path.splitext(NewImg.filename)
    # print(fn[0])
    ImgName = 'crop' + fn[1]
    # print(ImgName)
    
    
    upload_dir = f"assets/Crop/{Id}"
    
    file_path = os.path.join(upload_dir, ImgName)
    # print(file_path)
    
    # Save new file (overwrite old one if exists)
    with open(file_path, "wb") as f:
        f.write(NewImg.file.read())
        
    # Delete old file if exists and is different
    oldpath = os.path.join(upload_dir, OldImage) if OldImage else None
    if oldpath and os.path.exists(oldpath) and OldImage != ImgName:
        os.remove(oldpath)
    
query = f"""UPDATE crops SET CCId='{CCId}', Images='{ImgName}', CropName='{CropName}', Description='{Description}' WHERE CropId ={Id}"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Crops Update Successfully!");
    location.href="CropsList.py";
    </script>''')