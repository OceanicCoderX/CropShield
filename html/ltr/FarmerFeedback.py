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

query = "SELECT f.FId, f.Image, f.Name, fb.FeedBack, fb.Star FROM feedback fb JOIN farmerlogin f ON f.FID = fb.FId"
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchall()

tr_html = ''
for x in myresult:
    stars_html = ''
    for i in range(5):
        if i < x[4]:
            stars_html += '<span class="fa fa-star checked"></span>'  # filled star
        else:
            stars_html += '<span class="fa fa-star"></span>'  # empty star
               
    tr_html += f'''
        
        <li class="media">
            <h4>{x[0]}</h4> &nbsp &nbsp &nbsp
            <img class="m-r-15" src="assets/userImg/{x[0]}/{x[1]}" width="60" alt="Generic placeholder image">
            <div class="media-body">
                <h5 class="mt-0 mb-1">{x[2]}</h5> {x[3]}
                <div class="rating" aria-hidden="true">{stars_html}</div>
            </div>
        </li>
        <hr>
    '''
print("""
      <style>
         .fa-star {color: #ccc; font-size:15px;}
         .checked {color: #2962ff;}
      </style>
""")

import header
print(f"""
      <!-- ============================================================== -->
        <!-- Page wrapper  -->
        <!-- ============================================================== -->
        <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Farmers FeedBack</h4>
                    </div>
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <!-- basic table -->
                <div class="row">
                    <div class="col-lg-12">
                        <div class="card">
                            <div class="card-body">
                                <ul class="list-unstyled m-t-40">
                                    {tr_html}
                                </ul>
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
        
""")
import footer
