'''
====================================
-- 130 - Advanced Lessons – Add Logging To Your Code 
-- link : https://www.youtube.com/watch?v=VwDzQKfYs_k&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# --------------------------------------------------
# -- Advanced_Lessons =&gt; Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name =&gt; Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level =&gt; Level of Severity
# - filename =&gt; File Name and Extension
# - mode =&gt; Mode Of The File a =&gt; Append
# - format =&gt; Format For The Log Message
# ------------------------
# getLogger =&gt; Return a Logger With the Specified Name

import logging

# print(dir(logging))

logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s =&gt; '%(message)s'",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("Elzero")

my_logger.warning("This Is Warning Message")