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
                                <h4 class="card-title">Symptoms Form</h4>
                                <form class="m-t-30" action="SymptomsBackEnd.py" method="POST" enctype="multipart/form-data">
                                    <div class="form-group mb-3">
                                        <label for="DseName">Disease Name</label>
                                        <select class="form-control" id="DseName" name="DseName" required>
                                            <option value="">- Select Disease -</option>
                                            {dse_op}
                                        </select>
                                    </div> 
                                    <div class="form-group">
                                        <label for="SymImg">Symptoms Image</label>
                                        <input type="file" class="form-control" id="SymImg" name="SymImg" required>
                                    </div>   
                                    <div class="form-group">
                                        <label for="Description">Description</label>
                                        <input type="text" class="form-control" id="Description" name="Description" aria-describedby="emailHelp" required>
                                    </div>                                                         
                                    <button type="submit" class="btn btn-primary">Add Symptoms</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>                
            </div>
        </div>
""")
import footer
