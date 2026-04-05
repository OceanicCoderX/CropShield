#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
# print("Content-Type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
Id = form.getvalue("Id")
# print(form)

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
query = f"SELECT P.PartId, C.CropName, P.Name, P.Image FROM parts P JOIN crops C ON P.CrpId = C.CropId WHERE p.CrpId = {Id}"
# print(query)
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)


crop_part = ''
for x in myresult:
   crop_part += f'''
         <div class="col-lg-3 col-md-6">
            <div class="event-post">
               <div class="event-thumb" style="height:200px;"> 
                  <a href="symptoms.py?CPId={x[0]}&CId={Id}"> <i class="fas fa-link"></i></a> 
                  <img src="html/ltr/assets/Part/{x[0]}/{x[3]}" alt="">
               </div>
               <div class="event-txt">
                  <h5><a href="symptoms.py?CPId={x[0]}&CId={Id}">{x[2]}</a></h5>
               </div>
            </div>
         </div>
    '''
import header

print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1>Crop Parts</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> {myresult[0][1]} </a></li>
                  <li><a href="#">Parts</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         <!--Causes Start-->
         <section class="wf100 p80 events">
            <div class="event-grid-2">
               <div class="container">
               <h2> Select Crops Part </h2>
               <hr>
                  <div class="row">
                     <!--Blog Post Start-->
                     {crop_part}
                     <!--Blog Post End--> 
                  </div>
               </div>
            </div>
         </section>
         <!--Causes End--> 

""")
import footer
