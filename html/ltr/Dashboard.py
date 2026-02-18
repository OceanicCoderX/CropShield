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

# Counts
mycursor.execute("SELECT COUNT(*) FROM farmerlogin")
total_farmers = mycursor.fetchone()[0]
mycursor.execute("SELECT COUNT(*) FROM cropcategory")
total_crop_categories = mycursor.fetchone()[0]
mycursor.execute("SELECT COUNT(*) FROM crops")
total_crops = mycursor.fetchone()[0]
mycursor.execute("SELECT COUNT(*) FROM diseases")
total_diseases = mycursor.fetchone()[0]

# Farmer Queries counts
mycursor.execute("SELECT COUNT(*) FROM farmerquery")
total_queries = mycursor.fetchone()[0]
mycursor.execute("SELECT COUNT(*) FROM farmerquery WHERE QueryStatus IN ('Panding')")
pending_queries = mycursor.fetchone()[0]
mycursor.execute("SELECT COUNT(*) FROM farmerquery WHERE QueryStatus IN ('Replied')")
resolved_queries = mycursor.fetchone()[0]

# Recent feedbacks
mycursor.execute("SELECT f.FId, f.Image, f.Name, fb.FeedBack, fb.Star FROM feedback fb JOIN farmerlogin f ON f.FId = fb.FId ORDER BY fb.FId DESC LIMIT 4")
recent_feedbacks = mycursor.fetchall()


# Products by category
mycursor.execute("SELECT pc.Name, COUNT(p.PId) FROM product p JOIN productcategory pc ON p.PCId = pc.PCId GROUP BY pc.PCId, pc.Name")
prod_by_cat = mycursor.fetchall()

# Check for date-like column to compute registrations (week/month)
mycursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=%s AND TABLE_NAME=%s AND DATA_TYPE IN ('datetime','timestamp','date')", ('cropshield','farmerlogin'))
date_cols = mycursor.fetchall()
reg_stats = None
if date_cols:
    reg_col = date_cols[0][0]
    mycursor.execute(f"SELECT COUNT(*) FROM farmerlogin WHERE DATE({reg_col}) >= CURDATE() - INTERVAL 6 DAY")
    reg_last7 = mycursor.fetchone()[0]
    mycursor.execute(f"SELECT COUNT(*) FROM farmerlogin WHERE DATE({reg_col}) >= CURDATE() - INTERVAL 29 DAY")
    reg_last30 = mycursor.fetchone()[0]
    mycursor.execute(f"SELECT DATE({reg_col}) as d, COUNT(*) FROM farmerlogin WHERE DATE({reg_col}) >= CURDATE() - INTERVAL 6 DAY GROUP BY d ORDER BY d")
    reg_daily = mycursor.fetchall()
    reg_stats = (reg_last7, reg_last30, reg_daily)

import header

print(f"""
        <div class="page-wrapper">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-3">
                <div class="card p-3 text-center">
                  <h5>Total Farmers</h5>
                  <h2>{total_farmers}</h2>
                </div>
              </div>
              <div class="col-md-3">
                <div class="card p-3 text-center">
                  <h5>Crop Categories</h5>
                  <h2>{total_crop_categories}</h2>
                </div>
              </div>
              <div class="col-md-3">
                <div class="card p-3 text-center">
                  <h5>Total Crops</h5>
                  <h2>{total_crops}</h2>
                </div>
              </div>
              <div class="col-md-3">
                <div class="card p-3 text-center">
                  <h5>Total Diseases</h5>
                  <h2>{total_diseases}</h2>
                </div>
              </div>
            </div>

            <div class="row mt-4">
              <div class="col-md-4">
                <div class="card p-3">
                  <h6>Farmer Queries</h6>
                  <p>Total: {total_queries}</p>
                  <p>Pending: {pending_queries} &nbsp; Resolved/Replied: {resolved_queries}</p>
                  <canvas id="queriesChart" width="400" height="300"></canvas>
                </div>
              </div>
              <div class="col-md-8">
                <div class="card p-3">
                  <h6>Products by Category</h6>
                  <canvas id="prodCatChart" width="800" height="300"></canvas>
                </div>
              </div>
            </div>
                              
                    
            <div class="row mt-4">
              <div class="col-lg-6">
                <div class="card">
                  <div class="card-body">
                      <h4 class="card-title">Recent Feedbacks</h4>
                  </div>
""")

print("""
  <style>
      .fa-star {color: #ccc; font-size:15px;}
      .checked {color: #2962ff;}
  </style>
""")

for fid, img, name, msg, star in recent_feedbacks:
    stars = ''
    for i in range(5):
        if i < star:
            stars += '<span class="fa fa-star checked"></span>'  # filled star
        else:
            stars += '<span class="fa fa-star"></span>'  # empty star

    print(f"""
                  <div class="comment-widgets scrollable" style="padding:5px;">
                    <!-- Comment Row -->
                    <div class="d-flex flex-row comment-row m-t-0">
                      <div class="p-2"><img src="assets/userImg/{fid}/{img}" alt="user" width="50" class="rounded-circle"></div>
                      <div class="comment-text w-100">
                        <h6 class="font-medium">{name}</h6>
                        <span class="m-b-15 d-block">{msg}</span>
                        <div class="comment-footer">
                          <span class="text-muted float-right">April 14, 2016</span> 
                          <span class="label">{stars}</span> 
                        </div>
                      </div>
                    </div>
                  </div>
    """)

print("""
                    
                </div>
              </div>
        
              <div class="col-md-6">
                <div class="card p-3">
                  <h6>New Registrations</h6> <br><br>
""")

if reg_stats:
    reg_last7, reg_last30, reg_daily = reg_stats
    # Fetch last 30 days data for chart
    mycursor.execute(f"SELECT DATE({reg_col}) as d, COUNT(*) FROM farmerlogin WHERE DATE({reg_col}) >= CURDATE() - INTERVAL 29 DAY GROUP BY d ORDER BY d")
    reg_daily_30 = mycursor.fetchall()
    reg_labels_7 = [str(d) for d, c in reg_daily]
    reg_values_7 = [c for d, c in reg_daily]
    reg_labels_30 = [str(d) for d, c in reg_daily_30]
    reg_values_30 = [c for d, c in reg_daily_30]
    # Use simple numeric labels 1..N for chart x-axis instead of date strings
    reg_idx_7 = [str(i+1) for i in range(len(reg_labels_7))]
    reg_idx_30 = [str(i+1) for i in range(len(reg_labels_30))]

    print("""
    <div class='mb-2'>
      <button id='btn7' class='btn btn-sm btn-success' onclick='showRegChart(7)'>Last 7 Days</button>
      <button id='btn30' class='btn btn-sm btn-outline-success' onclick='showRegChart(30)'>Last 30 Days</button>
    </div>
    <canvas id='regChart' width='400' height='200'></canvas>
    <script src='https://cdn.jsdelivr.net/npm/chart.js'></script>
    <script>
      const regLabels7 = [%s];
      const regValues7 = [%s];
      const regLabels30 = [%s];
      const regValues30 = [%s];
      let regChart;
      function showRegChart(days) {
        let labels = days === 7 ? regLabels7 : regLabels30;
        let values = days === 7 ? regValues7 : regValues30;
        if (regChart) regChart.destroy();
        // compute suggested max for y-axis (at least 3)
        const maxVal = values.length ? Math.max(...values) : 3;
        const suggestedMax = Math.max(3, Math.ceil(maxVal + 1));
        regChart = new Chart(document.getElementById('regChart'), {
          type: 'line',
          data: {
            labels: labels,
            datasets: [{
              label: 'Registrations',
              data: values,
              borderColor: '#2962ff',
              backgroundColor: 'rgba(41,98,255,0.2)',
              fill: true,
              tension: 0.3,
              pointBackgroundColor: '#2962ff',
              pointRadius: 5
            }]
          },
          options: {
            scales: {
              x: { ticks: { autoSkip: false } },
              y: { beginAtZero: true, suggestedMax: suggestedMax, ticks: { stepSize: 1 } }
            },
            plugins: { legend: { display: true } }
          }
        });
        document.getElementById('btn7').className = days === 7 ? 'btn btn-sm btn-success' : 'btn btn-sm btn-outline-success';
        document.getElementById('btn30').className = days === 30 ? 'btn btn-sm btn-success' : 'btn btn-sm btn-outline-success';
      }
      showRegChart(7);
    </script>
  """ % (
    ','.join([f"'{lbl}'" for lbl in reg_labels_7]),
    ','.join([str(v) for v in reg_values_7]),
    ','.join([f"'{lbl}'" for lbl in reg_labels_30]),
    ','.join([str(v) for v in reg_values_30])
  ))
else:
    print('<p>No registration date column found in `farmerlogin`. Weekly/monthly stats not available.</p>')

print("""
                </div>
              </div>
            </div>
          </div>
        </div>
""")

labels = ','.join([f"'{x[0]}'" for x in prod_by_cat])
values = ','.join([str(x[1]) for x in prod_by_cat])
js = """
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script>
          const queriesData = [%d, %d];
          new Chart(document.getElementById('queriesChart'), {
            type: 'doughnut',
            data: { labels: ['Pending','Resolved'], datasets: [{ data: queriesData, backgroundColor: ['#f39c12','#27ae60'] }] }
          });
          const prodLabels = [%s];
          const prodValues = [%s];
          new Chart(document.getElementById('prodCatChart'), {
            type: 'bar',
            data: { labels: prodLabels, datasets: [{ label: 'Products', data: prodValues, backgroundColor: '#3498db' }] },
            options: { scales: { y: { beginAtZero: true } } }
          });
        </script>
""" % (pending_queries, resolved_queries, labels, values)

print(js)

import footer
