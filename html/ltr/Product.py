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

procat_query = "SELECT * FROM productcategory"
mycursor.execute(procat_query)
procat = mycursor.fetchall()
procat_op= ""
for pcat in procat:
    procat_op += f'''
    <option value="{pcat[0]}">{pcat[1]}</option>
    '''

dse_query = "SELECT * FROM diseases"
mycursor.execute(dse_query)
diseases = mycursor.fetchall()
dse_op= ""
for dse in diseases:
    dse_op += f'''
    <option value="{dse[0]}">{dse[3]}</option>
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
                                <form class="m-t-30" action="ProductBackEnd.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group mb-3">
                                        <label for="ProCategory">Product Category Name</label>
                                        <select class="form-control" id="ProCategory" name="ProCategory" required>
                                            <option value="">- Select Product Category -</option>
                                            {procat_op}
                                        </select>
                                    </div> 
                                    <div class="form-group mb-3">
                                        <label for="DesName">Disease Name</label>
                                        <select class="form-control" id="DesName" name="DesName" required>
                                            <option value="">- Select Disease -</option>
                                            {dse_op}
                                        </select>
                                    </div> 
                                    <div class="form-group">
                                        <label for="ProName">Product Name</label>
                                        <input type="text" class="form-control" id="ProName" name="ProName" aria-describedby="emailHelp" required>
                                    </div>
                                    <div class="form-group">
                                        <label for="ProImg">Product Image</label>
                                        <input type="file" class="form-control" id="ProImg" name="ProImg">
                                    </div>    
                                    <div class="form-group">
                                        <label for="ProDetails">Product Details</label>
                                        <input type="text" class="form-control" id="ProDetails" name="ProDetails" aria-describedby="emailHelp" required>
                                    </div>     
                                    <div class="form-group">
                                        <label for="Usage">How to Use?</label>
                                        <input type="text" class="form-control" id="Usage" name="Usage" aria-describedby="emailHelp">
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


