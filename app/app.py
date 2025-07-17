from flask import Flask, request, jsonify, render_template_string
import random
import os

app = Flask(__name__)

request_counts = {}

@app.route('/packet', methods=['POST'])
def packet():
    data = request.json
    latency = round(random.uniform(1, 5), 2)
    pod_id = os.environ.get('HOSTNAME', 'unknown-pod')

    request_counts[pod_id] = request_counts.get(pod_id, 0) + 1

    print(f"Received packet from pod {pod_id}: ID={data.get('id')} Latency={latency}ms")
    return jsonify({"status": "processed", "latency_ms": latency, "pod_id": pod_id})

@app.route('/stats', methods=['GET'])
def stats():
    return jsonify(request_counts)

@app.route('/')
def dashboard():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Packet Inspector Dashboard</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          margin: 0; 
          height: 100vh;
          display: flex;
          flex-direction: column;
        }
        header {
          padding: 10px 20px;
          display: flex;
          align-items: center;
        }
        header img {
          height: 100px;
        }
        main {
          flex-grow: 1;
          display: flex;
          justify-content: center;
          align-items: center;
        }
        table {
          border-collapse: collapse;
          width: 300px;
        }
        th, td {
          border: 1px solid #ddd;
          padding: 8px;
          text-align: center;
        }
        th {
          background-color: #f2f2f2;
        }
      </style>
    </head>
    <body>
      <header>
        <img src="/static/ericsson-logo.png" alt="Ericsson Logo" />
      </header>
      <main>
        <div>
          <h2 style="text-align:center;">Packet Inspector Pod Request Counts</h2>
          <table>
            <thead><tr><th>Pod ID</th><th>Requests</th></tr></thead>
            <tbody id="stats-body"></tbody>
          </table>
        </div>
      </main>

      <script>
        async function fetchStats() {
          const res = await fetch('/stats');
          const data = await res.json();
          const tbody = document.getElementById('stats-body');
          tbody.innerHTML = '';
          for (const [pod, count] of Object.entries(data)) {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${pod}</td><td>${count}</td>`;
            tbody.appendChild(row);
          }
        }
        setInterval(fetchStats, 2000);
        fetchStats();
      </script>
    </body>
    </html>
    '''
    return render_template_string(html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
