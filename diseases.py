#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

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
DId = form.getvalue("did")

query = f"SELECT d.DId, c.CropName, p.Name, d.Name FROM diseases d JOIN crops c ON d.CropId = c.CropId JOIN parts p ON d.PartId = p.PartId WHERE d.DId={DId}"
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)

disease = ''
for x in myresult:  
	disease += f"""
         <div class="col-md-4 col-sm-6">
            <div class="blog-post">
               <div class="post-txt">
                  <h3>{x[3]}</h3>
                  <h5>Crop: {x[1]} &nbsp;|&nbsp; Part: {x[2]}</h5>
                  <div class="mt-2">
                     <a class="btn btn-sm btn-success btn-block show-symptoms" href="symptoms.py?DId={x[0]}">Show More Symptoms</a>
                  </div>
               </div>
            </div>
         </div>
"""

import header
print("""
      <style>
             
         .post-txt h3{font-size:24px; line-height:1.1; letter-spacing:0; color:#222; margin:0 0 6px}
         .post-txt h5{font-size:14px; line-height:1.2; color:#444; margin:0 0 8px}
         .post-txt p{font-size:13px; color:#555; margin-top:6px}

         @media (max-width:767.98px){
            .post-txt h3{font-size:20px}
            .post-txt h5{font-size:13px}
         }
      </style>
""")

print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1>Diseases</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> Diseases </a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         
         <!--Diseases Start--> 
             
         <section class="wf100 p80 blog">
            <div class="blog-grid-medium">
               <div class="container">
                  <div class="row">

                     <!--Disease Entry Start-->
                     {disease}
                     <!--Disease Entry End-->


                  </div>
                  
               </div>
            </div>
         </section>
         <!--Diseases End--> 

""")

import footer
