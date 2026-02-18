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

query = """SELECT f.FId, f.Name, f.Image, fb.FeedBack, fb.Star FROM feedback fb JOIN farmerlogin f ON f.FId = fb.FId"""
mycursor.execute(query)
myresult = mycursor.fetchall()
# print(myresult)

print("""
      <style>
         .fa-star {color: #ccc; font-size:15px;}
         .checked {color: green;}
      </style>
      """)
fb_loop = ''
for x in myresult:
      stars_html = ''
      for i in range(5):
         if i < x[4]:
               stars_html += '<span class="fa fa-star checked"></span>'  # filled star
         else:
               stars_html += '<span class="fa fa-star"></span>'  # empty star

      fb_loop += f"""
         <div class="item">
               <p>{x[3]}</p>
               <div class="tuser">
                  <img src="html/ltr/assets/userImg/{x[0]}/{x[2]}" alt="">
                  <strong>{x[1]}</strong>
                  <div class="rating" aria-hidden="true">{stars_html}</div>
               </div>
         </div>
    """

import header
print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1 data-i18n="testimonials_title">Testimonials</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> Testimonials </a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End-->
         
         <!--Testimonials Start-->
         <section class="testimonials-section wf100 p80">
            <div class="container">
                  <div class="section-title-2 text-center">
                  <h5 data-i18n="testimonials_what_people">What People Say</h5>
                  <h2 data-i18n="testimonials_real_feedback">Real Farmer Feedback</h2>
               </div>
               <div class="row">
                  <div class="col-md-12">
                     <div id="h3testimonials" class="owl-carousel owl-theme">
                        <!--testimonial item-->
                        {fb_loop}
                     </div>
                  </div>
               </div>
            </div>
         </section>
         <!--Testimonials End-->

         <!--Feedback / Contact Start-->
         <section class="contact-page wf100 p80">
            <div class="container">
               <div class="row">
                  <div class="col-md-8">
                     <div class="contact-form mb60">
                        <h3 data-i18n="feedback_share">Share Your Feedback</h3>
                        <form method="post" action="FeedBackEnd.py">
                           <ul class="cform">
                              <li class="half pr-15">
                                 <input type="text" name="name" id="name" class="form-control" placeholder="Full Name" data-i18n-placeholder="ph_full_name" required>
                              </li>
                              <li class="half pl-15">
                                 <input type="email" name="email" id="email" class="form-control" placeholder="Email" data-i18n-placeholder="ph_email" required>
                              </li>
                              <li class="full">
                                 <label class="small-note">Your rating</label>
                                 <select name="rating" id="rating" class="form-control">
                                    <option value="5">5 - Excellent</option>
                                    <option value="4">4 - Good</option>
                                    <option value="3">3 - Fair</option>
                                    <option value="2">2 - Poor</option>
                                    <option value="1">1 - Very Poor</option>
                                 </select>
                              </li>
                              <li class="full">
                                 <textarea name="message" id="message" class="textarea-control" placeholder="Your feedback" data-i18n-placeholder="ph_your_feedback" required></textarea>
                              </li>
                              <li class="full">
                                 <button type="submit" class="fsubmit" data-i18n-value="btn_send_feedback">Send Feedback</button>
                              </li>
                           </ul>
                        </form>
                     </div>
                  </div>
                  <div class="col-md-4">
                     <div class="contact-info mb30">
                        <h4 data-i18n="why_share">Why share?</h4>
                        <p class="small-note" data-i18n="why_share_note">Your feedback helps other farmers and helps us improve CropShield. Selected
                        testimonials may be shown on this page (with your consent).</p>
                        <hr>
                        <h5 data-i18n="guidelines">Guidelines</h5>
                        <ul>
                           <li data-i18n="guide_keep_short">Keep feedback short and specific.</li>
                           <li data-i18n="guide_include_crop">Include crop and location if possible.</li>
                           <li data-i18n="guide_no_sensitive">Do not include personal ID numbers or sensitive data.</li>
                        </ul>
                     </div>
                  </div>
               </div>
            </div>
         </section>
         <!--Feedback / Contact End-->
""")
print("""
         <style>
         /* small styles for testimonials */
         .testimonials-section .tuser { display:flex; align-items:center; gap:10px; margin-top:12px; }
         .testimonials-section .tuser img { width:48px; height:48px; border-radius:50%; object-fit:cover; }
         .testimonials-section .rating { color:#f5b301; font-size:18px; margin-left:8px; }
         .contact-page .small-note { color:#6b6b6b }
         </style>

      
""")
import footer