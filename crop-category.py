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
# print(myresult)
crop_cat = ''
for x in myresult:  
	crop_cat += f"""
            <div class="col-md-4 col-sm-6">
               <div class="event-post">
                  <div class="event-thumb"> <a href="crops.py?CCId={x[0]}"><i  class="fa-solid fa-seedling"></i></a> <img src="html/ltr/assets/CropCategory/{x[0]}/{x[1]}" alt="Fruits" style="height: 300px;"> </div>
                  <div class="event-txt">
                     <h5><a href="crops.html">{x[2]}</a></h5>
                     <p>{x[3]}</p>
                  </div>
               </div>
            </div>
"""

import header
print(f"""         
         
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1 data-i18n="cropcats_title">Crop Categories</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#">Categories</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End-->

         <!--Crop Categories Start-->
         <section class="wf100 p80 events">
            <div class="container">
               <div class="row mb30">
                  <div class="col-md-8">
                     <div class="section-title-2">
                        <h5 data-i18n="cropcats_explore">Explore</h5>
                        <h2 data-i18n="cropcats_heading">Crop Categories</h2>
                     </div>
                  </div>
                  <div class="col-md-4 text-right">
                     <form class="form-inline" method="get" action="crop-category.py">
                        <input class="form-control mr-2" type="search" name="q" placeholder="Search crops" aria-label="Search" data-i18n-placeholder="search_crops">
                        <button class="btn btn-outline-success" type="submit" data-i18n="btn_search">Search</button>
                     </form>
                  </div>
               </div>

               <div class="row">
                  <!-- Crop Card Start -->
                  {crop_cat}
                  <!-- Crop Card End -->
               </div>

               <div class="row">
                  <div class="col-md-12">
                     <div class="gt-pagination mt20">
                        <nav>
                           <ul class="pagination">
                              <li class="page-item"> <a class="page-link" href="#" aria-label="Previous"> <i class="fas fa-angle-left"></i> </a> </li>
                              <li class="page-item"><a class="page-link" href="#">1</a></li>
                              <li class="page-item active"><a class="page-link" href="#">2</a></li>
                              <li class="page-item"><a class="page-link" href="#">3</a></li>
                              <li class="page-item"> <a class="page-link" href="#" aria-label="Next"> <i class="fas fa-angle-right"></i> </a> </li>
                           </ul>
                        </nav>
                     </div>
                  </div>
               </div>
            </div>
         </section>
         <!--Crop Categories End--> 
""")
import footer