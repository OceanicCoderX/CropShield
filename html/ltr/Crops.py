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

query = "SELECT * FROM cropcategory"
mycursor.execute(query)
myresult = mycursor.fetchall()
cat_op= ""
for cat in myresult:
    cat_op += f'''
    <option value="{cat[0]}">{cat[2]}</option>
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
                                <h4 class="card-title">Crops Information Form</h4>
                                <form class="m-t-30" action="CropsBackEnd.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group mb-3">
                                        <label for="CatName">Crop Category Name</label>
                                        <select class="form-control" id="CatName" name="CatName" required>
                                            <option value="">- Select Crop Category -</option>
                                            {cat_op}
                                        </select>
                                    </div> 
                                    <div class="form-group">
                                        <label for="CropImage">Crop Image</label>
                                        <input type="file" class="form-control" id="CropImage" name="CropImage" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="CropName">Crop Name</label>
                                        <input type="text" class="form-control" id="CropName" name="CropName" aria-describedby="emailHelp" required>
                                    </div>    
                                    <div class="form-group">
                                        <label for="Description">Description</label>
                                        <input type="text" class="form-control" id="Description" name="Description" aria-describedby="emailHelp">
                                    </div>                                                         
                                    <button type="submit" class="btn btn-primary">Add Crops</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer