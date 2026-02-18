#!C:/Python310/python.exe
import sys
import cgi
import cgitb
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
import header
print("""
        <div class="page-wrapper">
            <div class="container-fluid">
                <!-- row -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Crop Category Form</h4>
                                <form class="m-t-30" action="CropCategoryBackEnd.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="CropCatImage">Crop Category Image</label>
                                        <input type="file" class="form-control" id="CropCatImage" name="CropCatImage" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="CropCatName">Crop Category Name</label>
                                        <input type="text" class="form-control" id="CropCatName" name="CropCatName" required>
                                    </div>    
                                    <div class="form-group">
                                        <label for="Description">Description</label>
                                        <input type="text" class="form-control" id="Description" name="Description">
                                    </div>                                                         
                                    <button type="submit" class="btn btn-primary">Add Product</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer