#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import os
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')
print("Content-Type:text/html; charset=utf-8\n")

form = cgi.FieldStorage()
CId = form.getvalue("CId")
CPId = form.getvalue("CPId")
DId = form.getvalue("DId")

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

if CId:
   query = f"SELECT s.SId, d.Name, s.Image, s.Description, s.DId FROM symptoms s JOIN diseases d ON d.DId = s.DId WHERE d.CropId={CId} AND d.PartId={CPId}"
   # print(query)
   mycursor.execute(query)
   myresult = mycursor.fetchall()
   # print(myresult)
else:
   query = f"SELECT s.SId, d.Name, s.Image, s.Description, s.DId FROM symptoms s JOIN diseases d ON d.DId = s.DId WHERE s.DId={DId}"
   # print(query)
   mycursor.execute(query)
   myresult = mycursor.fetchall()
   # print(myresult)

symptm = ''
for x in myresult:
   symptm += f'''
   
      <div class="col-md-6">
         <div class="blog-small-post">
            <div class="post-thumb"> <a href="product.py?did={x[4]}"><i class="fas fa-link"></i></a> <img src="html/ltr/assets/Symptoms/{x[0]}/{x[2]}" style="height:250px;"> </div>
            <div class="post-txt">
               <h5><a href="diseases.py?did={x[4]}">{x[1]}</a></h5>
               <p>{x[3]}</p>
               <a class="btn btn-sm btn-success btn-block show-symptoms" href="product.py?did={x[4]}" data-i18n="btn_show_products">Show Products</a>
            </div>
         </div>
      </div>
      
'''

import header

print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1 data-i18n="symptoms_title">Symptoms</h1>
               <ul>
                  <li><a href="#" data-i18n="breadcrumb_home">Home</a></li>
                  <li><a href="#" data-i18n="breadcrumb_crops">Crops</a></li>
                  <li><a href="#" data-i18n="breadcrumb_parts">Parts</a></li>
                  <li><a href="#" data-i18n="breadcrumb_symptoms">Symptoms</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         <!--Blog Start-->
         <section class="wf100 p80 blog">
            <div class="container">
               <div class="row">
               
                  <!--Blog Small Post Start-->
                  {symptm}
                  <!--Blog Small Post End--> 
                  
               </div>
            </div>
         </section>
         <!--Blog End--> 

""")
import footer
