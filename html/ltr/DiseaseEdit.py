#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
# print("Content-Type:text/html; charset=utf-8\n")

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
Id = form.getvalue("cid")
# print(Id)

query = f""" SELECT * FROM diseases WHERE DId = {Id}"""
mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)


crop_query = "SELECT * FROM crops"
mycursor.execute(crop_query)
crop = mycursor.fetchall()
crop_op= ""
for cp in crop:
    selected = "selected" if str(cp[0]) == str(myresult[1]) else ""
    crop_op += f'''
    <option value="{cp[0]}" {selected}>{cp[3]}</option>
    '''

part_query = "SELECT * FROM parts"
mycursor.execute(part_query)
croppart = mycursor.fetchall()
part_op= ""
for part in croppart:
    selected = "selected" if str(part[0]) == str(myresult[2]) else ""
    part_op += f'''
    <option value="{part[0]}" {selected}>{part[2]}</option>
    '''
    
import header
print(f"""
        <div class="page-wrapper">
            <div class="container-fluid">
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Disease Form</h4>
                                <form class="m-t-30" action="DiseasesUpdate.py" method="POST" enctype="multipart/form-data"> 
                                    <div class="form-group">
                                        <label for="Id">Sr No.</label>
                                        <input type="number" class="form-control" id="Id" name="Id" aria-describedby="emailHelp" value="{myresult[0]}" readonly>
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="CropName">Crop Name</label>
                                        <select class="form-control" id="CropName" name="CropName" required>
                                            <option value="">- Select Crop -</option>
                                            {crop_op}
                                        </select>
                                    </div> 
                                    <div class="form-group mb-3">
                                        <label for="PartName">Crop Part Name</label>
                                        <select class="form-control" id="PartName" name="PartName" required>
                                            <option value="">- Select Crop Category -</option>
                                            {part_op}
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="DiseaseName">Disease Name</label>
                                        <input type="text" class="form-control" id="DiseaseName" name="DiseaseName" aria-describedby="emailHelp" value="{myresult[3]}">
                                    </div>                                                        
                                    <button type="submit" class="btn btn-primary">Add Disease</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer