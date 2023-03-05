from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

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
def list_job(id):
  job_list = load_job_from_db(id)
  # job_list is a LIST of DICTS of per job description
  if not job_list:
    return "not found", 404
  job_detail = job_list[0]
  # lists out 0th dict which is the job with particular <id> eg. /jobs/3
  return render_template('jobpage.html', job = job_detail, id= id, company_name = 'Topmate')


@app.route("/job/<id>/apply", methods=['POST'])
def apply_job(id):
  info = request.form
  return render_template('application_submitted.html', job = job_detail, id= id, company_name = 'Topmate')
  
# entry point
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
