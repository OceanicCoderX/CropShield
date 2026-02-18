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

query = f""" SELECT * FROM crops WHERE CroPId = {Id}"""
mycursor.execute(query)
myresult = mycursor.fetchone()


query = "SELECT * FROM cropcategory"
mycursor.execute(query)
cropscat = mycursor.fetchall()
cat_op= ""
for cat in cropscat:
    selected = "selected" if str(cat[0]) == str(myresult[1]) else ""
    cat_op += f'''
    <option value="{cat[0]}" {selected}>{cat[2]}</option>
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
                                <h4 class="card-title">Product Form</h4>
                                <form class="m-t-30" action="CropsUpdate.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="Id">Sr No.</label>
                                        <input type="number" class="form-control" id="Id" name="Id" aria-describedby="emailHelp" value="{myresult[0]}" readonly>
                                    </div>
                                    <div class="form-group mb-3">
                                        <label for="CatName">Crop Category Name</label>
                                        <select class="form-control" id="CatName" name="CatName" required>
                                            <option value="">- Select Crop Category -</option>
                                            {cat_op}
                                        </select>
                                    </div> 
                                    <div class="form-group">
                                        <label for="Image">Crop Category Image</label><br>
                                        <img src="assets/Crop/{myresult[0]}/{myresult[2]}" style="width: 100px; height: 100px;"> &nbsp;&nbsp;&nbsp;
                                        <input type="file" id="Image" name="Image">
                                        <input type="hidden" id="OldImage" name="OldImage" value="{myresult[2]}">
                                    </div>
                                    <div class="form-group">
                                        <label for="CropName">Crop Name</label>
                                        <input type="text" class="form-control" id="CropName" name="CropName" aria-describedby="emailHelp" value="{myresult[3]}">
                                    </div>    
                                    <div class="form-group">
                                        <label for="Description">Description</label>
                                        <input type="text" class="form-control" id="Description" name="Description" aria-describedby="emailHelp" value="{myresult[4]}">
                                    </div>                                                         
                                    <button type="submit" class="btn btn-primary">Edit Crops Information</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer