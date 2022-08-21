'''
====================================
-- 133 - Flask – Intro And Your First Page 
-- link : https://www.youtube.com/watch?v=Ze_lPWFQmXI&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ----------------------------------------
# -- Flask =&gt; Intro and Your First Page --
# ----------------------------------------
# - Flask Is Micro Framework Built With Python
# --------------------------------------------
# - HTML
# - CSS
# - JavaScript
# --------------------------------------------

from flask import Flask

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return "Hello From Flask Framework"

@skills_app.route("/about")
def about():
  return "About Page From Flask Framework"

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)