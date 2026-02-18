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

form = cgi.FieldStorage()
fid = form.getvalue("fid")

import header

print(f"""
         
         <!--Slider Start-->
         <section id="home-slider" class="owl-carousel owl-theme wf100">
            <div class="item">
                     <div class="slider-caption h2slider">
                  <div class="container">
                     <strong data-i18n="slider1_strong">Protect<span> Every Crop, </span></strong>
                     <h1 data-i18n="slider1_h1">Empower Every Farmer -</h1>
                     <p data-i18n="slider1_p">Together We Grow Stronger.</p>
                     <a href="crop-category.py" class="active" data-i18n="cta_crop_category">Crop Category</a> <a href="faq.py?fid={fid}" data-i18n="cta_faq">Farmer Ask Query</a>
                  </div>
               </div>
               <img src="images/CropShield/cropBg8.jpg" class="hei"> 
            </div>
            <div class="item">
                     <div class="slider-caption h2slider">
                  <div class="container">
                     <strong data-i18n="slider2_strong"><span>From</span>Root to Grain</strong>
                     <h1 style="font-size:80px;" data-i18n="slider2_h1">Shielding Crops, Securing Futures</h1>
                     <a href="crop-category.py" class="active" data-i18n="cta_crop_category">Crop Category</a> <a href="faq.py?fid={fid}" data-i18n="cta_faq">Farmer Ask Query</a>
                  </div>
               </div>
               <img src="images/CropShield/cropBg7.jpg" class="hei"> 
            </div>
            <div class="item">
                     <div class="slider-caption h2slider">
                  <div class="container">
                     <strong data-i18n="slider3_strong">Ask. <span> & don’t Act.</span> Advance</strong>
                     <h1 data-i18n="slider3_h1">Your Farm’s Health </h1>
                     <p data-i18n="slider3_p">Before <strong>it’s too late</strong> Starts Here.</p>
                     <a href="crop-category.py" class="active" data-i18n="cta_crop_category">Crop Category</a> <a href="faq.py?fid={fid}" data-i18n="cta_faq">Farmer Ask Query</a>
                  </div>
               </div>
               <img src="images/CropShield/cropBg5.jpg" class="hei"> 
            </div>
         </section>
         <!--Slider End--> 
         
         <!--Service Area Start-->
         <section class="services-area wf100">
            <div class="container">
         <ul>
                  <!--box  start-->
                  <li>
                     <div class="sinfo">
                        <img src="images/t1.png" style="width:70px;"> 
            <h6 data-i18n="svc_crop_diagnosis">Crop Diagnosis</h6>
            <p data-i18n="svc_crop_diagnosis_p">Identify symptoms & <br> protect your yield</p>
                     </div>
                  </li>
                  <!--box  end--> 
                  <!--box  start-->
                  <li>
                     <div class="sinfo">
                        <img src="images/t5.png" style="width:70px;">
                        <h6 data-i18n="svc_query_panel">Farmer Query <br> Panel</h6>
                        <p data-i18n="svc_query_panel_p">Ask questions, <br> get expert answers</p>
                     </div>
                  </li>
                  <!--box  end--> 
                  <!--box  start-->
                  <li>
                     <div class="sinfo">
                        <img src="images/t3.png" style="width:70px;">
                        <h6 data-i18n="svc_tracker">Disease & Symptom Tracker</h6>
                        <p data-i18n="svc_tracker_p">Track crop health <br> part-wise</p>
                     </div>
                  </li>
                  <!--box  end--> 
                  <!--box  start-->
                  <li>
                     <div class="sinfo">
                        <img src="images/t2.png" style="width:70px;">
                        <h6 data-i18n="svc_multilingual">Multilingual Crop Forms</h6>
                        <p data-i18n="svc_multilingual_p">Support for <br> English & Marathi inputs</p>
                     </div>
                  </li>
                  <!--box  end--> 
                  <!--box  start-->
                  <li>
                     <div class="sinfo">
                        <img src="images/sericon5.png" style="width:70px;">
                        <h6 data-i18n="svc_insights">Crop Category Insights</h6>
                        <p data-i18n="svc_insights_p">Explore parts, <br> diseases & treatments</p>
                     </div>
                  </li>
                  <!--box  end-->
               </ul>
            </div>
         </section>
         <!--Service Area End--> 
         
         
         <!--About Section Start-->
         <section class="home2-about wf100 p100 gallery">
            <div class="container">
               <div class="row">
                  <div class="col-md-5">
                     <div class="video-img"> <a href="http://vimeo.com/43338103&amp;width=700" data-rel="prettyPhoto" title="Vimeo video"><i class="fas fa-play"></i></a> <img src="images/agallery7.jpg" alt=""> </div>
                  </div>
                  <div class="col-md-7">
                     <div class="h2-about-txt">
                        <h3>CropShield — Smart Crop Diagnosis & Support</h3>
                        <h2>Eco-friendly products can be made from scratch.</h2>
                        <p>CropShield empowers farmers with fast, practical help for crop problems — from pests and diseases to nutrient deficiencies and management tips.</p>
                        <a class="aboutus" href="about.py">More About us</a> 
                     </div>
                  </div>
               </div>
            </div>
""")
mycursor.execute("SELECT COUNT(*) FROM crops")
total_crops = mycursor.fetchone()[0]

mycursor.execute("SELECT COUNT(*) FROM product")
total_product = mycursor.fetchone()[0]

mycursor.execute("SELECT COUNT(*) FROM feedback")
total_feedback = mycursor.fetchone()[0]

mycursor.execute("SELECT COUNT(*) FROM farmerquery")
total_query = mycursor.fetchone()[0]

print(f"""
            <div class="home-facts counter pt80">
               <div class="container">
                  <div class="row">
                     <div class="col-lg-3 col-sm-6 col-md-3">
                        <div class="counter-box">
                           <p class="counter-count">{total_crops}</p>
                           <p class="ctxt">Crops</p>
                        </div>
                     </div>
                     <div class="col-lg-3 col-sm-6 col-md-3">
                        <div class="counter-box">
                           <p class="counter-count">{total_product}</p>
                           <p class="ctxt">Products</p>
                        </div>
                     </div>
                     <div class="col-lg-3 col-sm-6 col-md-3">
                        <div class="counter-box">
                           <p class="counter-count">{total_feedback}</p>
                           <p class="ctxt">Farmers Feed Back</p>
                        </div>
                     </div>
                     <div class="col-lg-3 col-sm-6 col-md-3">
                        <div class="counter-box">
                           <p class="counter-count">{total_query}</p>
                           <p class="ctxt">Farmers Querys</p>
                        </div>
                     </div>
                  </div>
                  <img src="images\moveImgs\case-caseih.gif" alt="Animated Farmer" style="max-width:200px; margin-left: 1050px; margin-top:-180px; margin-bottom: -180px;">
               </div>
            </div>
         </section>
         <!--About Section End-->
          
         <!--Urgent Causes Start-->
         <section class="urgent-causes wf100 p80">
            <div class="container">
               <div class="row">
                  <div class="col-md-8">
                     <br><br><br>
                     <div class="section-title-2 white">
                        <h5>Protect Crops.</h5>
                        <h2>Empower Farmers. Stop Crop Loss.</h2>
                     </div>
                     <p> We need your support and help to Stop Globar Warning. Few generations ago it to seemed like the world’s resources were infinite, and the people needed only. </p>
                     <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 55%" aria-valuenow="55" aria-valuemin="0" aria-valuemax="100"></div>
                     </div>
                     <ul class="funds">
                        <li class="text-left"><strong>73%</strong> Diagnosed </li>
                        <li class="text-center"><strong>$948.00</strong> Farmers Helped </li>
                        <li class="text-right"><strong>$1750.00</strong> Crop-Part Mappings </li>
                     </ul>
                  </div>
                  <div class="col-lg-4 col-md-4">
                     <div class="volunteer-form">
                        <div class="section-title">
                           <h3>Get Started</h3>
                        </div>
                        <ul>
                           <li>
                              <input type="text" class="form-control" placeholder="Farmer name" aria-label="Your Name">
                           </li>
                           <li>
                              <input type="text" class="form-control" placeholder="Village / Town" aria-label="Location">
                           </li>
                           <li>
                              <input type="text" class="form-control" placeholder="Contact number" aria-label="Contact">
                           </li>
                           <li>
                              <input type="submit" class="fsubmit" value="Request Advice">
                           </li>
                        </ul>
                     </div>
                  </div>
               </div>
            </div>
         </section>
         <!--Urgent Causes End--> 
         
         
""")
crop_cat = "SELECT * FROM cropcategory LIMIT 8"
mycursor.execute(crop_cat)
categories = mycursor.fetchall()

c_category = ''
for x in categories:
   c_category += f'''
      <li class="nav-item"> <a class="nav-link" href="crop-category.py">{x[2]} </a> </li>
   '''
cat_img = ''
for x in categories:
   cat_img += f'''
      <div class="item">
         <div class="pro-box">
            <img src="html/ltr/assets/CropCategory/{x[0]}/{x[1]}" style="height:300px;">
            <h5>{x[2]}</h5>
            <div class="pro-hover">
               <h6>{x[2]}</h6>
               <p>{x[3]}</p>
               <a href="crop-category.py">Read More</a>
            </div>
         </div>
      </div>
   '''
print(f"""
         <!--Crop Category Start-->
         <section class="wf100 p80 current-projects">
            <div class="container">
               <div class="row">
                  <div class="col-lg-4">
                     <div class="section-title-2">
                        <h5>We are working these</h5>
                        <h2>Crops-Category</h2>
                     </div>
                  </div>
                  <div class="col-lg-8">
                     <ul class="nav" id="myTab" role="tablist">
                        {c_category}
                     </ul>
                  </div>
               </div> <br><br>
               <div class="row">
                  <div class="col-md-12">
                     <div class="tab-content" id="myTabContent">
                     
                        <!-- Slider Start-->
                        <div class="tab-pane fade show active" id="wildlife" role="tabpanel" aria-labelledby="wildlife-tab">
                           <div class="cpro-slider owl-carousel owl-theme">
                           
                              <!--Pro Box-->
                              {cat_img}
                              <!--Pro Box End-->    
                              
                           </div>
                        </div>
                        <!-- Slider End--> 
                         
                     </div>
                  </div>
               </div>
            </div>
         </section>
         <!--Crop Category End--> 
        
""")
query = "SELECT rq.Question, rq.Answer, p.PId, p.Image FROM replayquery rq JOIN product p ON rq.SuggestProduct = p.PId LIMIT 2"
# print(query)
mycursor.execute(query)
faq_results = mycursor.fetchall()
admin_query = ''
for f in faq_results:
   que, ans, pid, pimg = f
   admin_query += f'''
                     <div class="blog-small-post">
                        <div class="post-thumb"> <a href="#"><i class="fas fa-link"></i></a> <img src="html/ltr/assets/Product/{pid}/{pimg}" style="height:200px"> </div>
                        <div class="post-txt">
                           <h5><a href="#">{que}</a></h5>
                           <p>{(ans[:80] + '...') if ans and len(ans)>80 else (ans or '')}</p>
                           <a href="#" class="rm">Read More</a> 
                        </div>
                     </div>
   
   '''
   
print(f""" 
         <!--Farmers Queries Start-->
         <section class="h2-news wf100 p80">
            <div class="container">
               <div class="row">
                  <div class="col-md-6">
                     <div class="section-title-2">
                        <h5>Read Our Latest</h5>
                        <h2>Farmers Queries</h2>
                     </div>
                  </div>
                  <div class="col-md-6"> <a href="#" class="view-more">View More News</a> </div>
               </div>
               <div class="row">
                  <div class="col-md-6">
                     <div class="blog-post-large">
                        <div class="post-thumb"> <a href="#"><i class="fas fa-link"></i></a> <img src="images/h2news1.jpg" alt=""></div>
                        <div class="post-txt">
                           <ul class="post-meta">
                              <li><i class="fas fa-calendar-alt"></i> Join Farmers</li>
                              <li><i class="fas fa-comments"></i> 134 Queries</li>
                           </ul>
                           <h5><a href="#">Planting Trees for Better Future</a></h5>
                        </div>
                     </div>
                  </div>
                  <div class="col-md-6">
                     <!--Blog Small Post Start-->
                     {admin_query}
                     <!--Blog Small Post End--> 
                  </div>
               </div>
            </div>
         </section>
         <!--Farmers Queries End--> 
         
         <!--Farmer Ask Query Start-->
         <section class="why-ecova wf100">
            <div class="container">
               <div class="row">
                  <div class="col-md-12">
                     <h1> Farmer Ask Query</h1>
                     <p>Join us in transforming agriculture — save water, conserve energy, 
                        reduce pollution, and plant for a greener future with solar-powered solutions.
                     </p>
                     <a id="faqLink" href="faq.py" class="cus">Farmer Ask Query <i class="fa-solid fa-arrow-right"></i></a> 
                  </div>
               </div>
            </div>
         </section>
         <!--Farmer Ask Query End--> 
""")

products_query = "SELECT p.PId, pc.Name, p.Name, p.Image FROM product p JOIN productcategory pc ON p.PCId = pc.PCId ORDER BY PId DESC LIMIT 4"
mycursor.execute(products_query)
products = mycursor.fetchall()
pro_list = ''
for pro in products:
   pro_list += f'''
   
                  <div class="col-md-3 col-sm-6">
                     <div class="product-box">
                        <div class="pro-thumb"> <a href="details.py?pid={pro[0]}">Show Detail</a> <img src="html/ltr/assets/Product/{pro[0]}/{pro[3]}" alt=""></div>
                        <div class="pro-txt">
                           <h6><a href="#">{pro[2]}</a></h6>
                           <p class="pro-price">{pro[1]}</p>
                        </div>
                     </div>
                  </div>
   
   '''

print(f"""         
         <!--Online Products Start-->
         <section class="online-shop wf100 p80">
            <div class="container">
               <div class="row">
                  <div class="col-md-12">
                     <div class="section-title-2 text-center">
                        <h5>Read Our Latest</h5>
                        <h2>Products</h2>
                     </div>
                  </div>
               </div>
               <div class="row">
                  <!--Pro Box Start-->
                  {pro_list}
                  <!--Pro Box End--> 
                   
               </div>
            </div>
         </section>
         <!--Online Products End-->

""")
import footer