#!C:/Users/khush/AppData/Local/Programs/Python/Python310/python.exe
import sys
import cgi
import cgitb
import mysql.connector
cgitb.enable()
sys.stdout.reconfigure(encoding='utf-8')

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="cropshield",
    ssl_disabled=True,
    use_pure=True
)
mycursor = mydb.cursor()

form = cgi.FieldStorage()
fid = form.getvalue("fid")

import header

if fid:
  # Total queries
  mycursor.execute("SELECT COUNT(*) FROM farmerquery WHERE FId = %s", (fid,))
  total_queries = mycursor.fetchone()[0]

  # Recent queries (latest 6)
  mycursor.execute(f"SELECT FQId, FarmerName, CropName, PartName, SymptomsDetails, SImg, QueryStatus FROM farmerquery WHERE FId = {fid} ORDER BY FQId DESC LIMIT 6")
  recent_queries = mycursor.fetchall()

  # Recent crops viewed (fallback: crops from recent queries)
  mycursor.execute(f"SELECT c.CropName FROM farmerquery f JOIN crops c ON c.CropId = f.CropName WHERE FId = {fid} ORDER BY FQId DESC LIMIT 6")
  recent_crops = mycursor.fetchall()

  # Products suggested by admin: no explicit suggestions table found in repo.
  # Fallback: show latest products as "suggested" placeholder.
  mycursor.execute(f"SELECT r.SuggestProduct, p.Name, p.Image FROM product p JOIN replayquery r ON r.SuggestProduct = p.PId WHERE r.FQId = {recent_queries[0][0]} ORDER BY PId DESC LIMIT 6")
  suggested_products = mycursor.fetchall()

  # Quick crop categories
  mycursor.execute("SELECT CCId, Name FROM cropcategory ORDER BY Name LIMIT 12")
  crops = mycursor.fetchall()

  print(f"""
        
        <!--Inner Header Start-->
         <section class="wf100 p100 inner-header">
            <div class="container">
               <h1>Gallery</h1>
               <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="#"> My Dashboard </a></li>
               </ul>
            </div>
         </section>
         <!--Inner Header End--> 
         
      <div class="page-wrapper">
          <div class="container p-4"> <br>
              <div class="dashboard-header" style="margin-bottom:20px;">
                  <h2>Welcome back, Farmer!</h2>
                  <p>Here's your query dashboard and activity overview</p>
              </div>
              <div class="row" style="margin-top:20px;">
              <div class="col-md-5">
                  <div class="card">
                      <div class="card-body">
                          <h5>Total Queries Asked</h5>
                          <h2>{total_queries}</h2>
                          <a href="faq.py?fid={fid}">Ask New Query</a>
                      </div>
                  </div>
              </div>

              <div class="col-md-7">
                  <div class="card">
                      <div class="card-body">
                          <h5>Recent Queries & Responses</h5>
                          <ul style="list-style:none;padding-left:0;">
  """)

  if recent_queries:
      for q in recent_queries:
          fqid, farmername, crop, part, symptoms, simg, status = q
          # Build image path used elsewhere in project
          print(f"""
                              <li style=\"margin-bottom:12px;\"> 
                                  <div><strong>Query #</strong>  <small>({status})</small></div>
                                  <div style=\"font-size:90%\">{(symptoms[:160] + '...') if symptoms and len(symptoms)>160 else (symptoms or '')}</div>
                                  <div><a href="myhistory.py">View Details</a>
                                      <span> - <img src="html/ltr/assets/FqueryImg/{fqid}/{simg}" style=\"height:100px;\"></span>
                                  </div>
                              </li>
          """)
  else:
      print("                 <li>No recent queries found.</li>")

  print(f"""
                          </ul>
                      </div>
                  </div>
              </div>

              <div class="col-md-12">
                  <div class="card">
                      <div class="card-body">
                          <h5>Crops & Products Viewed Recently</h5>
  """)

  if recent_crops:
      for c in recent_crops:
          print(f"        <div style=\"padding:6px 0;\">{c[0]}</div>")
  else:
      print("             <div>No recent crops tracked. (Fallback: none)</div>")

  print(f"""
                      </div>
                  <hr>
                  <h6>Products Suggested by Admin</h6>
                  <div style="display:flex; flex-wrap:wrap; gap:8px;">
  """)

  if suggested_products:
      for p in suggested_products:
          pid, pname, pimg = p
          print(f"""      <div style=\"width:45%;\">
                              <a href=\"product.py?pid={pid}\">
                                  <img src="html/ltr/assets/Product/{pid}/{pimg}" style="width:100%;height:80px;object-fit:cover;">
                                  <div>{pname}</div>
                              </a>
                          </div>
                """)
  else:
      print("<div>No admin suggestions available.</div>")

  print(f"""
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="container p-4" style="margin-top:20px;"> 
            <div class="row">
              <div class="col-md-6"> 
                <div class="card"> 
                  <div class="card-body"> 
                    <h5>Submit Feedback</h5>
                    <form action="FeedBackEnd.py" method="POST"> 
                      <div class="form-group"> 
                        <input type=\"email\" name=\"email\" class=\"form-control\" placeholder=\"Your registered email\" required> 
                      </div> 
                      <div class=\"form-group\"> 
                        <label>Rating</label>
                        <select name=\"rating\" class=\"form-control\"> 
                          <option value=\"5\">5</option>
                          <option value=\"4\">4</option>
                          <option value=\"3\">3</option>
                          <option value=\"2\">2</option>
                          <option value=\"1\">1</option>
                        </select>
                      </div>
                      <div class=\"form-group\"> 
                        <textarea name=\"message\" class=\"form-control\" placeholder=\"Your feedback\" required></textarea>
                      </div>
                      <input type=\"hidden\" name=\"fid\" value=\"{fid}\"> 
                      <button class=\"btn btn-primary\">Submit Feedback</button>
                    </form>
                  </div>
                </div>
              </div>

              <div class=\"col-md-6\"> 
                <div class=\"card\"> 
                  <div class=\"card-body\"> 
                    <h5>Quick Crop Categories</h5>
                    <div style=\"display:flex;flex-wrap:wrap;gap:8px;\"> 
  """)

  if crops:
      for crop in crops:
          cid, cname = crop
          print(f"<a href=\"crops.py?CCId={cid}&fid={fid}\" style=\"padding:8px 10px;border:1px solid #ddd;border-radius:4px;text-decoration:none;color:#333;\">{cname}</a>")
  else:
      print("<div>No crop categories available.</div>")

  print(f"""
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
  """)

else:
  print("""
      <script>
        alert(" You are not logged In, Login First!");
        location.href="index.py";
      </script>
  """)
import footer
