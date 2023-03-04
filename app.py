from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  job_list = load_jobs_from_db()
  return render_template("home.html", jobs = job_list, company_name = 'Topmate')

@app.route("/api/jobs")
def list_jobs():
  job_list = load_jobs_from_db()
  return jsonify(job_list)

@app.route("/job/<id>")
def list_jobs(id):
  job = load_job_from_db()
  return jsonify(job)  
  
# entry point
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
