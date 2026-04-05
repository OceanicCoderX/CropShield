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

    if total_queries:
        

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

        print("""
            <style>
                body { background: #f5f5f5; }
                .dashboard-page { padding: 30px 0; }
                
                /* Product Styles */
                .product-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                    gap: 20px;
                    margin-top: 15px;
                }
                .product-card {
                    background: white;
                    border: 1px solid #eee;
                    border-radius: 8px;
                    overflow: hidden;
                    text-decoration: none;
                    transition: all 0.3s;
                    display: block;
                }
                .product-card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                }
                .product-img {
                    width: 100%;
                    height: 200px;
                    object-fit: cover;
                    display: block;
                }
                .product-name {
                    padding: 12px;
                    color: #2d5a27;
                    font-weight: 500;
                    text-align: center;
                }

                /* Form Styles */
                .form-control {
                    width: 100%;
                    padding: 12px;
                    margin-bottom: 15px;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    font-size: 14px;
                }
                .form-control:focus {
                    border-color: #2d5a27;
                    outline: none;
                }
                select.form-control {
                    appearance: none;
                    background-image: url("data:image/svg+xml,<svg fill='%232d5a27' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/></svg>");
                    background-repeat: no-repeat;
                    background-position: right 10px center;
                    padding-right: 30px;
                }
                textarea.form-control {
                    min-height: 100px;
                    resize: vertical;
                }
                .submit-btn {
                    width: 100%;
                    padding: 14px;
                    background: #2d5a27;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    font-weight: 600;
                    font-size: 16px;
                    cursor: pointer;
                    transition: all 0.3s;
                }
                .submit-btn:hover {
                    background: #234820;
                    transform: translateY(-2px);
                }
                .page-title { 
                    color: #2d5a27;
                    font-size: 32px;
                    font-weight: bold;
                    margin-bottom: 5px;
                }
                .page-subtitle {
                    color: #666;
                    font-size: 16px;
                    margin-bottom: 30px;
                }
                .stats-card {
                    background: #2d5a27;
                    color: white;
                    border-radius: 12px;
                    padding: 30px;
                    text-align: center;
                    margin-bottom: 30px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                }
                .stats-title {
                    color: white;
                    font-size: 20px;
                    margin-bottom: 15px;
                    font-weight: 500;
                }
                .stats-number {
                    font-size: 72px;
                    font-weight: bold;
                    margin-bottom: 20px;
                    line-height: 1;
                }
                .query-btn {
                    background: #90be6d;
                    color: white;
                    padding: 12px 24px;
                    border-radius: 8px;
                    text-decoration: none;
                    display: inline-block;
                    transition: all 0.3s;
                    font-size: 16px;
                }
                .query-btn:hover {
                    background: #7aa95c;
                    transform: translateY(-2px);
                }
                .white-card {
                    background: white;
                    border-radius: 12px;
                    padding: 25px;
                    margin-bottom: 30px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                }
                .card-title {
                    color: #2d5a27;
                    font-size: 20px;
                    font-weight: 500;
                    margin-bottom: 20px;
                    display: flex;
                    align-items: center;
                    gap: 10px;
                }
                .query-item {
                    border-bottom: 1px solid #eee;
                    padding: 15px 0;
                }
                .query-item:last-child {
                    border-bottom: none;
                }
                .query-header {
                    display: flex;
                    align-items: center;
                    margin-bottom: 10px;
                }
                .query-number {
                    color: #2d5a27;
                    font-weight: 600;
                    margin-right: 10px;
                }
                .query-status {
                    background: #e8f3e5;
                    color: #2d5a27;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-size: 13px;
                }
                .query-text {
                    color: #666;
                    margin-bottom: 10px;
                    line-height: 1.5;
                }
                .view-details {
                    color: #90be6d;
                    text-decoration: none;
                    font-weight: 500;
                }
                .view-details:hover {
                    color: #2d5a27;
                }
                .crop-tag {
                    background: #f8f9fa;
                    padding: 8px 16px;
                    border-radius: 8px;
                    color: #2d5a27;
                    text-decoration: none;
                    display: inline-block;
                    margin: 5px;
                    transition: all 0.3s;
                }
                .crop-tag:hover {
                    background: #e8f3e5;
                }
            </style>

        """)
        print(f"""
            <div class="dashboard-page">
                <div class="container">
                    <h1 class="page-title">Welcome back, Farmer!</h1>
                    <p class="page-subtitle">Here's your query dashboard and activity overview</p>
                    <div class="row">
                    <div class="col-md-4">
                        <div class="stats-card">
                            <h4 class="stats-title">TOTAL QUERIES ASKED</h4>
                            <div class="stats-number">{total_queries}</div>
                            <a href="faq.py?fid={fid}" class="query-btn">+ Ask New Query</a>
                        </div>
                    </div>

                    <div class="col-md-8">
                        <div class="white-card">
                            <h3 class="card-title">ðŸ“ Recent Queries & Responses</h3>
                            <div class="query-list">
        """)

        if recent_queries:
            for q in recent_queries:
                fqid, farmername, crop, part, symptoms, simg, status = q
                # Build image path used elsewhere in project
                print(f"""
                                    <div class="query-item">
                                        <div class="query-header">
                                            <span class="query-number">Query #{fqid}</span>
                                            <span class="query-status">{status}</span>
                                        </div>
                                        <p class="query-text">{(symptoms[:160] + '...') if symptoms and len(symptoms)>160 else (symptoms or '')}</p>
                                        <a href="myhistory.py?fid={fid}" class="view-details">View Details â†’</a>
                                    </div>
                """)
        else:
            print("                 <li>No recent queries found.</li>")

        print(f"""
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="col-md-12">
                        <div class="white-card">
                            <h3 class="card-title">ðŸŒ¾ Crops Viewed Recently</h3>
        """)

        if recent_crops:
            for c in recent_crops:
                print(f"        <a href=\"#\" class=\"crop-tag\">{c[0]}</a>")
        else:
            print("             <div>No recent crops viewed</div>")

        print(f"""
                            </div>
                        </div>
                    </div>

                    <div class="col-md-12">
                        <div class="white-card">
                            <h3 class="card-title">ðŸ›ï¸ Products Suggested by Admin</h3>
                            <div class="product-grid">
        """)

        if suggested_products:
            for p in suggested_products:
                pid, pname, pimg = p
                print(f"""      
                                <a href="details.py?pid={pid}" class="product-card">
                                    <img src="html/ltr/assets/Product/{pid}/{pimg}" class="product-img">
                                    <div class="product-name">{pname}</div>
                                </a>
                        """)
        else:
            print("<div>No admin suggestions available.</div>")

        print(f"""
                        </div>
                        </div>
                    </div>
                    </div>
                </div>

                <div class="container"> 
                    <div class="row">
                    <div class="col-md-6"> 
                        <div class="white-card"> 
                            <h3 class="card-title">ðŸ’­ Submit Feedback</h3>
                            <form action="FeedBackEnd.py" method="POST"> 
                                <input type="email" name="email" class="form-control" placeholder="Your Email" required>
                                <select name="rating" class="form-control">
                                    <option value="">Select Rating</option>
                                    <option value="5">â­â­â­â­â­ Excellent</option>
                                    <option value="4">â­â­â­â­ Very Good</option>
                                    <option value="3">â­â­â­ Good</option>
                                    <option value="2">â­â­ Fair</option>
                                    <option value="1">â­ Poor</option>
                                </select>
                                <textarea name="message" class="form-control" placeholder="Share your experience with us..." rows="4" required></textarea>
                                <input type="hidden" name="fid" value="{fid}">
                                <button type="submit" class="submit-btn">SUBMIT FEEDBACK</button>
                            </form>
                        </div>
                    </div>

                    <div class="col-md-6"> 
                        <div class="white-card"> 
                            <h3 class="card-title">ðŸŒ± Quick Crop Categories</h3>
                            <div style="display: flex; flex-wrap: wrap; gap: 10px;"> 
        """)

        if crops:
            for crop in crops:
                cid, cname = crop
                print(f"<a href=\"crops.py?CCId={cid}&fid={fid}\" class=\"crop-tag\">{cname}</a>")
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
        print(f"""
            <script>
                alert(" No Queries Found, Please Ask Your Query!");
                location.href="faq.py?fid={fid}";
            </script>
        """)

else:
  print("""
      <script>
        alert(" You are not logged In, Login First!");
        location.href="index.py";
      </script>
  """)
import footer
