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
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="cropshield",
    ssl_disabled=True,
    use_pure=True
)
mycursor = mydb.cursor()

form = cgi.FieldStorage()

OldImg = form.getvalue("OldImg")
fi = form["UserImg"]
fn = os.path.splitext(fi.filename)
uploadFileName = 'user' + fn[1]

FId = form.getvalue("Id")
Name = form.getvalue("Name")
Email = form.getvalue("Email")
PhoneNo = form.getvalue("PhoneNo")
Address = form.getvalue("Address")
Distric = form.getvalue("Distric")
State = form.getvalue("State")

if uploadFileName:
    query = f"""UPDATE farmerlogin SET Name='{Name}', Image='{uploadFileName}', Email='{Email}', PhoneNo='{PhoneNo}', Address='{Address}', Distric='{Distric}', State='{State}' WHERE FId={FId}"""
    mycursor.execute(query)
    mydb.commit()
    
    upload_dir=f"html/ltr/assets/userImg/{FId}"
    # print(upload_dir)
    os.makedirs(upload_dir, exist_ok=True)
    file_path=os.path.join(upload_dir, uploadFileName)
    # print(file_path)
    open(file_path, 'wb').write(fi.file.read())
    
else:

    # Handle file upload
    if "UserImg" in form:
        NewImg = form["UserImg"]
        # print(NewImg)
    else:
        NewImg = None
        
    UserImg = OldImg # Keep old photo by default
    # print(ImgName)

    if "UserImg" in form and form["UserImg"].filename:
        NewImg = form["UserImg"]
        fn = os.path.splitext(NewImg.filename)
        UserImg = 'user' + fn[1]
        
        upload_dir = f"html/ltr/assets/userImg/{FId}"
        
        file_path = os.path.join(upload_dir, UserImg)
        
        with open(file_path, 'wb') as f:
            f.write(NewImg.file.read())
            
        # Delete old file if exists and is different
        oldpath = os.path.join(upload_dir, OldImg) if OldImg else None
        if oldpath and os.path.exists(oldpath) and OldImg != UserImg:
            os.remove(oldpath)

        query = f"""UPDATE farmerlogin SET Name='{Name}', Image='{UserImg}', Email='{Email}', PhoneNo='{PhoneNo}', Address='{Address}', Distric='{Distric}', State='{State}' WHERE FId={FId}"""
        mycursor.execute(query)
        mydb.commit()
        
print(f'''
    <script>alert(" Profile Update Successfully!");
    location.href="myaccount.py?fid={FId}";
    </script>''')