#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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

query = f""" SELECT * FROM productcategory WHERE PCId = {Id}"""
mycursor.execute(query)
myresult = mycursor.fetchone()


import header
print(f"""
        <div class="page-wrapper">
            <div class="container-fluid">
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Product Category Form</h4>
                                <form class="m-t-30" action="ProductCategoryUpdate.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="Id">Sr No.</label>
                                        <input type="number" class="form-control" id="Id" name="Id" aria-describedby="emailHelp" value="{myresult[0]}" readonly>
                                    </div>
                                    <div class="form-group">
                                        <label for="ProCatName">Product Category Name</label>
                                        <input type="text" class="form-control" id="ProCatName" name="ProCatName" aria-describedby="emailHelp" value="{myresult[1]}">
                                    </div> 
                                    <div class="form-group">
                                        <label for="Image">Crop Category Image</label><br>
                                        <img src="assets/ProductCategory/{myresult[0]}/{myresult[2]}" style="width: 100px; height: 100px;"> &nbsp;&nbsp;&nbsp;
                                        <input type="file" id="Image" name="Image">
                                        <input type="hidden" id="OldImage" name="OldImage" value="{myresult[2]}">
                                    </div>   
                                    <div class="form-group">
                                        <label for="Description">Description</label>
                                        <input type="text" class="form-control" id="Description" name="Description" aria-describedby="emailHelp" value="{myresult[3]}">
                                    </div>                                                         
                                    <button type="submit" class="btn btn-primary">Add Product Category</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer
