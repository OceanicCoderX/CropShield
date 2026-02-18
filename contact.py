#!C:/Python310/python.exe
import sys
import cgi
import cgitb
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

query = "SELECT * FROM company"

mycursor.execute(query)
myresult = mycursor.fetchone()
# print(myresult)

import header
print(f"""
         <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1 data-i18n="contact_title">Contact CropShield</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> Contact </a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End-->

         <!--Contact Start-->
         <section class="contact-page wf100 p80">
            <div class="container">
               <div class="row">
                  <div class="col-md-12">
                     <div class="section-title-2 text-center mb40">
                        <h5 data-i18n="contact_need_help">Need Help?</h5>
                        <h2 data-i18n="contact_get_in_touch">Get in touch with our agronomy team</h2>
                        <p class="lead" data-i18n="contact_lead">Whether it's a diagnosis, treatment guidance, bulk product order or a site visit,
                        choose the option that fits you. We typically respond within 24 hours.</p>
                     </div>
                  </div>

                  <div class="col-md-7">
                     <div class="contact-form mb60">
                        <h3 data-i18n="contact_general">General Contact</h3>
                        <form method="post" action="contact.py">
                           <ul class="cform">
                              <li class="half pr-15">
                                 <input type="text" name="name" class="form-control" placeholder="Full Name" required>
                              </li>
                              <li class="half pl-15">
                                 <input type="email" name="email" class="form-control" placeholder="Email" required>
                              </li>
                              <li class="half pr-15">
                                 <input type="text" name="phone" class="form-control" placeholder="Contact" required>
                              </li>
                              <li class="half pl-15">
                                 <input type="text" name="subject" class="form-control" placeholder="Subject">
                              </li>
                              <li class="full">
                                 <textarea name="message" class="textarea-control" placeholder="Message" required></textarea>
                              </li>
                              <li class="full">
                                 <input type="submit" value="Send Message" class="fsubmit">
                              </li>
                           </ul>
                        </form>
                     </div>

                     <div class="contact-form mb60">
                        <h3 data-i18n="contact_farmer_support">Farmer Support — Upload Photos for Diagnosis</h3>
                        <form method="post" action="contact.py" enctype="multipart/form-data">
                           <ul class="cform">
                              <li class="full">
                                 <input type="text" name="farm_name" class="form-control" placeholder="Farm / Farmer Name" required>
                              </li>
                              <li class="full">
                                 <input type="text" name="crop_type" class="form-control" placeholder="Crop (e.g. Tomato)" required>
                              </li>
                              <li class="full">
                                 <input type="file" name="photos" accept="image/*" class="form-control-file">
                                 <small class="small-note">Attach up to 3 images: close-up of symptoms + full plant + field view.</small>
                              </li>
                              <li class="full">
                                 <textarea name="notes" class="textarea-control" placeholder="Describe the problem, how long it has been happening, recent weather or treatments"></textarea>
                              </li>
                              <li class="full">
                                 <input type="submit" value="Send for Diagnosis" class="fsubmit">
                              </li>
                           </ul>
                        </form>
                     </div>
                  </div>

                  <div class="col-md-5">
                     <div class="contact-info mb30">
                        <h4 data-i18n="contact_quick_contacts">Quick Contacts</h4>
                        <address>
                           <p><strong>Office: &nbsp&nbsp</strong>{myresult[1]}</p>
                           <p><strong>Address: &nbsp&nbsp</strong>{myresult[5]}</p>
                           <p><strong>Support Phone: &nbsp&nbsp</strong>{myresult[4]}</p>
                           <p><strong>Email: &nbsp&nbsp</strong>{myresult[3]}</p>
                        </address>
                        <hr>
                        <h5 data-i18n="contact_services">Services</h5>
                        <ul>
                           <li>Rapid remote diagnosis (photo upload)</li>
                           <li>Callback from agronomy team</li>
                           <li>Bulk product orders and pricing</li>
                           <li>On-field visits and training</li>
                        </ul>
                        <hr>
                        <h5 data-i18n="contact_request_callback">Request a Callback</h5>
                        <form method="post" action="contact.py">
                           <div class="form-group">
                              <input type="text" name="cb_name" class="form-control" placeholder="Your name">
                           </div>
                           <div class="form-group">
                              <input type="tel" name="cb_phone" class="form-control" placeholder="Phone number">
                           </div>
                           <div class="form-group">
                              <input type="text" name="cb_when" class="form-control" placeholder="Best time to call">
                           </div>
                           <div class="form-group">
                              <input type="submit" class="btn btn-outline-success btn-block" value="Request Call" class="fsubmit">
                           </div>
                        </form>
                     </div>

                     <div class="google-map">
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11418.310112375979!2d-74.00986187433132!3d40.710981182716246!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew+York%2C+NY!5e0!3m2!1sen!2s!4v1540972202179" style="width:100%;height:240px;border:0;" allowfullscreen="" loading="lazy"></iframe>
                     </div>
                  </div>
               </div>
            </div>
         </section>
         <!--Contact End-->

""")
import footer