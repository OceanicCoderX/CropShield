#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import os
print("Content-Type:text/html\n")
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
Id = form.getvalue("Id")
OldImage = form.getvalue("OldImage")
Name = form.getvalue("Name")
Email = form.getvalue("Email")
PhoneNo = form.getvalue("PhoneNo")
Address = form.getvalue("Address")
GSTno = form.getvalue("GSTno")
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
# Handle file upload
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
    ImgName = 'logo' + fn[1]
    # print(ImgName)
    
    
    upload_dir = f"assets/Logo/{Id}"
    
    file_path = os.path.join(upload_dir, ImgName)
    # print(file_path)
    
    # Save new file (overwrite old one if exists)
    with open(file_path, "wb") as f:
        f.write(NewImg.file.read())
        
    # Delete old file if exists and is different
    oldpath = os.path.join(upload_dir, OldImage) if OldImage else None
    if oldpath and os.path.exists(oldpath) and OldImage != ImgName:
        os.remove(oldpath)
    
query = f"""UPDATE company SET CompanyName='{Name}', Logo='{ImgName}', Email='{Email}', PhoneNo='{PhoneNo}', Address='{Address}', GSTno='{GSTno}' WHERE CId={Id}"""
# print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Company Update Successfully!");
    location.href="CompanyList.py";
    </script>''')
