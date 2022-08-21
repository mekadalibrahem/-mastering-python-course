'''
====================================
-- 137 - Flask – Advanced CSS Task Using Jinja 
-- link : https://www.youtube.com/watch?v=CP8gG1gDbAw&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------------------------
# -- Flask =&gt; Advanced Css Task Using Jinja --
# --------------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage.html",
                          title="Homepage",
                          custom_css="home")
@skills_app.route("/add")
def add():
  return render_template("add.html",
                          title="Add Skill",
                          custom_css="add")

@skills_app.route("/about")
def about():
  return render_template("about.html", title="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)