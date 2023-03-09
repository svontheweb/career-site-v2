from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db, load_applications_from_db, load_applications_with_id_from_db
# from email_delivery import send_mail
from email_delivery2 import send_mail, send_mail_to_hr

app = Flask(__name__)


@app.route("/")
def hello_world():
  job_list = load_jobs_from_db()
  return render_template("home.html", jobs = job_list, company_name = 'Topmate')

# APIs
@app.route("/api/jobs")
def list_jobs():
  job_list = load_jobs_from_db()
  return jsonify(job_list)

@app.route("/api/applications")
def list_applications():
  applications_list = load_applications_from_db()
  return jsonify(applications_list)

# finds data of applicants who applied for particular jobid
@app.route("/api/applications/<id>")
def find_applications_with_id(id):
  applicants_list = load_applications_with_id_from_db(id)
  return jsonify(applicants_list)

# LOADING TEMPLATES
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
  # 1. store this info in DB
  add_application_to_db(id, info)
  # 2. send confirmation email
  # send_mail() is imported from email_delivery.py file, it uses MailJest API
  send_mail(info['email'], info['full_name'])
  send_mail_to_hr(info['email'], info['full_name'])
  
  # 3. display acknoledgement page
  # find job_details to render info
  job_list = load_job_from_db(id)
  job_detail = job_list[0]
  job_title = job_detail['title']
  return render_template('application_submitted.html', application = info, job = job_title, company_name = 'Topmate')
  # TODO: 
  # 1. captcha using hCaptcha.com, to prevent web scrapping that might overload database
  # 2. API end-point to jsonify() applications for a particular 'jobid'
  # solve- on page-reload applicant info is submitted again to db with same data
  
  
# entry point
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
