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

form = cgi.FieldStorage()
fid = form.getvalue("fid")

if fid:
   Far_query = f"SELECT Name FROM farmerlogin WHERE FId ={fid}"
   mycursor.execute(Far_query)
   FarmerName = mycursor.fetchall()

   crop_query = "SELECT * FROM crops"
   mycursor.execute(crop_query)
   crop = mycursor.fetchall()

   crop_op= ""
   part_op= ""

   for cp in crop:
      crop_op += f'''
      <option value="{cp[0]}">{cp[3]}</option>
      '''

      part_query = f"SELECT * FROM parts WHERE CrpId = {cp[0]}"
      mycursor.execute(part_query)
      croppart = mycursor.fetchall()
      for part in croppart:
         part_op += f'''
         <option value="{part[0]}" data-cropid="{cp[0]}">{part[2]}</option>
         '''

   import header
   print("""
         
         <style>
      /* Page-local tweaks for a nicer FAQ look */
      .faq-section .card-header {
         background: #f3faf4;
         border: none;
         padding: 0;
      }

      .faq-section .card-header h5 button {
         width: 100%;
         text-align: left;
         padding: 18px 20px;
         font-size: 16px;
         color: #234d2a;
         background: transparent;
         border: 0;
         box-shadow: none;
      }

      .faq-section .card-body {
         background: #fff;
         padding: 18px 20px;
         color: #444;
      }

      .inner-header h1 {
         color: #fff;
      }

      .connect-panel {
         background: #f7fff7;
         border: 1px solid #e6f4ea;
         padding: 18px;
         border-radius: 6px;
      }

      @media (max-width: 767.98px) {
         .faq-section .card-header h5 button {
         font-size: 15px;
         padding: 14px 16px;
         }
      }

      .small-note {font-size:13px;color:#6b6b6b}
   </style>
         
         """)
   print(f"""
            <!--Inner Header Start-->
            <section class="wf100 p100 inner-header">
               <div class="container">
                  <h1 data-i18n="faq_title">Solar & Wind Energies</h1>
                  <ul>
                     <li><a href="#" data-i18n="breadcrumb_home">Home</a></li>
                     <li><a href="#" data-i18n="breadcrumb_faq">FAQ</a></li>
                  </ul>
               </div>
            </section>
            <!--Inner Header End--> 
            
   """)
      
   mycursor.execute("SELECT * FROM replayquery WHERE Position = 'public' LIMIT 6")
   public_query = mycursor.fetchall()
   
   query = ''
   for x in public_query:
      query += f'''
                        <div class="card">
                           <div class="card-header" id="faqHeadingOne">
                              <h5 class="mb-0">
                              <button class="btn btn-link" data-toggle="collapse" data-target="#faqOne" aria-expanded="true" aria-controls="faqOne">
                                 {x[2]}
                              </button>
                              </h5>
                           </div>
                           <div id="faqOne" class="collapse show" aria-labelledby="faqHeadingOne" data-parent="#faqAccordion">
                              <div class="card-body">
                              {x[3]}
                              </div>
                           </div>
                        </div>
      '''
         
      
   print(f"""          
            
            <!-- FAQ Section -->
            <section class="wf100 p80 faq-section">
               <div class="container">
                  <div class="row">
                     <div class="col-lg-7">
                        <div class="section-title-2">
                           <h5>Got Questions?</h5>
                           <h2>We’re Here To Help</h2>
                           <p class="lead">Below are answers to the questions we get asked most often. If you still need help, please
                              <a href="contact.py">contact us</a>.</p>
                        </div>

                        <div id="faqAccordion" class="accordion">
                           {query}

                     </div>
                     
                     <br><br><br>
                     
                     <div class="contact-form mb60">
                        <h3>Farmer Support — Upload Photos for Diagnosis</h3>
                        <form method="post" action="faqBackEnd.py" enctype="multipart/form-data">
                           <ul class="cform">
                              <li class="full">
                                 <input type="tel" name="fid" id="fid" value="{fid}" hidden>
                                 <input type="text" name="FarmerName" id="FarmerName" class="form-control" placeholder="Your Name" required>
                              </li>
                              <li class="full">
                                 <select class="form-control" id="CropName" name="CropName" onchange="filterCropParts()" required>
                                    <option value="">- Select Crop -</option>
                                    {crop_op}
                                 </select>
                              </li>
                              <li class="full">
                                 <input type="file" name="sImg" id="sImg" accept="image/*" class="form-control-file">
                                 <small class="small-note">Attach up to 3 images: close-up of symptoms + full plant + field view.</small>
                              </li>
                              <li class="full">
                                 <select class="form-control" id="PartName" name="PartName" required>
                                    <option value="">- Select Crop Part -</option>
                                    {part_op}
                                 </select>
                              </li>
                              <li class="full">
                                 <textarea name="symtomes" id="symtomes" class="textarea-control" placeholder="Describe the problem, how long it has been happening, recent weather or treatments" required></textarea>
                              </li>
                              <li class="full">
                                 <input type="submit" value="Send for Diagnosis" class="fsubmit">
                              </li>
                           </ul>
                        </form>
                     </div> 
                  </div>

                  <div class="col-lg-5">
                     <div class="connect-panel">
                     <h4>Connect with Admin</h4>
                     <p class="small-note">Choose how you'd like to reach the admin. Farmers can send messages, request a call,
                        upload images for diagnosis, or schedule a site visit.</p>

                     <!-- Quick Message Form (posts to contact.py or can be hooked to backend) -->
                     <form id="quickMessage" method="post" action="contact.py" enctype="multipart/form-data">
                        <input type="hidden" name="source" value="faq_quick_message">
                        <div class="form-group">
                           <label class="small-note">Full name</label>
                           <input type="text" name="name" class="form-control"  placeholder="Your Name" required>
                        </div>
                        <div class="form-group">
                           <label class="small-note">Phone or Email</label>
                           <input type="text" name="contact" class="form-control" placeholder="Phone or email" required>
                        </div>
                        <div class="form-group">
                           <label class="small-note">Message</label>
                           <textarea name="message" class="form-control" placeholder="Brief message for admin" rows="3"
                           required></textarea>
                        </div>
                        <div class="form-group">
                           <button type="submit" class="btn btn-success btn-block">Send Message</button>
                        </div>
                     </form>

                     <hr>

                     <!-- Request Callback -->
                     <form id="requestCall" method="post" action="contact.py">
                        <input type="hidden" name="source" value="faq_request_call">
                        <div class="form-group">
                           <label class="small-note">Request a call</label>
                           <input type="text" name="call_name" class="form-control"  placeholder="Your Name">
                        </div>
                        <div class="form-group">
                           <input type="tel" name="call_phone" class="form-control" placeholder="Best phone number">
                        </div>
                        <div class="form-group">
                           <label class="small-note">Preferred time</label>
                           <input type="text" name="call_time" class="form-control" placeholder="e.g. Tomorrow morning">
                        </div>
                        <div class="form-group">
                           <button type="submit" class="btn btn-outline-success btn-block">Request Callback</button>
                        </div>
                     </form>

                     <hr>

                     <!-- Upload images for diagnosis -->
                     <form id="uploadImages" method="post" action="contact.py" enctype="multipart/form-data">
                        <input type="hidden" name="source" value="faq_upload_images">
                        <div class="form-group">
                           <label class="small-note">Upload photos</label>
                           <input type="file" name="photos" accept="image/*" class="form-control-file">
                           <small class="small-note">Attach clear close-up and wide shots (up to 3 images).</small>
                        </div>
                        <div class="form-group">
                           <label class="small-note">Brief notes</label>
                           <input type="text" name="photo_notes" class="form-control" placeholder="Short notes about problem">
                        </div>
                        <div class="form-group">
                           <button type="submit" class="btn btn-outline-success btn-block">Send Photos</button>
                        </div>
                     </form>

                     <hr>

                     <!-- Schedule Visit (simple form) -->
                     <form id="scheduleVisit" method="post" action="contact.py">
                        <input type="hidden" name="source" value="faq_schedule_visit">
                        <div class="form-group">
                           <label class="small-note">Schedule a site visit</label>
                           <input type="text" name="visit_name" class="form-control"  placeholder="Your Name" placeholder="Your Name">
                        </div>
                        <div class="form-group">
                           <input type="text" name="visit_phone" class="form-control" placeholder="Contact number">
                        </div>
                        <div class="form-group">
                           <input type="text" name="visit_date" class="form-control" placeholder="Preferred date (YYYY-MM-DD)">
                        </div>
                        <div class="form-group">
                           <select name="visit_timeframe" class="form-control">
                           <option value="morning">Morning</option>
                           <option value="afternoon">Afternoon</option>
                           <option value="evening">Evening</option>
                           </select>
                        </div>
                        <div class="form-group">
                           <button type="submit" class="btn btn-success btn-block">Request Visit</button>
                        </div>
                     </form>

                     </div>
                  </div>

               </div>
               </div>
            </section>   
            
   """)

   print("""

      <script>
      window.onload = function() {
         filterCropParts(); // hide irrelevant parts on page load
      };

         function filterCropParts() {
         const cropId = document.getElementById('CropName').value;
         const cropParts = document.getElementById('PartName');
         const options = cropParts.querySelectorAll('option');
         console.log(options)

         // reset selection
         cropParts.value = "";

         options.forEach(option => {
               const relatedCropId = option.getAttribute('data-cropid');
               if (!relatedCropId) return; // skip placeholder option

               // Show or hide based on selected crop ID
               if (relatedCropId === cropId) {
               option.style.display = "block";
               option.disabled = false;
               } else {
               option.style.display = "none";
               option.disabled = true;
               }
         });
         }
      </script>

   """)

   import footer

else:
    print(f'''
        <script>
        alert(" You are not logged In, Login First!");
        location.href="index.py";
        </script>''')
