'''
====================================
-- 134 - Flask – Create HTML Files 
-- link : https://www.youtube.com/watch?v=07qgoQngK2Q&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------------
# -- Flask =&gt; Create HTML Files --
# --------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage.html", pagetitle="Homepage")

@skills_app.route("/about")
def about():
  return render_template("about.html", pagetitle="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)