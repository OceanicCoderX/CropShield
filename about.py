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

import header
print("""
   
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1 data-i18n="about_title">About Us</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#">About Us</a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         <!--About Start-->
         <section class="wf100 about">
            <!--About Txt Video Start-->
            <div class="about-video-section wf100">
               <div class="container">
                  <div class="row">
                     <div class="col-lg-6">
                           <div class="about-text">
                              <h5 data-i18n="about_protecting">Protecting Your Harvest</h5>
                              <h2 data-i18n="about_heading">CropShield — Smart Crop Diagnosis & Support</h2>
                              <p><strong data-i18n="about_intro">CropShield empowers farmers with fast, practical help for crop problems — from pests and
                              diseases to nutrient deficiencies and management tips.</strong></p>
                              <p data-i18n="about_body">We provide image-based guides, symptom checkers, and a direct farmer-to-admin connection so farmers
                              receive timely, actionable advice. Our mission is to reduce yield loss and promote sustainable,
                              affordable solutions for small and large farms alike.</p>
                              <a href="contact.py" data-i18n="about_contact">Contact Support</a> 
                           </div>
                        </div>
                     <div class="col-lg-6">
                        <div class="about-video-img"> <a href="#"><i class="fas fa-play"></i></a> <img src="images/aboutimg.jpg" alt=""> </div>
                     </div>
                  </div>
               </div>
            </div>
            <!--About Txt Video End--> 
            
            
            <!--Why you Need to Choose Ecova Start-->
            <div class="choose-ecova wf100 p80">
               <div class="container">
                  <div class="row">
                     <div class="col-lg-8">
                        <div class="section-title-2">
                           <h5>Why Farmers Trust Us</h5>
                           <h2>Practical Tools, Fast Support</h2>
                        </div>
                        <div class="row">
                           <div class="col-6">
                              <div class="eco-box">
                                 <span class="econ-icon"><i class="fas fa-images"></i></span>
                                 <h5> Image-based Guides </h5>
                                 <p>Clear photos and symptom charts help you identify problems quickly in the field.</p>
                              </div>
                           </div>
                           <div class="col-6">
                              <div class="eco-box">
                                 <span class="econ-icon"><i class="fas fa-headset"></i></span>
                                 <h5> Direct Support </h5>
                                 <p>Message admin, request callbacks, upload photos, or schedule site visits — all from one page.</p>
                              </div>
                           </div>
                           <div class="col-6">
                              <div class="eco-box">
                                 <span class="econ-icon"><i class="fas fa-leaf"></i></span>
                                 <h5> Sustainable Recommendations </h5>
                                 <p>We prefer integrated pest management and low-toxicity options when suitable.</p>
                              </div>
                           </div>
                           <div class="col-6">
                              <div class="eco-box">
                                 <span class="econ-icon"> <i class="fas fa-chart-line"></i> </span>
                                 <h5> Track Outcomes </h5>
                                 <p>Record treatments and results to improve future decision-making on your farm.</p>
                              </div>
                           </div>
                        </div>
                     </div>
                     <div class="col-lg-4">
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
            </div>
            <!--Why you Need to Choose Ecova End--> 
            
             
            <!--Partner Logos Section Start-->
            <div class="partner-logos wf100">
               <div class="container">
                  <div id="partner-logos" class="owl-carousel owl-theme">
                     <div class="item"><img src="images/plogo1.png" alt=""></div>
                     <div class="item"><img src="images/plogo2.png" alt=""></div>
                     <div class="item"><img src="images/plogo3.png" alt=""></div>
                     <div class="item"><img src="images/plogo4.png" alt=""></div>
                     <div class="item"><img src="images/plogo5.png" alt=""></div>
                     <div class="item"><img src="images/plogo1.png" alt=""></div>
                     <div class="item"><img src="images/plogo2.png" alt=""></div>
                     <div class="item"><img src="images/plogo3.png" alt=""></div>
                     <div class="item"><img src="images/plogo4.png" alt=""></div>
                     <div class="item"><img src="images/plogo5.png" alt=""></div>
                  </div>
               </div>
            </div>
            <!--Partner Logos Section End--> 
         </section>
         <!--About End--> 


""")
import footer