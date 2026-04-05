#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
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

crop_query = "SELECT * FROM crops"
mycursor.execute(crop_query)
crop = mycursor.fetchall()
crop_op= ""
for cp in crop:
    crop_op += f'''
    <option value="{cp[0]}">{cp[3]}</option>
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
                                <h4 class="card-title">Crop Part Form</h4>
                                <form class="m-t-30" action="CropPartBackEnd.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group mb-3">
                                        <label for="CropName">Crop Name</label>
                                        <select class="form-control" id="CropName" name="CropName" required>
                                            <option value="">- Select Crop -</option>
                                            {crop_op}
                                        </select>
                                    </div> 
                                    <div class="form-group">
                                        <label for="CropPartName">Crop Part Name</label>
                                        <input type="text" class="form-control" id="CropPartName" name="CropPartName" aria-describedby="emailHelp" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="CropPartImage">Crop Part Image</label>
                                        <input type="file" class="form-control" id="CropPartImage" name="CropPartImage" required>
                                    </div>                                                         
                                    <button type="submit" class="btn btn-primary">Add Crop Part</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer
