#!C:/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
# print("Content-Type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
Id = form.getvalue("CCId")

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
query = f"SELECT C.CropId, CC.Name, C.Images, C.CropName, C.Description FROM crops C JOIN cropcategory CC ON C.CCId = CC.CCId WHERE C.CCId = {Id}"
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)



crops = ''
for x in myresult:  
	crops += f"""
            <div class="col-md-3 col-sm-6">
               <div class="gallery-img">
                  <a class="crop-icon" href="crop-part.py?Id={x[0]}"><i class="fa-solid fa-leaf"></i></a>
                  <img src="html/ltr/assets/Crop/{x[0]}/{x[2]}" style="height:350px;" alt="">
                  <div class="gallery-caption mt-2">
                     <div class="crop-meta">
                        <div>
                           <h5>{x[3]}</h5>
                           <span class="crop-category">Category: {x[1]}</span>
                        </div>
                     </div>
                     <p>{x[4]}</p>
                  </div>
               </div>
            </div>
"""
print("""
      <style>
         /* Page-local styles for crop cards */
         .gallery-caption{padding:10px}
         .gallery-caption h5{margin-bottom:4px}
         .gallery-caption .crop-category{display:block;font-size:13px;color:#6c757d;margin-bottom:6px}
         .crop-icon{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:50%;background:#2b8a3e;color:#fff;text-decoration:none}
         .gallery-img{position:relative}
         .gallery-caption{position:relative}
         .gallery-caption .crop-meta{display:flex;justify-content:space-between;align-items:center}
         </style>
      """)
import header
print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1>Crops</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> {myresult[0][1]} </a></li>
                  <li><a href="#"> Crops</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         <!--Gallery / Crops Start-->
         <div class="gallery wf100 p80">
            <div class="container">
               <h2> {myresult[0][1]}: </h2> <br> <br>
               <div class="row">
                  <!--Image Box Start-->
                  {crops}
                  <!--Image Box End--> 
               </div>
            </div>
         </div>
         <!--Gallery / Crops End-->

""")

import footer

